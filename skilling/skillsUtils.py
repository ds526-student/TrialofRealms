import utils
import player

# method name = the function used to call the area selection
# initial_message = the message to display before the area selection
# location_list = the list of locations to select from
# item_type = the type of item to equip when prompted
# item_name = the name of the item to display in the prompt
# error_message = the message to display if the player is not high enough level
# next_method = the method to call after selecting a location
# skill_level = the current level of the skill
# equip_method = the method to call to equip the item

def areaSelect(method_name, initial_message, location_list, item_type, item_name, error_message, next_method, skill_level, equip_method=None):
    print(initial_message)

    for i in range(len(location_list)):
        print(f"{i + 1}. {location_list[i][0]} (Level required: {location_list[i][1]})")

    if equip_method is None:
        # do not display the option to equip an item
        i += 1
    else:  
        i += 2
        print(f"{i}. Equip a {item_type}")
    i += 1
    print(f"{i}. Return")

    x = utils.get_valid_int(f"Please select a {item_name}: ", 1, len(location_list) + 1, return_zero_based=True)

    
    if x == len(location_list) and equip_method is not None:
        print(equip_method)
        method_name()
    elif x < len(location_list):
        if skill_level < location_list[x][1]:
            print(error_message)
            utils.enter()
            return
        else:
            return x
    else:
        return
