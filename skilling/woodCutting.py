import msvcrt
import math
import string
import random
import utils
import player

# trees = [treeName, levelRequired, health, exp, logType] 
trees = [
    ["Normal Tree", 1, 5, 10, "Normal Log"],        # 10 exp
    ["Oak Tree", 15, 10, 150, "Oak Log"],            # 150 exp
    ["Willow Tree", 30, 20, 500, "Willow Log"],      # 500 exp
    ["Teak Tree", 35, 25, 800, "Teak Log"],          # 800 exp
    ["Maple Tree", 45, 30, 1200, "Maple Log"],       # 1200 exp
    ["Mahogany Tree", 50, 35, 1750, "Mahogany Log"], # 1750 exp
    ["Yew Tree", 60, 40, 2800, "Yew Log"],           # 2800 exp
    ["Magic Tree", 75, 50, 5000, "Magic Log"],       # 5000 exp
    ["Redwood Tree", 90, 60, 9000, "Redwood Log"]    # 9000 exp
]

def calcXp(currentXp, level):
    xpNeeded = math.floor(10 * (level ** 1.4))
    if currentXp >= xpNeeded:
        totalXp += currentXp
        level += 1
        currentXp -= xpNeeded
        print("You have reached level " + str(level) + "!")
    else:
        totalXp += currentXp
        print("You now have " + str())


def treeSelect():
    print("Select a tree to cut down")

    for i in range(0, len(trees)):
        print(str(i + 1) + ". " + trees[i][0] + " (Level required: " + str(trees[i][1]) + ")")

    i += 1
    print(str(i + 1) + ". Return")

    x = utils.get_valid_int("Please select a tree: ", 1, len(trees) + 1, return_zero_based=True)

    if x == len(trees):
        return
    else:
        if player.playerStats.woodCuttingLevel < trees[x][1]:
            print("You are not a high enough level to cut down this tree")
            utils.enter()
            return
        else:
            woodCutting(trees[x][0], trees[x][2], trees[x][3], trees[x][4])


def woodCutting(treeName, health, exp, logType):
    print("You have selected to cut down a " + treeName)
    for i in range(0, health):
        randLetter = random.choice(string.ascii_lowercase)
        print("Press " + randLetter + " to cut down the tree")
        while True:
            x = msvcrt.getch()
            if x.decode("utf-8") == randLetter:
                break
            else:
                print("You pressed " + x.decode("utf-8") + " instead of " + randLetter)
                continue
        print()
        

    print("The tree has fallen")