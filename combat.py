import Player
import Enemy
import itemsInfo

def attack(minDmg, maxDmg):
    from random import randrange
    return randrange(minDmg, maxDmg)

def loot(minCoins, maxCoins):
    from random import randrange
    return randrange(minCoins, maxCoins)  

#Select the enemy that you want to fight based on your location 
def enemySelection(list, array):
    #print each of the enemies in the area
    for i in range(0, len(list)):
        print(str(i + 1) +  ". " + list[i])
        i += 1
    x = input()
    if x == "6":
        print("You have now entered the " + str(list[5]))
    else:
        print(list[int(x) - 1])
        #Print player and enemy stats
        enemy_stats = array[int(x) - 1]
        printStats(enemy_stats)
        return enemy_stats

#Allows you to choose what enemy you want to fight depending on your location
def pickingEnemy(x):
    print("Pick an enemy to fight")
    if x == 3:
        enemyStats = enemySelection(Enemy.grasslandEnemies, Enemy.grasslandStats)
    elif x == 4:
        enemyStats = enemySelection(Enemy.darkForestEnemies, Enemy.darkForestStats)
    elif x == 5:
        enemyStats = enemySelection(Enemy.frozenPeaksEnemies, Enemy.frozenPeakStats)
    elif x == 6:
        enemyStats = enemySelection(Enemy.lostCavesEnemies, Enemy.lostCaveStats)
    elif x == 7:
        enemyStats = enemySelection(Enemy.burningWastesEnemies, Enemy.burningWastesStats)
    
    initialHealth = enemyStats[0]
    return enemyStats, initialHealth

#Fighting, Buffing, and Running is managed here
def combatSit(initialHealth, enemyStats):
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
        elif action == "r":
            return
    enemyStats[0] = initialHealth
    #If the enemy is dead provide players with xp and roll drops
    if enemyDead:
        xpEarned = Enemy.xpCalc(Player.playerStats.level, enemyStats[3])
        xpRequired = Player.addXp(xpEarned)
        gold = loot(enemyStats[4], enemyStats[5])
        Player.playerStats.inventory["gold"]["amount"] += gold
        print("The enemy dropped " + str(gold) + " gold")
        Player.print_gold()


def pickingDungeon():
    #Prints the list of dungeons you can travel to
    for i in range(0, len(Enemy.dungeons)):
        print(str(i + 1) +  ". " + Enemy.dungeons[i])
        i += 1
    print("Pick a dungeon to fight")
    x = int(input())
    print("This dungeon will contain these enemies:")
    if x == 1:
        enemiesList = Enemy.grasslandEnemies
        enemyStats = Enemy.grasslandStats
        dungeon = Enemy.burrowEnemies
        print(dungeon)
    elif x == 2:
        enemiesList = Enemy.darkForestEnemies
        enemyStats = Enemy.darkForestStats
        dungeon = Enemy.heartEnemies
        print(dungeon)
    elif x == 3:
        enemiesList = Enemy.frozenPeaksEnemies
        enemyStats = Enemy.frozenPeakStats
        dungeon = Enemy.cradleEnemies
        print(dungeon)
    elif x == 4:
        enemiesList = Enemy.lostCavesEnemies
        enemyStats = Enemy.lostCaveStats
        dungeon = Enemy.vaultEnemies
        print(dungeon)
    elif x == 5:
        enemiesList = Enemy.burningWastesEnemies
        enemyStats = Enemy.burningWastesStats
        dungeon = Enemy.infernalEnemies
        print(dungeon)
    
    print("Are you sure you want to enter? (y/n)")
    y = input()

    if y == "y":
        print("You have entered the " + Enemy.dungeons[x - 1])

        print("You have encountered " + str(enemiesList[1]))
        printStats(enemyStats[1])
        combatSit(enemiesList[1][0], enemyStats[1])

        print("You have encountered " + str(enemiesList[2]))
        printStats(enemyStats[2])
        combatSit(enemiesList[2][0], enemyStats[2])

        print("You have encountered " + str(enemiesList[3]))
        printStats(enemyStats[3])
        combatSit(enemiesList[3][0], enemyStats[3])

        print("You have encountered " + str(enemiesList[5]))
        printStats(enemyStats[4])
        combatSit(enemiesList[5][0], enemyStats[5])

        print("You have completed the dungeon")
    else:
        return

def printStats(enemy_stats):
    print(f"Health: {enemy_stats[0]} \nMin Damage: {enemy_stats[1]} \nMax Damage: {enemy_stats[2]}")
    print()
    print("Player (Level " + str(Player.playerStats.level) + ") \nHealth: " + str(Player.playerStats.health) + " \nMin Damage: " + str(Player.playerStats.minimumDamage) + " \nMax Damage: " + str(Player.playerStats.maximumDamage) + "\nDamage Reduction: " + str(Player.playerStats.damageReduction))