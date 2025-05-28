import msvcrt
import math
import string
import random
import utils
import player
import game_data.skillsInfo as skillsInfo
import inventory
import skilling.skillsUtils as skillsUtils

def calcXp(currentXp, xpEarned, treeIndex=None):
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
    print("Press e to cut down another tree, or any key to return")
    if msvcrt.getch().decode("utf-8") == "e":
        woodCutting(treeIndex)
    else:
        return

def xpToNextLevel():
    return math.floor(10 * (player.playerStats.woodCuttingLevel ** 1.4))

def woodCutting(arrayIndex):
    treeName = skillsInfo.trees[arrayIndex][0]
    treeHealth = skillsInfo.trees[arrayIndex][2]
    xp = skillsInfo.trees[arrayIndex][3]
    logType = skillsInfo.trees[arrayIndex][4]

    print("You have selected to cut down a " + treeName)
    while treeHealth > 0:
        randLetter = random.choice(string.ascii_lowercase)
        print("Press " + randLetter + " to cut down the tree")
        while True:
            x = msvcrt.getch()
            if x.decode("utf-8") == randLetter:
                treeHealth -= player.playerStats.axeDamage
                break
            else:
                print("You pressed " + x.decode("utf-8") + " instead of " + randLetter)
                continue
        print()
        

    print("The tree has fallen")
    player.playerStats.inventory[logType]["amount"] += 1
    print(player.playerStats.inventory[logType]["amount"], logType + "s in your inventory")
    calcXp(player.playerStats.woodCuttingXp, xp, arrayIndex)

def equipAxe():
    print("Select an axe to equip")
    inventory.equip_item(
        item_type="axe",
        equipped_attr="axe",
        dict_ref=skillsInfo.axesDict,
        display_fields=["damage"],
        category_name="axes",
        update_stats_fn=lambda item: setattr(player.playerStats, "axeDamage", skillsInfo.axesDict[item]["damage"])
    )

def treeSelect():
    position = skillsUtils.areaSelect(
        method_name=treeSelect,
        initial_message="Select a tree to cut down",
        location_list=skillsInfo.trees,
        item_type="axe",
        item_name="axe",
        error_message="You are not a high enough level to cut down this tree",
        next_method=woodCutting,
        skill_level=player.playerStats.woodCuttingLevel,
        equip_method=equipAxe
    )

    if position is not None:
        woodCutting(position)
    else:
        print("Returning to previous menu.")