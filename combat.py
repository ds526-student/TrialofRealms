import Player
import game_data.Enemy as Enemy
import game_data.itemsInfo as itemsInfo
import utils
import town.beastiary as beastiary

globalEnemyDict = {}
globalEnemyName = ""

def attack(minDmg, maxDmg):
    from random import randrange
    return randrange(minDmg, maxDmg)

def loot(minCoins, maxCoins):
    from random import randrange
    return randrange(minCoins, maxCoins)  

#Select the enemy that you want to fight based on your location 
def enemySelection(list, array):
    global globalEnemyName
    #print each of the enemies in the area
    for i in range(0, len(list)):
        print(str(i + 1) +  ". " + list[i])
        i += 1

    x = utils.get_valid_int("Please select an enemy: ", 1, len(list) + 1, return_zero_based=True)

    if x == "6":
        print("You have now entered the " + str(list[5]))
    else:
        print(list[int(x)])
        globalEnemyName = list[int(x)]
        #Print player and enemy stats
        enemy_stats = array[int(x)]
        printStats(enemy_stats)
        return enemy_stats

#Allows you to choose what enemy you want to fight depending on your location
def pickingEnemy(x):
    global globalEnemyDict
    print("Pick an enemy to fight")
    if x == 3:
        globalEnemyDict = Enemy.grasslandBeast
        enemyStats = enemySelection(Enemy.grasslandEnemies, Enemy.grasslandStats)
    elif x == 4:
        globalEnemyDict = Enemy.darkForestBeast
        enemyStats = enemySelection(Enemy.darkForestEnemies, Enemy.darkForestStats)
    elif x == 5:
        globalEnemyDict = Enemy.frozenPeakBeast
        enemyStats = enemySelection(Enemy.frozenPeaksEnemies, Enemy.frozenPeakStats)
    elif x == 6:
        globalEnemyDict = Enemy.lostCaveBeast
        enemyStats = enemySelection(Enemy.lostCavesEnemies, Enemy.lostCaveStats)
    elif x == 7:
        globalEnemyDict = Enemy.burningWastesBeast
        enemyStats = enemySelection(Enemy.burningWastesEnemies, Enemy.burningWastesStats)
    
    initialHealth = enemyStats[0]
    return enemyStats, initialHealth

#Fighting, Buffing, and Running is managed here
def combatSit(initialHealth, enemyStats):
    cooldown = 0
    #While the enemy is not dead run the method
    while enemyStats[0] > 0:
        print("Attack, Buff, or Run? (a/b/r)")
        action = input()
        #Applies damage to the player and the enemy
        if action == "a":
            enemyDamage = attack(enemyStats[1], enemyStats[2])
            playerDamage = attack(Player.playerStats.minimumDamage, Player.playerStats.maximumDamage)

            enemyStats[0] -= playerDamage

            if enemyStats[0] <= 0:
                print("Enemy Health: 0")
                enemyDead = True
            else:
                Player.playerStats.health -= enemyDamage
                #When enemy is dead set enemyDead = true
                print("Player Health: " + str(Player.playerStats.health))
                print("Enemy Health: " + str(enemyStats[0]))
        elif action == "b":
            if cooldown > 0:
                print("You cannot use a consumable yet")
                continue
            elif Player.playerStats.health == Player.playerStats.maximumHealth:
                print("You are already at full health")
                continue
            else:
                Player.print_consumables()

                x = int(input()) - 1

                if x == len(itemsInfo.healthPotions):
                    return

                Player.playerStats.health += itemsInfo.healthPotions[x][1]
                Player.playerStats.inventory[itemsInfo.healthPotions[x][0]]["amount"] -= 1

                if Player.playerStats.health > Player.playerStats.maximumHealth:
                    Player.playerStats.health = Player.playerStats.maximumHealth

                print("Player Health: " + str(Player.playerStats.health))
                print("Enemy Health: " + str(enemyStats[0]))

                cooldown = 3
        elif action == "r":
            return
        else:
            print("Invalid input")
            continue
    enemyStats[0] = initialHealth
    #If the enemy is dead provide players with xp and roll drops
    if enemyDead:
        xpEarned = Player.xpCalc(Player.playerStats.level, enemyStats[3])
        xpRequired = Player.addXp(xpEarned)
        gold = loot(enemyStats[4], enemyStats[5])
        Player.playerStats.inventory["gold"]["amount"] += gold
        print("The enemy dropped " + str(gold) + " gold")
        Player.print_gold()
        utils.enter()
        beastiary.beastLogEntry(globalEnemyDict, globalEnemyName)


