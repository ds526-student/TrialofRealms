import player
import game_data.itemsInfo as itemsInfo
import utils

#Displays all the items within your inventory
def openInventory():
    player.print_inventory()

    x = utils.confirm("Would you like to equip any gear? (y/n) ")
    equipmentList = []
    i = 0
    if x == "y":
        print("weapon, armour or off-hand? (w/a/o)")
        x = input()
        if x == "w":
            print("You currently have " + player.playerStats.weapon + " equipped")
            swordList = []  
            for item, details in player.playerStats.inventory.items():
                if isinstance(details, list) and details[0].get('type') == 'sword':
                    swordList.append(f"{i} - {item}: Min DPS: {details[0].get('minDps', 'N/A')} Max DPS: {details[0].get('maxDps', 'N/A')}")
                elif isinstance(details, dict) and details.get('type') == 'sword':
                    swordList.append(f"{i} - {item}: Min DPS: {details.get('minDps', 'N/A')} Max DPS: {details.get('maxDps', 'N/A')}")
                i += 1  
                equipmentList.append(item)
                if len(swordList) == 0:
                    print("You have no swords in your inventory")
                    print("Press enter to continue")
                    input()
                    return
            print("Which item would you like to equip?")
            player.playerStats.inventory[player.playerStats.weapon] = {
                **itemsInfo.SwordsDict.get(player.playerStats.weapon, {}),
                "type": "sword"
            }

            x = utils.get_valid_int("Please select an item: ", 1, len(swordList) + 1, return_zero_based=True)

            item = equipmentList[x]
            if itemsInfo.SwordsDict[item]["levelReq"] > player.playerStats.level:
                print("You are not a high enough level to equip this item")
            else:
                player.playerStats.weapon = equipmentList[x]
                player.playerStats.minimumDamage = itemsInfo.SwordsDict[equipmentList[x]]["minDps"]
                player.playerStats.maximumDamage = itemsInfo.SwordsDict[equipmentList[x]]["maxDps"]
            
        elif x == "a":
            print("You currently have " + player.playerStats.armour + " equipped")
            armourList = []
            equipmentList = []
            i = 0
            for item, details in player.playerStats.inventory.items():
                if isinstance(details, dict) and details.get('type') == 'armour':
                    armourList.append(f"{i} - {item}: Damage Reduction: {details.get('dmgRed', 'N/A')}")
                    equipmentList.append(item)
                    i += 1
            if len(armourList) == 0:
                print("You have no armour in your inventory")
                utils.enter()
                return
            print("Which item would you like to equip?")

            x = utils.get_valid_int("Please select an item: ", 1, len(armourList) + 1, return_zero_based=True)

            item = equipmentList[x]
            if itemsInfo.meleeArmourDict[item]["levelReq"] > player.playerStats.level:
                print("You are not a high enough level to equip this item")
            else:
                player.playerStats.armour = item
                player.playerStats.damageReduction = itemsInfo.armourDict[item]["dmgRed"]
        elif x == "o":  
            if player.playerStats.className == "Warrior":
                warriorOffhand()
        else:
            return
    equipmentList.clear()
    i = 0

def warriorOffhand():
    if player.playerStats.shield == "placeholder":
        print("You currently have no shield equipped")
    else:
        print("You currently have " + player.playerStats.shield + " equipped")

    shieldList = []
    equipmentList = []
    i = 0

    for item, details in player.playerStats.inventory.items():
        print(item)
        print(details)
        print(details.get('type'))
        if details.get('type') == 'shield':
            print("Found a shield in list")
            shieldList.append(f"{i} - {item}: Damage Reduction: {details.get('dmgRed', 'N/A')}")
            i += 1  
            equipmentList.append(item)
    if len(shieldList) == 0:
        print("You have no shields in your inventory")
        utils.enter()
        return
    print("Which item would you like to equip?")
    player.playerStats.inventory[player.playerStats.shield] = {
        **itemsInfo.armourDict.get(player.playerStats.shield, {}),
        "type": "shield"
    }

    x = utils.get_valid_int("Please select an item: ", 1, len(shieldList) + 1, return_zero_based=True)

    item = equipmentList[x]
    if itemsInfo.armourDict[item]["levelReq"] > player.playerStats.level:
        print("You are not a high enough level to equip this item")
    else:
        player.playerStats.shield = equipmentList[x]
        equippedArmour = player.playerStats.armour
        player.playerStats.damageReduction = itemsInfo.armourDict[item]["dmgRed"] + itemsInfo.armourDict[equippedArmour]["dmgRed"]