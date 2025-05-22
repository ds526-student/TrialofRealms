import player
import game_data.enemy as enemy
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
        globalEnemyDict = enemy.grasslandBeast
        enemyStats = enemySelection(enemy.grasslandEnemies, enemy.grasslandStats)
    elif x == 4:
        globalEnemyDict = enemy.darkForestBeast
        enemyStats = enemySelection(enemy.darkForestEnemies, enemy.darkForestStats)
    elif x == 5:
        globalEnemyDict = enemy.frozenPeakBeast
        enemyStats = enemySelection(enemy.frozenPeaksEnemies, enemy.frozenPeakStats)
    elif x == 6:
        globalEnemyDict = enemy.lostCaveBeast
        enemyStats = enemySelection(enemy.lostCavesEnemies, enemy.lostCaveStats)
    elif x == 7:
        globalEnemyDict = enemy.burningWastesBeast
        enemyStats = enemySelection(enemy.burningWastesEnemies, enemy.burningWastesStats)
    
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
            playerDamage = attack(player.playerStats.minimumDamage, player.playerStats.maximumDamage)

            enemyStats[0] -= playerDamage

            if enemyStats[0] <= 0:
                print("Enemy Health: 0")
                enemyDead = True
            else:
                player.playerStats.health -= enemyDamage
                #When enemy is dead set enemyDead = true
                print("Player Health: " + str(player.playerStats.health))
                print("Enemy Health: " + str(enemyStats[0]))
        elif action == "b":
            if cooldown > 0:
                print("You cannot use a consumable yet")
                continue
            elif player.playerStats.health == player.playerStats.maximumHealth:
                print("You are already at full health")
                continue
            else:
                player.print_consumables()

                x = int(input()) - 1

                if x == len(itemsInfo.healthPotions):
                    return

                player.playerStats.health += itemsInfo.healthPotions[x][1]
                player.playerStats.inventory[itemsInfo.healthPotions[x][0]]["amount"] -= 1

                if player.playerStats.health > player.playerStats.maximumHealth:
                    player.playerStats.health = player.playerStats.maximumHealth

                print("Player Health: " + str(player.playerStats.health))
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
        xpEarned = player.xpCalc(player.playerStats.level, enemyStats[3])
        xpRequired = player.addXp(xpEarned)
        gold = loot(enemyStats[4], enemyStats[5])
        player.playerStats.inventory["gold"]["amount"] += gold
        print("The enemy dropped " + str(gold) + " gold")
        player.print_gold()
        utils.enter()
        beastiary.beastLogEntry(globalEnemyDict, globalEnemyName)


def pickingDungeon():
    global globalEnemyDict
    global globalEnemyName
    #Prints the list of dungeons you can travel to
    for i in range(0, len(enemy.dungeons)):
        print(str(i + 1) +  ". " + enemy.dungeons[i])
        i += 1

    i += 1
    print(str(i) + ". Return")
    print("Pick a dungeon to fight")
    x = utils.get_valid_int("Please select a dungeon: ", 1, len(enemy.dungeons) + 1, return_zero_based=True)
    print("This dungeon will contain these enemies:")

    # assigns the correct list of weapons and armours based on the players class

    if x == 0:
        enemyStats = enemy.grasslandStats
        dungeon = enemy.burrowEnemies
        globalEnemyDict = enemy.grasslandBeast
    elif x == 1:
        enemyStats = enemy.darkForestStats
        dungeon = enemy.heartEnemies
        globalEnemyDict = enemy.darkForestBeast
    elif x == 2:
        enemyStats = enemy.frozenPeakStats
        dungeon = enemy.cradleEnemies
        globalEnemyDict = enemy.frozenPeakBeast
    elif x == 3:
        enemyStats = enemy.lostCaveStats
        dungeon = enemy.vaultEnemies
        globalEnemyDict = enemy.lostCaveBeast
    elif x == 4:
        enemyStats = enemy.burningWastesStats
        dungeon = enemy.infernalEnemies
        globalEnemyDict = enemy.burningWastesBeast
    elif x == len(enemy.dungeons):
        return

    if player.playerStats.className == "Warrior":
        weaponReward = itemsInfo.dungeonSwords[x][0]   
        armourReward = itemsInfo.dungeonMeleeArmours[x][0]
    elif player.playerStats.className == "Ranger":
        weaponReward = itemsInfo.dungeonRanged[x][0]   
        armourReward = itemsInfo.dungeonRangedArmours[x][0]
    elif player.playerStats.className == "Mage":
        weaponReward = itemsInfo.dungeonMagic[x][0]   
        armourReward = itemsInfo.dungeonMageArmours[x][0]
        print(dungeon)

    y = utils.confirm("Would you like to enter the dungeon? (y/n) ")

    if y == "y":
        print("You have entered the " + enemy.dungeons[x - 1])

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
        player.playerStats.inventory[str(weaponReward)] = {
            **itemsInfo.weaponsDict.get(str(weaponReward), {}),
            "type": "sword"
        }
        
        player.playerStats.inventory[str(armourReward)] = {
            **itemsInfo.armourDict.get(str(armourReward), {}),
            "type": "armour"
        }   
        utils.enter()
    else:
        return

def printStats(enemy_stats):
    print(f"Level: {enemy_stats[3]} \nHealth: {enemy_stats[0]} \nMin Damage: {enemy_stats[1]} \nMax Damage: {enemy_stats[2]}")
    print()
    print("Player (Level " + str(player.playerStats.level) + ") \nHealth: " + str(player.playerStats.health) + " \nMin Damage: " + str(player.playerStats.minimumDamage) + " \nMax Damage: " + str(player.playerStats.maximumDamage) + "\nDamage Reduction: " + str(player.playerStats.damageReduction))