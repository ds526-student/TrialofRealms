import WorldMap
import Player
import game_data.itemsInfo as itemsInfo
import utils

def swordSmither():
    print("For which area would you like to purchase a weapon?")
    #Print the world locations to choose from
    for i in range(2, len(WorldMap.locationsList) - 1):
        print(str(i - 1) +  ". " + WorldMap.locationsList[i])
        i += 1
    
    print(str(i - 1) + ". Return")
    
    x = utils.get_valid_int("Please select a location: ", 1, len(WorldMap.locationsList) + 1, return_zero_based=True)

    if x == 0:
        y = itemsInfo.grasslandSwords
    elif x == 1:
        y = itemsInfo.darkForestSword
    elif x == 2:
        y = itemsInfo.frozenPeakSwords
    elif x == 3:
        y = itemsInfo.lostCaveSwords
    elif x == 4:
        y = itemsInfo.burningWasteSwords
    elif x == 5:
        return

    
    #Prints the list of swords you can buy based on the area you selected
    Player.print_gold()

    if y == itemsInfo.grasslandSwords and len(y) > 0 and y[0][0] == "Wooden Sword": 
        y.pop(0) 

    if len(y) == 0:
        print("There are no more swords available in this area")
        utils.enter()
        return
    
    for i in range(0, len(y)):
        print(str(i + 1) + ". " + str(y[i][0]) + " Price: " + str(y[i][4]) + " gold")
        i += 1
    print(str(i + 1) + ". Return")
    
    buyItem = utils.get_valid_int("Please select a weapon for purchase: ", 1, len(y) + 1, return_zero_based=True)

    if buyItem == len(y):
        return

    print("You have selected " + str(y[buyItem][0]) + " for " + str(y[buyItem][4]) + " gold")
    print("This weapon has a minimum damage of " + str(y[buyItem][1]) + " and a maximum damage of " + str(y[buyItem][2]) + " and a level requirement of " + str(y[buyItem][3]))
    
    x = utils.confirm("Would you like to proceed with the purchase? (y/n)")
    if x != "y":
        print("You have cancelled your purchase")
        utils.enter()
        return
    
    if Player.playerStats.inventory["gold"]["amount"] >= y[buyItem][4]:
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
        print("You have purchased " + str(y[buyItem][0]) + " for " + str(y[buyItem][4]) + " gold")
        utils.enter()
    else:
        print("You do not have enough gold to purchase this item")
        utils.enter()