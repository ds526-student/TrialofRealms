import msvcrt
import math
import string
import random
import utils
import player
import game_data.skillsInfo as skillsInfo

def calcXp(currentXp, xpEarned):
    xpNeeded = xpToNextLevel()
    currentXp += xpEarned
    if currentXp >= xpNeeded:
        player.playerStats.woodCuttingLevel += 1
        currentXp -= xpNeeded
        print("You have reached woodcutting level " + str(player.playerStats.woodCuttingLevel) + "!")
        print("You now have " + str(currentXp) + "/" + str(xpToNextLevel()) + " xp towards your next level.")
    else:
        print("You now have " + str(currentXp) + "/" + str(xpNeeded) + " xp towards your next level.")


    player.playerStats.woodCuttingXp = currentXp
    utils.enter()

def xpToNextLevel():
    return math.floor(10 * (player.playerStats.woodCuttingLevel ** 1.4))

def treeSelect():
    print("Select a tree to cut down")

    for i in range(0, len(skillsInfo.trees)):
        print(str(i + 1) + ". " + skillsInfo.trees[i][0] + " (Level required: " + str(skillsInfo.trees[i][1]) + ")")

    i += 1
    print(str(i + 1) + ". Return")

    x = utils.get_valid_int("Please select a tree: ", 1, len(skillsInfo.trees) + 1, return_zero_based=True)

    if x == len(skillsInfo.trees):
        return
    else:
        if player.playerStats.woodCuttingLevel < skillsInfo.trees[x][1]:
            print("You are not a high enough level to cut down this tree")
            utils.enter()
            return
        else:
            woodCutting(skillsInfo.trees[x][0], skillsInfo.trees[x][2], skillsInfo.trees[x][3], skillsInfo.trees[x][4])


def woodCutting(treeName, health, xp, logType):
    print("You have selected to cut down a " + treeName)
    while health > 0:
        randLetter = random.choice(string.ascii_lowercase)
        print("Press " + randLetter + " to cut down the tree")
        while True:
            x = msvcrt.getch()
            if x.decode("utf-8") == randLetter:
                health -= player.playerStats.axeDamage
                break
            else:
                print("You pressed " + x.decode("utf-8") + " instead of " + randLetter)
                continue
        print()
        

    print("The tree has fallen")
    calcXp(player.playerStats.woodCuttingXp, xp)