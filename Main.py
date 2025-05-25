import player
import worldMap
import fighting.combat as combat   
import game_data.itemsInfo as itemsInfo
import os
import town.potionBrewer as potionBrewer
import town.weaponSmith as weaponSmith
import town.armourDealer as armourDealer
import town.beastiary as beastiary
import inventory
import utils    
import skilling.skillSelection as skillSelection

#Select the location you would like to travel to 
def traveling():
    print("Where would you like to travel to?")

    #Prints the list of places you can travel to 
    for i in range(0, len(worldMap.locationsList)):
        print(str(i + 1) +  ". " + worldMap.locationsList[i])
        i += 1

    x = utils.get_valid_int("Please select a location: ", 1, len(worldMap.locationsList) + 1)

    #Checks to see if your input is within range of the list of possible places to travel
    if x > 1 and x < len(worldMap.locationsList) + 1:
        if x > 2:
            print("Welcome to " + worldMap.locationsList[x - 1] + "!")
        return x
    elif x == 1:
        print("You have opened your inventory")
        return x
    else:
        print("Invalid response please try again")

#Prints all player stats to the user
def playerStats():
    print("Class: " + player.playerStats.className)
    print("Level " + str(player.playerStats.playerLevel) + " " + str(player.playerStats.playerXp) + "/" + str(int(100 * (player.playerStats.playerLevel**1.5))) + "xp")
    print(str(player.playerStats.health) + "/" + str(player.playerStats.maximumHealth) + " health")
    print("Weapon: " + player.playerStats.weapon + " DPS: " + str(player.playerStats.minimumDamage) + "->" + str(player.playerStats.maximumDamage))
    print("Shield: " + player.playerStats.shield + " Damage Reduction: " + str(itemsInfo.armourDict[player.playerStats.shield]["dmgRed"]))
    print("Armour: " + player.playerStats.armour + " Damage Reduction: " + str(itemsInfo.armourDict[player.playerStats.armour]["dmgRed"]))
    print("Total Damage Reduction: " + str(player.playerStats.damageReduction))
    input()

#Allows you to interact with the stuff in town
def town():
    player.playerStats.health = player.playerStats.maximumHealth
    print("You have been healed to full health")
    print("Welcome to town! What would you like to do?")

    #Prints the list of things you can do in town
    town_list = worldMap.get_town_list()
    for i in range(0, len(town_list)):
        print(str(i + 1) +  ". " + town_list[i])
        i += 1

    i += 1
    print(str(i) + ". Return")

    x = utils.get_valid_int("Please select an activity: ", 1, len(town_list) + 1, return_zero_based=True)

    if x is len(town_list) + 1:
        return
    elif x >= 0 and x < len(town_list) + 1:
        print("You are now speaking to the " + town_list[x])

    # choose which shop you want to go to
    if x == 0:
        weaponSmith.weaponSmith()
    elif x == 1:
        armourDealer.amourmentsDealer()
    elif x == 2:
        potionBrewer.potionBrewer()
    elif x == 3:
        beastiary.beastLog()
    elif x == 4:
        playerStats()


os.system('cls' if os.name == 'nt' else 'clear')
print("Welcome to Trial of Realms!")
print("You are a brave adventurer who has set out to explore the world of Trial of Realms.")
print("You will encounter many enemies and challenges along the way.")
print("You will need to use your skills and items to survive.")
print()
print("But first we need to select your class")
print("You have 3 classes to choose from:")
print("1. Warrior: A strong and durable fighter.")
print("2. Mage: A powerful spellcaster.")
print("3. Ranger: A skilled archer and hunter.")

classSelection = utils.get_valid_int("Please select a class: ", 1, 3)
if classSelection == 1:
    player.playerStats.className = "Warrior"
    player.playerStats.weapon = "Wooden Sword"
    itemsInfo.grasslandSwords.pop(0)
if classSelection == 2:
    player.playerStats.className = "Mage"
    player.playerStats.weapon = "Cracked Wand"
    itemsInfo.grasslandMagic.pop(0)
if classSelection == 3:
    player.playerStats.className = "Ranger"
    player.playerStats.weapon = "Worn Bow"
    itemsInfo.grasslandRanged.pop(0)

print("You have selected " + player.playerStats.className + "!")
print("You are now ready to begin your adventure!")
print("Good luck!")
utils.enter()

#forever loop so that the game never ends unless manually closed
while True:
    #Clears the console
    os.system('cls' if os.name == 'nt' else 'clear')
    x = traveling()
    if x == 1:
        inventory.openInventory()
    elif x == 2:
        town()
    elif x == 3:
        skillSelection.skillsSelect()
    elif x == 4:
        combat.pickingCombatArea()