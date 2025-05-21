import WorldMap
import Player
import game_data.itemsInfo

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
            print("You currently have " + Player.playerStats.weapon + " equipped")
            swordList = []  
            for item, details in Player.playerStats.inventory.items():
                if isinstance(details, list) and details[0].get('type') == 'sword':
                    swordList.append(f"{i} - {item}: Min DPS: {details[0].get('minDps', 'N/A')} Max DPS: {details[0].get('maxDps', 'N/A')}")
                elif isinstance(details, dict) and details.get('type') == 'sword':
                    swordList.append(f"{i} - {item}: Min DPS: {details.get('minDps', 'N/A')} Max DPS: {details.get('maxDps', 'N/A')}")
                i += 1  
                equipmentList.append(item)
                if len(swordList) == 0:
                    print("You have no swords in your inventory")
                    print("Press enter to continue")
                    input()
                    return
            print("Which item would you like to equip?")
            Player.playerStats.inventory[Player.playerStats.weapon] = {
                **itemsInfo.SwordsDict.get(Player.playerStats.weapon, {}),
                "type": "sword"
            }

            invalidResponse = True
            while invalidResponse:
                try:
                    x = int(input())
                    if x > 0 and x < len(swordList) + 1:
                        invalidResponse = False
                    else: 
                        print("Invalid response please try again")
                except ValueError:
                    print("Invalid response please try again")

            item = equipmentList[x]
            if itemsInfo.SwordsDict[item]["levelReq"] > Player.playerStats.level:
                print("You are not a high enough level to equip this item")
            else:
                Player.playerStats.weapon = equipmentList[x]
                Player.playerStats.minimumDamage = itemsInfo.SwordsDict[equipmentList[x]]["minDps"]
                Player.playerStats.maximumDamage = itemsInfo.SwordsDict[equipmentList[x]]["maxDps"]
            
        elif x == "a":
            print("You currently have " + Player.playerStats.armour + " equipped")
            armourList = []
            for item, details in Player.playerStats.inventory.items():
                if isinstance(details, list) and details[0].get('type') == 'armour':
                    armourList.append(f"{i} - {item}: Damage Reduction: {details[0].get('dmgRed', 'N/A')}")
                elif isinstance(details, dict) and details.get('type') == 'armour':
                    armourList.append(f"{i} - {item}: Damage Reduction: {details.get('dmgRed', 'N/A')}")
                i += 1
                equipmentList.append(item)
                if len(armourList) == 0:
                    print("You have no armour in your inventory")
                    print("Press enter to continue")
                    input()
                    return
            print("Which item would you like to equip?")

            invalidResponse = True
            while invalidResponse:
                try:
                    x = int(input())
                    if x > 0 and x < len(armourList) + 1:
                        invalidResponse = False
                    else: 
                        print("Invalid response please try again")
                except ValueError:
                    print("Invalid response please try again")

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
    equipmentList.clear()
    i = 0