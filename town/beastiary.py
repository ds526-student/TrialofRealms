import worldMap
import utils
import game_data.enemy as enemy

def beastLog():
    print("Welcome to the bestiary! Here you can see all the enemies you have encountered.")
    print("For which area would you like to see the bestiary?")
    for i in range(0, len(worldMap.combatAreas) - 1):
        print(str(i - 1) +  ". " + worldMap.combatAreas[i])
        i += 1

    print(str(i - 1) + ". Return")

    x = utils.get_valid_int("Please select an area: ", 1, len(worldMap.locationsList) + 1, return_zero_based=True)

    print(str(x))
    if x is len(worldMap.locationsList) + 1:
        return
    elif x >= 0 and x < len(worldMap.locationsList) + 1:

        if x is 0:
            dictionary = enemy.grasslandBeast
        elif x is 1:
            dictionary = enemy.darkForestBeast
        elif x is 2:
            dictionary = enemy.frozenPeakBeast
        elif x is 3:
            dictionary = enemy.lostCaveBeast
        elif x is 4:
            dictionary = enemy.burningWastesBeast

        print("Here are the stats for the enemies you have encountered in the " + worldMap.combatAreas[x] + ":")
        print("-------------------------------------------------")
    for item, details in dictionary.items():
        if details.get("kills") > 0:
            print(f"{item} | {details['Level']} level | {details['Health']} hp | {details['minDps']} - {details['maxDps']} dps | {details['kills']} kills")
            
    utils.enter()


def beastLogEntry(dictionary, enemy):
    dictionary[enemy]["kills"] += 1
    