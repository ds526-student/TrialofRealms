import utils
import skilling.woodCutting as woodCutting

skillsList = [
    "Woodcutting",
    "Fishing",
    "Cooking",
    "Mining",
    "Smithing",
    "Thieving",
    "Fletching",
    "Crafting",
    "Runecrafting",
    "Herblore",
    "Agility",
    "Astrology"
]

def skillsSelect():
    print("What skill would you like to train?")
    for i in range(0, len(skillsList)):
        print(str(i + 1) + ". " + skillsList[i])
    
    i += 1
    print(str(i + 1) + ". Return")

    x = utils.get_valid_int("Please select a skill: ", 1, len(skillsList) + 2, return_zero_based=True)

    if x == len(skillsList) + 1:
        return
    else:
        print("You have selected " + skillsList[x - 1])
        print("You are now training " + skillsList[x - 1])

        skillMethodList = [
            woodCutting.woodCutting,
        ]

        skillMethodList[x - 1]()