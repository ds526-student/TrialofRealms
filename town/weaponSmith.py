import worldMap
import player
import game_data.itemsInfo as itemsInfo
import utils

def weaponSmith():
    print("Welcome " + player.playerStats.className + "!")
    print("What would you like to purchase?")
    if player.playerStats.className == "Warrior":
        print("1. Swords")
        print("2. Shields")
    elif player.playerStats.className == "Ranger":
        print("1. Bows")
        print("2. Arrows")
    elif player.playerStats.className == "Mage":
        print("1. Staffs")
        print("2. Runes")
        
    print("3. Return")
    x = utils.get_valid_int("Please select an option: ", 1, 3, return_zero_based=True)


    if x == 0:
        print("For which area would you like to purchase a weapon?")
        #Print the world locations to choose from
        for i in range(0, len(worldMap.combatAreas)):
            print(str(i + 1) +  ". " + worldMap.combatAreas[i])
            i += 1
        
        print(str(i + 1) + ". Return")
        
        x = utils.get_valid_int("Please select a location: ", 1, len(worldMap.combatAreas) + 1, return_zero_based=True)

        class_weapon_map = {
            "Warrior": [
                itemsInfo.grasslandSwords,
                itemsInfo.darkForestSword,
                itemsInfo.frozenPeakSwords,
                itemsInfo.lostCaveSwords,
                itemsInfo.burningWasteSwords
            ],
            "Ranger": [
                itemsInfo.grasslandRanged,
                itemsInfo.darkForestRanged,
                itemsInfo.frozenPeakRanged,
                itemsInfo.lostCavesRanged,
                itemsInfo.burningWasteRanged
            ],
            "Mage": [
                itemsInfo.grasslandMagic,
                itemsInfo.darkForestMagic,
                itemsInfo.frozenPeakMagic,
                itemsInfo.lostCavesMagic,
                itemsInfo.burningWasteMagic
            ]
        }

        if x < len(class_weapon_map[player.playerStats.className]):
            y = class_weapon_map[player.playerStats.className][x]
        else:
            return
        purchaseItem(y, 1, "sword", "weaponsDict")
    
    elif x == 1:
        #Print the world locations to choose from
        for i in range(0, len(worldMap.combatAreas) - 1):
            print(str(i - 1) +  ". " + worldMap.locationsList[i])
            i += 1
        if player.playerStats.className == "Warrior":
            print("From which area would you like to purchase a shield?")
            prompt = 2
            type = "shield"
            dictionary = "armourDict"
            x = utils.get_valid_int("Please select a location: ", 1, len(worldMap.locationsList) + 1, return_zero_based=True)
        elif player.playerStats.className == "Ranger":
            print("From which area would you like to purchase a quiver?")
            prompt = 3
            type = "arrow"
            dictionary = "arrowsDict"
            x = utils.get_valid_int("Please select a location: ", 1, len(worldMap.locationsList) + 1, return_zero_based=True)
        else:
            x = 0
            prompt = 4
            type = "tome"
            dictionary = "tomeDict"

        class_secondary_map = {
            "Warrior": [
                itemsInfo.grasslandShields,
                itemsInfo.darkForestShields,
                itemsInfo.frozenPeakShields,
                itemsInfo.lostCavesShields,
                itemsInfo.burningWasteShields
            ],
            "Ranger": [
                itemsInfo.grasslandArrows,
                itemsInfo.darkForestArrows,
                itemsInfo.frozenPeakArrows,
                itemsInfo.lostCavesArrows,
                itemsInfo.burningWasteArrows
            ],
            "Mage": [
                itemsInfo.tomes
            ]
        }

        if x < len(class_secondary_map[player.playerStats.className]):
            y = class_secondary_map[player.playerStats.className][x]
        else:
            return
        
        purchaseItem(y, prompt, type, dictionary)
    else:
        return
    



def purchaseItem(y, prompt="", type="", dictionary = ""):
    #Prints the list of swords you can buy based on the area you selected
    player.print_gold()

    if len(y) == 0:
        print("There are no more items available for purchase in this area")
        utils.enter()
        return
    
    for i in range(0, len(y)):
        print(str(i + 1) + ". " + str(y[i][0]) + " Price: " + str(y[i][-1]) + " gold")
        i += 1
    print(str(i + 1) + ". Return")
    
    buyItem = utils.get_valid_int("Please select a weapon for purchase: ", 1, len(y) + 1, return_zero_based=True)

    if buyItem == len(y):
        return

    print("You have selected " + str(y[buyItem][0]) + " for " + str(y[buyItem][-1]) + " gold")
    if prompt == 1:
        print("This weapon has a minimum damage of " + str(y[buyItem][1]) + " and a maximum damage of " + str(y[buyItem][2]) + " and a level requirement of " + str(y[buyItem][3]))
    elif prompt == 2:
        print("This shield has " + str(y[buyItem][1]) + " damage reduction and a level requirement of " + str(y[buyItem][3]))
    elif prompt == 3:
        print("This quiver has " + str(y[buyItem][1]) + " effect and a level requirement of " + str(y[buyItem][4]))
    elif prompt == 4:
        print("This tome has " + str(y[buyItem][1]) + " effect and a level requirement of " + str(y[buyItem][4]))
    
    x = utils.confirm("Would you like to proceed with the purchase? (y/n)")
    if x != "y":
        print("You have cancelled your purchase")
        utils.enter()
        return
    
    if player.playerStats.inventory["gold"]["amount"] >= y[buyItem][-1]:
        player.playerStats.inventory["gold"]["amount"] -= y[buyItem][-1]

        # print(str(itemsInfo.ArmourDict["Leather vest"]["price"]))
        item_dict = getattr(itemsInfo, dictionary)
        player.playerStats.inventory[str(y[buyItem][0])] = {
            **item_dict.get(str(y[buyItem][0]), {}),
            "type": type
        }

        print(str(player.playerStats.inventory[str(y[buyItem][0])]))

        y.pop(buyItem)

        # Add information from the dictionary with the same name
        player.print_gold()
        print("You have purchased " + str(y[buyItem][0]) + " for " + str(y[buyItem][-1]) + " gold")
        utils.enter()
    else:
        print("You do not have enough gold to purchase this item")
        utils.enter()