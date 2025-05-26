import utils
import player

def areaSelect(method_name, initial_message, location_list, equip_method, item_type, item_name, error_message, next_method):
    print(initial_message)

    for i in range(len(location_list)):
        print(f"{i + 1}. {location_list[i][0]} (Level required: {location_list[i][1]})")

    i += 2
    print(f"{i}. Equip a {item_type}")
    i += 1
    print(f"{i}. Return")

    x = utils.get_valid_int(f"Please select a {item_name}: ", 1, len(location_list) + 1, return_zero_based=True)

    if x == len(location_list) + 1:
        return None
    elif x == len(location_list):
        print(equip_method)
        method_name()
    else:
        if player.playerStats.woodCuttingLevel < location_list[x][1]:
            print(error_message)
            utils.enter()
            return
        else:
            next_method(location_list[x][0], location_list[x][2], location_list[x][3], location_list[x][4])
