import game_data.Enemy as Enemy
import Player
import WorldMap
import combat   
import game_data.itemsInfo as itemsInfo
import os
import town.potionBrewer as potionBrewer
import town.weaponSmith as weaponSmith
import town.armourDealer as armourDealer
import town.beastiary as beastiary
import inventory
import utils    

#Select the location you would like to travel to 
def traveling():
    print("Where would you like to travel to?")

    #Prints the list of places you can travel to 
    for i in range(0, len(WorldMap.locationsList)):
        print(str(i + 1) +  ". " + WorldMap.locationsList[i])
        i += 1

    x = utils.get_valid_int("Please select a location: ", 1, len(WorldMap.locationsList) + 1)

    #Checks to see if your input is within range of the list of possible places to travel
    if x > 1 and x < len(WorldMap.locationsList) + 1:
        if x > 2:
            print("Welcome to " + WorldMap.displayLocationsList[x - 1] + "!")
        return x
    elif x == 1:
        print("You have opened your inventory")
        return x
    else:
        print("Invalid response please try again")

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
    print("You have been healed to full health")
    print("Welcome to town! What would you like to do?")

    #Prints the list of things you can do in town
    town_list = WorldMap.get_town_list()
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
        weaponSmith.swordSmither()
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
classSelection = utils.get_valid_int("Please select a class: ", 1, 4)
if classSelection == 1:
    Player.playerStats.className = "Warrior"
    Player.playerStats.weapon = "Wooden Sword"
if classSelection == 2:
    Player.playerStats.className = "Mage"
    Player.playerStats.weapon = "Cracked Wand"
if classSelection == 3:
    Player.playerStats.className = "Ranger"
    Player.playerStats.weapon = "Worn Bow"
print("You have selected " + Player.playerStats.className + "!")
print("You are now ready to begin your adventure!")
print("Good luck!")
utils.enter()

#forever loop so that the game never ends unless manually closed
while True:
    #Clears the console
    os.system('cls' if os.name == 'nt' else 'clear')
    x = traveling()
    if x == 8:
        combat.pickingDungeon()
    elif x >= 3:
        enemyStats, initialHealth = combat.pickingEnemy(x)
        combat.combatSit(initialHealth, enemyStats) 
    elif x == 2:
        town()
    elif x == 1:
        inventory.openInventory()