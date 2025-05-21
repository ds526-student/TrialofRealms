import WorldMap
import utils
import game_data.Enemy as Enemy

def beastLog():
    print("Welcome to the bestiary! Here you can see all the enemies you have encountered.")
    print("For which area would you like to see the bestiary?")
    for i in range(2, len(WorldMap.displayLocationsList) - 1):
        print(str(i - 1) +  ". " + WorldMap.displayLocationsList[i])
        i += 1

    print(str(i - 1) + ". Return")

    x = utils.get_valid_int("Please select an area: ", 1, len(WorldMap.locationsList) + 1, return_zero_based=True)

    print(str(x))
    if x is len(WorldMap.locationsList) + 1:
        return
    elif x >= 0 and x < len(WorldMap.locationsList) + 1:

        if x is 0:
            dictionary = Enemy.grasslandBeast
        elif x is 1:
            dictionary = Enemy.darkForestBeast
        elif x is 2:
            dictionary = Enemy.frozenPeakBeast
        elif x is 3:
            dictionary = Enemy.lostCaveBeast
        elif x is 4:
            dictionary = Enemy.burningWastesBeast

        print("Here are the stats for the enemies you have encountered in the " + WorldMap.displayLocationsList[x + 2] + ":")
        print("-------------------------------------------------")
    for item, details in dictionary.items():
        if details.get("kills") > 0:
            print(f"{item} | {details['Level']} level | {details['Health']} hp | {details['minDps']} - {details['maxDps']} dps | {details['kills']} kills")
            
    utils.enter()


def beastLogEntry(dictionary, enemy):
    dictionary[enemy]["kills"] += 1
    