import player
import game_data.itemsInfo as itemsInfo
import utils

#Displays all the items within your inventory
def openInventory():
    player.print_inventory()

    x = utils.confirm("Would you like to equip any gear? (y/n) ")
    if x == "y":
        print("weapon, armour or off-hand? (w/a/o)")
        x = input()
        def equip_item(item_type, equipped_attr, dict_ref, display_fields, category_name, update_stats_fn):
            print(f"You currently have {getattr(player.playerStats, equipped_attr)} equipped")
            printList = []
            equipList = []
            i = 0
            for item, details in player.playerStats.inventory.items():
                if isinstance(details, dict) and details.get('type') == item_type:
                    display_str = f"{i + 1} - {item}: " + " ".join(
                        f"{field}: {details.get(field, 'N/A')}" for field in display_fields
                    )
                    printList.append(display_str)
                    equipList.append(item)
                    i += 1

            if len(printList) == 0:
                print("You have no " + category_name + " to equip")
                utils.enter()
                return
            
            print("Which item would you like to equip?")

            for item in printList:
                print(item)

            x = utils.get_valid_int("Please select an item: ", 1, len(printList) + 1, return_zero_based=True)

            item = equipList[x]

            if item is None:
                return

            if dict_ref[item]["levelReq"] > player.playerStats.playerLevel:
                print("You are not a high enough level to equip this item")
            else:
                # Put currently equipped item back into inventory
                player.playerStats.inventory[getattr(player.playerStats, equipped_attr)] = {
                    **dict_ref.get(getattr(player.playerStats, equipped_attr), {}),
                    "type": item_type
                }
                setattr(player.playerStats, equipped_attr, item)
                update_stats_fn(item)
                del player.playerStats.inventory[item]

        if x == "w":
            equip_item(
                item_type="sword",
                equipped_attr="weapon",
                dict_ref=itemsInfo.weaponsDict,
                display_fields=["minDps", "maxDps"],
                category_name="swords",
                update_stats_fn=lambda item: (
                    setattr(player.playerStats, "minimumDamage", itemsInfo.weaponsDict[item]["minDps"]),
                    setattr(player.playerStats, "maximumDamage", itemsInfo.weaponsDict[item]["maxDps"])
                )
            )
        elif x == "a":
            equip_item(
                item_type="armour",
                equipped_attr="armour",
                dict_ref=itemsInfo.armourDict,
                display_fields=["dmgRed"],
                category_name="armour",
                update_stats_fn=lambda item: setattr(
                    player.playerStats,
                    "damageReduction",
                    itemsInfo.armourDict[item]["dmgRed"] + itemsInfo.armourDict[player.playerStats.shield]["dmgRed"]
                )
            )
        elif x == "o":  
            if player.playerStats.className == "Warrior":
                equip_item(
                    item_type="shield",
                    equipped_attr="shield",
                    dict_ref=itemsInfo.armourDict,
                    display_fields=["dmgRed"],
                    category_name="shields",
                    update_stats_fn=lambda item: setattr(
                        player.playerStats,
                        "damageReduction",
                        itemsInfo.armourDict[item]["dmgRed"] + itemsInfo.armourDict[player.playerStats.armour]["dmgRed"]
                    )
                )
            elif player.playerStats.className == "Mage":
                equip_item(
                    item_type="tome",
                    equipped_attr="tome",
                    dict_ref=itemsInfo.weaponsDict,
                    display_fields=["minDps", "maxDps"],
                    category_name="tomes",
                    update_stats_fn=lambda item: (
                        setattr(player.playerStats, "minimumDamage", itemsInfo.weaponsDict[item]["minDps"]),
                        setattr(player.playerStats, "maximumDamage", itemsInfo.weaponsDict[item]["maxDps"])
                    )
                )
            elif player.playerStats.className == "Ranger":
                equip_item(
                    item_type="arrow",
                    equipped_attr="arrow",
                    dict_ref=itemsInfo.weaponsDict,
                    display_fields=["effect"],
                    category_name="arrows",
                    update_stats_fn=lambda item: setattr(player.playerStats, "effect", itemsInfo.weaponsDict[item]["effect"])
                )
        else:
            return