def pickingDungeon():
    global globalEnemyDict
    global globalEnemyName
    #Prints the list of dungeons you can travel to
    for i in range(0, len(Enemy.dungeons)):
        print(str(i + 1) +  ". " + Enemy.dungeons[i])
        i += 1

    i += 1
    print(str(i) + ". Return")
    print("Pick a dungeon to fight")
    x = utils.get_valid_int("Please select a dungeon: ", 1, len(Enemy.dungeons) + 1, return_zero_based=True)
    print("This dungeon will contain these enemies:")

    # assigns the correct list of weapons and armours based on the players class

    if x == 0:
        enemyStats = Enemy.grasslandStats
        dungeon = Enemy.burrowEnemies
        globalEnemyDict = Enemy.grasslandBeast
    elif x == 1:
        enemyStats = Enemy.darkForestStats
        dungeon = Enemy.heartEnemies
        globalEnemyDict = Enemy.darkForestBeast
    elif x == 2:
        enemyStats = Enemy.frozenPeakStats
        dungeon = Enemy.cradleEnemies
        globalEnemyDict = Enemy.frozenPeakBeast
    elif x == 3:
        enemyStats = Enemy.lostCaveStats
        dungeon = Enemy.vaultEnemies
        globalEnemyDict = Enemy.lostCaveBeast
    elif x == 4:
        enemyStats = Enemy.burningWastesStats
        dungeon = Enemy.infernalEnemies
        globalEnemyDict = Enemy.burningWastesBeast
    elif x == len(Enemy.dungeons):
        return

    if Player.playerStats.className == "Warrior":
        weaponReward = itemsInfo.dungeonSwords[x][0]   
        armourReward = itemsInfo.dungeonMeleeArmours[x][0]
    elif Player.playerStats.className == "Ranger":
        weaponReward = itemsInfo.dungeonRanged[x][0]   
        armourReward = itemsInfo.dungeonRangedArmours[x][0]
    elif Player.playerStats.className == "Mage":
        weaponReward = itemsInfo.dungeonMagic[x][0]   
        armourReward = itemsInfo.dungeonMageArmours[x][0]
        print(dungeon)

    y = utils.confirm("Would you like to enter the dungeon? (y/n) ")

    if y == "y":
        print("You have entered the " + Enemy.dungeons[x - 1])

        print("You have encountered " + str(dungeon[0]))
        printStats(enemyStats[1])
        globalEnemyName = dungeon[0]
        combatSit(dungeon[0], enemyStats[1].copy())

        print("You have encountered " + str(dungeon[1]))
        printStats(enemyStats[2])
        globalEnemyName = dungeon[1]
        combatSit(dungeon[1], enemyStats[2].copy())

        print("You have encountered " + str(dungeon[2]))
        printStats(enemyStats[3])
        globalEnemyName = dungeon[2]
        combatSit(dungeon[2], enemyStats[3].copy())

        print("You have encountered " + str(dungeon[3]))
        printStats(enemyStats[5])
        globalEnemyName = dungeon[3]
        combatSit(dungeon[3], enemyStats[5].copy())

        print("You have completed the dungeon")
        print("You have received " + weaponReward + " and " + armourReward)
        # print(str(itemsInfo.ArmourDict["Leather vest"]["price"]))
        Player.playerStats.inventory[str(weaponReward)] = {
            **itemsInfo.weaponsDict.get(str(weaponReward), {}),
            "type": "sword"
        }
        
        Player.playerStats.inventory[str(armourReward)] = {
            **itemsInfo.armourDict.get(str(armourReward), {}),
            "type": "armour"
        }   
        utils.enter()
    else:
        return

def printStats(enemy_stats):
    print(f"Level: {enemy_stats[3]} \nHealth: {enemy_stats[0]} \nMin Damage: {enemy_stats[1]} \nMax Damage: {enemy_stats[2]}")
    print()
    print("Player (Level " + str(Player.playerStats.level) + ") \nHealth: " + str(Player.playerStats.health) + " \nMin Damage: " + str(Player.playerStats.minimumDamage) + " \nMax Damage: " + str(Player.playerStats.maximumDamage) + "\nDamage Reduction: " + str(Player.playerStats.damageReduction))