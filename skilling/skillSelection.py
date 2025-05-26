import utils
import skilling.woodCutting as woodCutting
import game_data.skillsInfo as skillsInfo
import skilling.fishing as fishing

def skillsSelect():
    print("What skill would you like to train?")
    for i in range(0, len(skillsInfo.skillsList)):
        print(str(i + 1) + ". " + skillsInfo.skillsList[i])
    
    i += 1
    print(str(i + 1) + ". Return")

    x = utils.get_valid_int("Please select a skill: ", 1, len(skillsInfo.skillsList) + 2, return_zero_based=True)

    if x == len(skillsInfo.skillsList) + 1:
        return
    else:
        print("You have selected " + skillsInfo.skillsList[x])

        skillMethodList = [
            woodCutting.treeSelect,
            fishing.areaSelect,
        ]

        skillMethodList[x]()