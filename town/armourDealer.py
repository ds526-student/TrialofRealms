import worldMap
import player
import game_data.itemsInfo as itemsInfo
import utils

#Handles your interaction/s with the Amourments Dealer
def amourmentsDealer():
    print("For which area would you like to purchase your armour?")
    #Print the world locations to choose from
    for i in range(2, len(worldMap.locationsList) - 1):
        print(str(i - 1) +  ". " + worldMap.locationsList[i])
        i += 1
    
    print(str(i - 1) + ". Return")

    x = utils.get_valid_int("Please select a location: ", 1, len(worldMap.locationsList) + 1, return_zero_based=True)

    if player.playerStats.className == "Warrior":
        if x == 0:
            y = itemsInfo.grasslandMeleeArmour
        elif x == 1:
            y = itemsInfo.darkForestMeleeArmour
        elif x == 2:
            y = itemsInfo.frozenPeakMeleeArmour
        elif x == 3:
            y = itemsInfo.lostCavesMeleeArmour
        elif x == 4:
            y = itemsInfo.burningWasteMeleeArmour
        elif x == 5:
            return
    elif player.playerStats.className == "Ranger":
        if x == 0:
            y = itemsInfo.grasslandRangedArmour
        elif x == 1:
            y = itemsInfo.darkForestRangedArmour
        elif x == 2:
            y = itemsInfo.frozenPeakRangedArmour
        elif x == 3:
            y = itemsInfo.lostCavesRangedArmour
        elif x == 4:
            y = itemsInfo.burningWasteRangedArmour
        elif x == 5:
            return
    elif player.playerStats.className == "Mage":
        if x == 0:
            y = itemsInfo.grasslandMageArmour
        elif x == 1:
            y = itemsInfo.darkForestMageArmour
        elif x == 2:
            y = itemsInfo.frozenPeakMageArmour
        elif x == 3:
            y = itemsInfo.lostCavesMageArmour
        elif x == 4:
            y = itemsInfo.burningWasteMageArmour
        elif x == 5:
            return
    
    #Prints the list of swords you can buy based on the area you selected
    player.print_gold()

    if len(y) == 0:
        print("There is no more armour available in this area")
        utils.enter()
        return
    
    for i in range(0, len(y)):
        print(str(i + 1) + ". " + str(y[i][0]) + " Price: " + str(y[i][3]) + " gold")
        i += 1
    print(str(i + 1) + ". Return")
    
    buyItem = utils.get_valid_int("Please select an item: ", 1, len(y) + 1, return_zero_based=True)

    if buyItem == len(y):
        return
            
    print("You have selected " + str(y[buyItem][0]) + " for " + str(y[buyItem][3]) + " gold")
    print("This armour has a damage reduction of " + str(y[buyItem][1]) + " and a level requirement of " + str(y[buyItem][2]))
    x = input("Would you still like to purchase this item? (y/n) ")
    if x is not "y":
        print("You have cancelled your purchase")
        return

    if player.playerStats.inventory["gold"]["amount"] >= y[buyItem][3]:
        player.playerStats.inventory["gold"]["amount"] -= y[buyItem][3]

        # print(str(itemsInfo.ArmourDict["Leather vest"]["price"]))
        player.playerStats.inventory[str(y[buyItem][0])] = {
            **itemsInfo.meleeArmourDict.get(str(y[buyItem][0]), {}),
            "type": "armour"
        }   

        print(str(player.playerStats.inventory[str(y[buyItem][0])]))

        y.pop(buyItem)

        player.print_gold()
        print("You have purchased " + str(y[buyItem][0]) + " for " + str(y[buyItem][3]) + " gold")
        utils.enter()
    else:
        print("You do not have enough gold to purchase this item")
        utils.enter()