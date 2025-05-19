import Enemy
import Player
import WorldMap
import combat   
import itemsInfo
import os

#Select the location you would like to travel to 
def traveling():
    print("Where would you like to travel to?")

    #Prints the list of places you can travel to 
    for i in range(0, len(WorldMap.locationsList)):
        print(str(i + 1) +  ". " + WorldMap.locationsList[i])
        i += 1

    #Prints you current location
    invalidResponse = True
    while invalidResponse:
        x = int(input())
        #Checks to see if your input is within range of the list of possible places to travel
        if x > 1 and x < len(WorldMap.locationsList) + 1:
            print("You are now in " + WorldMap.locationsList[x - 1])
            invalidResponse = False
            return x
        elif x == 1:
            print("You have opened your inventory")
            return x
        else:
            print("Invalid response please try again")

#Handles your interaction/s with the sword smith
def swordSmith():
    print("For which area would you like to purchase a weapon?")
    #Print the world locations to choose from
    for i in range(2, len(WorldMap.locationsList)):
        print(str(i - 1) +  ". " + WorldMap.locationsList[i])
        i += 1
    x = int(input())
    if x == 1:
        y = itemsInfo.grasslandSwords
    elif x == 2:
        y = itemsInfo.darkForestSword
    elif x == 3:
        y = itemsInfo.frozenPeakSwords
    elif x == 4:
        y = itemsInfo.lostCaveSwords
    elif x == 5:
        y = itemsInfo.burningWasteSwords
    
    #Prints the list of swords you can buy based on the area you selected
    Player.print_gold()

    if y == itemsInfo.grasslandSwords:
        y.pop(0)
    for i in range(0, len(y)):
        print(str(i + 1) + ". " + str(y[i][0]) + " Price: " + str(y[i][4]) + " gold")
        i += 1
    print(str(i + 1) + ". Return")
    
    #Checks to see if you can buy an item or not
    buyItem = int(input()) - 1
    if buyItem == len(y):
        return
    elif Player.playerStats.inventory["gold"]["amount"] >= y[buyItem][4]:
        Player.playerStats.inventory["gold"]["amount"] -= y[buyItem][4]

        # print(str(itemsInfo.ArmourDict["Leather vest"]["price"]))
        Player.playerStats.inventory[str(y[buyItem][0])] = {
            **itemsInfo.SwordsDict.get(str(y[buyItem][0]), {}),
            "type": "sword"
        }

        print(str(Player.playerStats.inventory[str(y[buyItem][0])]))

        y.pop(buyItem)

        # Add information from the dictionary with the same name
        Player.print_gold()
    else:
        print("You do not have enough gold to purchase this item")

#Handles your interaction/s with the Amourments Dealer
def amourmentsDealer():
        print("For which area would you like to purchase your armour?")
        #Print the world locations to choose from
        for i in range(2, len(WorldMap.locationsList)):
            print(str(i - 1) +  ". " + WorldMap.locationsList[i])
            i += 1
        x = int(input())
        if x == 1:
            y = itemsInfo.grasslandArmour
        elif x == 2:
            y = itemsInfo.darkForestArmour
        elif x == 3:
            y = itemsInfo.frozenPeakArmour
        elif x == 4:
            y = itemsInfo.lostCavesArmour
        elif x == 5:
            y = itemsInfo.burningWasteArmour
        
        #Prints the list of swords you can buy based on the area you selected
        Player.print_gold()
        for i in range(0, len(y)):
            print(str(i + 1) + ". " + str(y[i][0]) + " Price: " + str(y[i][3]) + " gold")
            i += 1
        print(str(i + 1) + ". Return")
        
        #Checks to see if you can buy an item or not
        buyItem = int(input()) - 1
        if buyItem == len(y):
            return
        elif Player.playerStats.inventory["gold"]["amount"] >= y[buyItem][3]:
            Player.playerStats.inventory["gold"]["amount"] -= y[buyItem][3]

            # print(str(itemsInfo.ArmourDict["Leather vest"]["price"]))
            Player.playerStats.inventory[str(y[buyItem][0])] = {
                **itemsInfo.ArmourDict.get(str(y[buyItem][0]), {}),
                "type": "armour"
            }   

            print(str(Player.playerStats.inventory[str(y[buyItem][0])]))

            y.pop(buyItem)

            Player.print_gold()
        else:
            print("You do not have enough gold to purchase this item")

#Handles your interaction/s with the Potion Brewer
def potionBrewer():
    # prints the amount of available gold that you have in your inventory
    Player.print_gold()
    # prints the full list of available health potions
    for i in range(0, len(itemsInfo.healthPotions)):
        print(str(i + 1) + ". " + str(itemsInfo.healthPotions[i][0]) + " Price: " + str(itemsInfo.healthPotions[i][2]) + " gold")
        i += 1

    print(str(i + 1) + ". Return")

    # selects the health potion that you want to buy
    buyItem = int(input()) - 1

    if buyItem == len(itemsInfo.healthPotions):
        return
    
    # asks how many health potions you want to buy
    print("How many " + str(itemsInfo.healthPotions[buyItem][0]) + " would you like to buy?")
    amount = int(input())

    # checks if you have enough gold to buy the health potions
    if Player.playerStats.inventory["gold"]["amount"] >= itemsInfo.healthPotions[buyItem][2] * amount:
        Player.playerStats.inventory["gold"]["amount"] -= itemsInfo.healthPotions[buyItem][2] * amount

        # adds the health potions to your inventory inventory[potionName] | prints remaining gold and number of available health potions
        Player.playerStats.inventory[str(itemsInfo.healthPotions[buyItem][0])]["amount"] += amount
        Player.print_gold()
        print("You now have " + str(Player.playerStats.inventory[str(itemsInfo.healthPotions[buyItem][0])]["amount"]) + " " + str(itemsInfo.healthPotions[buyItem][0]) + "(s) in your inventory")
    else:
        print("You do not have enough gold to purchase this item")
        return

