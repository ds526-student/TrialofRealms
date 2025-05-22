import player
import game_data.itemsInfo as itemsInfo
import utils

#Handles your interaction/s with the Potion Brewer
def potionBrewer():
    # prints the amount of available gold that you have in your inventory
    player.print_gold()
    # prints the full list of available health potions
    for i in range(0, len(itemsInfo.healthPotions)):
        print(str(i + 1) + ". " + str(itemsInfo.healthPotions[i][0]) + " Price: " + str(itemsInfo.healthPotions[i][2]) + " gold")
        i += 1

    print(str(i + 1) + ". Return")

    buyItem = utils.get_valid_int("Please select a health potion: ", 1, len(itemsInfo.healthPotions) + 1, return_zero_based=True)
    
    print("You have selected " + str(itemsInfo.healthPotions[buyItem - 1][0]) + " for " + str(itemsInfo.healthPotions[buyItem - 1][2]) + " gold")
    print("This health potion will heal " + str(itemsInfo.healthPotions[buyItem - 1][1]) + " health")
    x = input("Would you still like to purchase this item? (y/n) ")
    if x is not "y":
        print("You have cancelled your purchase")
        return
    
    # asks how many health potions you want to buy
    print("How many " + str(itemsInfo.healthPotions[buyItem - 1][0]) + " would you like to buy?")

    amount = utils.get_valid_int("Enter amount: ", 1, 1000, return_zero_based=True)

    # checks if you have enough gold to buy the health potions
    if player.playerStats.inventory["gold"]["amount"] >= itemsInfo.healthPotions[buyItem - 1][2] * amount:
        player.playerStats.inventory["gold"]["amount"] -= itemsInfo.healthPotions[buyItem - 1][2] * amount

        # adds the health potions to your inventory inventory[potionName] | prints remaining gold and number of available health potions
        player.playerStats.inventory[str(itemsInfo.healthPotions[buyItem - 1][0])]["amount"] += amount
        player.print_gold()
        print("You now have " + str(player.playerStats.inventory[str(itemsInfo.healthPotions[buyItem - 1][0])]["amount"]) + " " + str(itemsInfo.healthPotions[buyItem - 1][0]) + "(s) in your inventory")
        utils.enter()
    else:
        print("You do not have enough gold to purchase this item")
        utils.enter()
        return