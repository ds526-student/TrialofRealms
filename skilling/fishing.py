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

def areaSelect():
    skillsUtils.areaSelect(
        method_name=areaSelect,
        initial_message="Select a fishing area",
        location_list=skillsInfo.fishingAreas,
        equip_method=equipFishingRod,
        item_type="fishing rod",
        item_name="fishing rod",
        error_message="You are not high enough level to fish here.",
        next_method=fishing
    )