#Prints enemy stats and drop rates based on the enemies you've killed
def dictionary():
    print("Currently not available")

#Prints all player stats to the user
def playerStats():
    print(str(Player.playerStats.health) + "/" + str(Player.playerStats.maximumHealth) + " health")
    print("Weapon: " + Player.playerStats.weapon + " DPS: " + str(Player.playerStats.minimumDamage) + "->" + str(Player.playerStats.maximumDamage))
    print("Armour: " + Player.playerStats.armour + " Damage Reduction: " + str(Player.playerStats.damageReduction))
    print("Level " + str(Player.playerStats.level) + " " + str(Player.playerStats.xp) + "/" + str(int(100 * (Player.playerStats.level**1.5))) + "xp")
    input()

#Allows you to interact with the stuff in town
def town():
    Player.playerStats.health = Player.playerStats.maximumHealth
    print("Welcome to town! What would you like to do?")

    #Prints the list of things you can do in town
    for i in range(0, len(WorldMap.townList)):
        print(str(i + 1) +  ". " + WorldMap.townList[i])
        i += 1

    #Choose what activity you would like to do within town
    invalidResponse = True
    while invalidResponse:
        x = int(input())
        if x > 0 and x < len(WorldMap.townList) + 1:
            print("You are now speaking to the " + WorldMap.townList[x - 1])
            invalidResponse = False
        else:
            print("Invalid response please try again")

    #When talking to the sword smith choose which area you would like to purchase your weapon from 
    if x == 1:
        swordSmith()
    elif x == 2:
        amourmentsDealer()
    elif x == 3:
        potionBrewer()
    elif x == 4:
        dictionary()
    elif x == 5:
        playerStats()

#Displays all the items within your inventory
def openInventory():
    Player.print_inventory()
    print("Would you like to equip any gear? (y/n)")
    x = input()
    equipmentList = []
    i = 0
    if x == "y":
        print("weapon or armour? (w/a)")
        x = input()
        if x == "w":
            for item, details in Player.playerStats.inventory.items():
                if isinstance(details, list) and details[0].get('type') == 'sword':
                    print(f"{i} - {item}: Min DPS: {details[0].get('minDps', 'N/A')} Max DPS: {details[0].get('maxDps', 'N/A')}")
                elif isinstance(details, dict) and details.get('type') == 'sword':
                    print(f"{i} - {item}: Min DPS: {details.get('minDps', 'N/A')} Max DPS: {details.get('maxDps', 'N/A')}")
                i += 1  
                equipmentList.append(item)
            print("Which item would you like to equip?")
            Player.playerStats.inventory[Player.playerStats.weapon] = {
                **itemsInfo.SwordsDict.get(Player.playerStats.weapon, {}),
                "type": "sword"
            }
            x = int(input())
            item = equipmentList[x]
            if itemsInfo.SwordsDict[item]["levelReq"] > Player.playerStats.level:
                print("You are not a high enough level to equip this item")
            else:
                Player.playerStats.weapon = equipmentList[x]
                Player.playerStats.minimumDamage = itemsInfo.SwordsDict[equipmentList[x]]["minDps"]
                Player.playerStats.maximumDamage = itemsInfo.SwordsDict[equipmentList[x]]["maxDps"]
            
        elif x == "a":
            for item, details in Player.playerStats.inventory.items():
                if isinstance(details, list) and details[0].get('type') == 'armour':
                    print(f"{i} - {item}: Damage Reduction: {details[0].get('dmgRed', 'N/A')}")
                elif isinstance(details, dict) and details.get('type') == 'armour':
                    print(f"{i} - {item}: Damage Reduction: {details.get('dmgRed', 'N/A')}")
                i += 1
                equipmentList.append(item)
            print("Which item would you like to equip?")
            x = int(input())
            Player.playerStats.inventory[Player.playerStats.armour] = {
                **itemsInfo.ArmourDict.get(Player.playerStats.armour, {}),
                "type": "armour"
            }
            item = equipmentList[x]
            if itemsInfo.ArmourDict[item]["levelReq"] > Player.playerStats.level:
                print("You are not a high enough level to equip this item")
            else:
                Player.playerStats.armour = equipmentList[x]
                Player.playerStats.damageReduction = itemsInfo.ArmourDict[equipmentList[x]]["dmgRed"]
        else:
            return
    else:
        Player.print_inventory()
    equipmentList.clear()
    i = 0

def printStats(enemy_stats):
    print(f"Health: {enemy_stats[0]} \nMin Damage: {enemy_stats[1]} \nMax Damage: {enemy_stats[2]}")
    print()
    print("Player (Level " + str(Player.playerStats.level) + ") \nHealth: " + str(Player.playerStats.health) + " \nMin Damage: " + str(Player.playerStats.minimumDamage) + " \nMax Damage: " + str(Player.playerStats.maximumDamage) + "\nDamage Reduction: " + str(Player.playerStats.damageReduction))

#forever loop so that the game never ends unless manually closed
while True:
    x = traveling()
    if x == 8:
        combat.pickingDungeon()
    elif x >= 3:
        enemyStats, initialHealth = combat.pickingEnemy(x)
        combat.combatSit(initialHealth, enemyStats) 
    elif x == 2:
        town()
    elif x == 1:
        openInventory()