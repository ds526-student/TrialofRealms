# Timing/Reflex Mechanic:
# Instead of pressing a random letter, show a "bite" event after a random delay. The player must press a key quickly (within a short time window) to catch the fish. If they miss, the fish escapes.

# Multiple Fish Types:
# Each fish could have different bite speeds, XP, and rarity.

# Fishing Rods and Bait:
# Allow equipping different rods and using bait to increase catch chances or access rarer fish.

# Random Events:
# Sometimes, the player might catch junk, nothing, or a rare item.

# Progress Bar or "Tug-of-War":
# For higher-level fish, require the player to press a sequence of keys or alternate keys to "reel in" the fish, simulating a struggle.

# fishing bait
# increases the chance of catching a fish instead of trash

# chance for the line to break
# this depends on the fishing rod and level of the fishing area
import skilling.skillsUtils as skillsUtils
import player
import game_data.skillsInfo as skillsInfo
import utils

def areaSelect():
    position = skillsUtils.areaSelect(
        method_name=areaSelect,
        initial_message="Select a fishing area",
        location_list=skillsInfo.fishingAreas,
        item_type="fishing rod",
        item_name="fishing rod",
        error_message="You are not high enough level to fish here.",
        skill_level=player.playerStats.fishingLevel
    )

    if position is not None:    
        areaName = skillsInfo.fishingAreas[position][0]
        arrayIndex = position
        fishSelect(areaName, arrayIndex)
    else:
        print("You have returned to the previous menu.")



def fishSelect(areaName, arrayIndex):
    print(f"You have selected to fish at {areaName}.")

    j = 1
    for i in range(arrayIndex * 2, arrayIndex * 2 + 2):
        fishName = skillsInfo.fishNameArray[i]
        print(j + fishName)
        j += 1

    j += 1
    print(f"{j}. Return")
    x = utils.get_valid_int("Please select a fish to catch: ", 1, 4, return_zero_based=True)

    if x == 3:
        return
    else:
        fishName = skillsInfo.fishNameArray[arrayIndex * 2 + x - 1]
        minLevel = skillsInfo.fishDict[fishName]["levelReq"]
        if player.playerStats.fishingLevel < minLevel:
            print(f"You are not high enough level to catch {fishName}.")
            utils.enter()
            return
        else:
            catchName = skillsInfo.fishDict[fishName]["catchName"]
            xp = skillsInfo.fishDict[fishName]["exp"]

            minFishingTime = (1 - player.playerStats.fishingRodTimeReduction) * player.playerStats.minFishingTime
            maxFishingTime = (1 - player.playerStats.fishingRodTimeReduction) * player.playerStats.maxFishingTime

            catchFish(fishName, catchName, xp, minFishingTime, maxFishingTime)

def catchFish(fishName, catchName, xp, minFishingTime, maxFishingTime):
    print("HELLO")
        