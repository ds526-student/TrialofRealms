import player
import game_data.enemy as enemy
import game_data.itemsInfo as itemsInfo
import utils
import town.beastiary as beastiary
import worldMap

globalEnemyDict = {}
globalEnemyName = ""

def attack(minDmg, maxDmg, multiplier):
    from random import randrange
    basedmg = randrange(minDmg, maxDmg + 1)
    return basedmg * multiplier

def loot(minCoins, maxCoins):
    from random import randrange
    return randrange(minCoins, maxCoins)  

def criticalHit(critChance):
    from random import randrange
    critHit = randrange(0, 100)
    if critHit <= critChance:
        print("Critical Hit!")
        return player.playerStats.critHitDamage
    else:
        return 1

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
    if x == 0:
        globalEnemyDict = enemy.grasslandBeast
        enemyStats = enemySelection(enemy.grasslandEnemies, enemy.grasslandStats)
    elif x == 1:
        globalEnemyDict = enemy.darkForestBeast
        enemyStats = enemySelection(enemy.darkForestEnemies, enemy.darkForestStats)
    elif x == 2:
        globalEnemyDict = enemy.frozenPeakBeast
        enemyStats = enemySelection(enemy.frozenPeaksEnemies, enemy.frozenPeakStats)
    elif x == 3:
        globalEnemyDict = enemy.lostCaveBeast
        enemyStats = enemySelection(enemy.lostCavesEnemies, enemy.lostCaveStats)
    elif x == 4:
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
            damageMultiplier = criticalHit(player.playerStats.critHitChance)
            enemyDamage = attack(enemyStats[1], enemyStats[2], 1)
            playerDamage = attack(player.playerStats.minimumDamage, player.playerStats.maximumDamage, damageMultiplier)

            enemyDamage = enemyDamage - player.playerStats.damageReduction
            if enemyDamage < 0:
                enemyDamage = 1


            print("You hit the " + str(globalEnemyName) + " for " + str(playerDamage) + " damage")
            
            enemyStats[0] -= playerDamage

            if enemyStats[0] <= 0:
                print("Enemy Health: 0")
                enemyDead = True
            else:
                print("The " + str(globalEnemyName) + " hit you for " + str(enemyDamage) + " damage")
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
        xpEarned = player.xpCalc(player.playerStats.playerLevel, enemyStats[3])
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

    if x == len(enemy.dungeons):
        return

    dungeon_data = [
        (enemy.grasslandStats, enemy.burrowEnemies, enemy.grasslandBeast),
        (enemy.darkForestStats, enemy.heartEnemies, enemy.darkForestBeast),
        (enemy.frozenPeakStats, enemy.cradleEnemies, enemy.frozenPeakBeast),
        (enemy.lostCaveStats, enemy.vaultEnemies, enemy.lostCaveBeast),
        (enemy.burningWastesStats, enemy.infernalEnemies, enemy.burningWastesBeast),
    ]

    if 0 <= x < len(dungeon_data):
        enemyStats, dungeon, globalEnemyDict = dungeon_data[x]

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

    y = utils.confirm("Would you like to enter the dungeon? (y/n): ")

    if y == "y":
        print("You have entered the " + enemy.dungeons[x - 1])

        for i in range(0, len(dungeon)):
            print("You have encountered " + str(dungeon[i]))
            printStats(enemyStats[i + 1])
            globalEnemyName = dungeon[i]
            combatSit(dungeon[i], enemyStats[i + 1].copy())

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
    print("Player (Level " + str(player.playerStats.playerLevel) + ") \nHealth: " + str(player.playerStats.health) + " \nMin Damage: " + str(player.playerStats.minimumDamage) + " \nMax Damage: " + str(player.playerStats.maximumDamage) + "\nDamage Reduction: " + str(player.playerStats.damageReduction))

def pickingCombatArea():
    print("Pick a combat area to fight")
    for i in range(0, len(worldMap.combatAreas)):
        print(str(i + 1) +  ". " + worldMap.combatAreas[i])
        i += 1

    i += 1
    print(str(i) + ". Return")

    x = utils.get_valid_int("Please select a combat area: ", 1, len(worldMap.combatAreas) + 1, return_zero_based=True)

    if x == len(worldMap.combatAreas) - 1:
        pickingDungeon()
    elif x == len(worldMap.combatAreas):
        return
    else:
        print("You have now entered the " + str(worldMap.combatAreas[x]))
        enemyStats, initialHealth = pickingEnemy(x)
        combatSit(initialHealth, enemyStats) 