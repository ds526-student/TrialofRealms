import game_data.itemsInfo as itemsInfo

class playerStats:   
    className = ""
    maximumHealth = 100 
    health = 100 
    weapon = "Wooden Sword"
    armour = "Cloth Scraps"
    shield = "Broken Shield"
    tome = "Old Leather Tome"
    arrow = "Wooden Arrow"
    damageReduction = itemsInfo.armourDict[armour]["dmgRed"] + itemsInfo.armourDict[shield]["dmgRed"]
    minimumDamage = itemsInfo.weaponsDict[weapon]["minDps"]
    maximumDamage = itemsInfo.weaponsDict[weapon]["maxDps"]
    # minimumDamage = 10000
    # maximumDamage = 10001


    critHitChance = 10
    critHitDamage = 1.5


    playerLevel = 50
    playerXp = 0 

    woodCuttingLevel = 1
    woodCuttingXp = 0


    maxLevel = 99

    inventory = {
        "gold": {
            "amount": 100000000,
            "type" : "loot"
        },
        "Minor Health Potion": {
            "amount": 10,
            "type" : "consumable"
        },
        "Lesser Health Potion": {
            "amount": 0,
            "type" : "consumable"
        },
        "Health Potion": {
            "amount": 0,
            "type" : "consumable"
        },
        "Greater Health Potion": {
            "amount": 0,
            "type" : "consumable"
        },
        "Superior Health Potion": {
            "amount": 0,
            "type" : "consumable"
        }
    }
    
def print_consumables():
    i = 1
    for item, details in playerStats.inventory.items():
        if details["type"] == "consumable":
            if details['amount'] > 0:
                print(f"{i}. {item}({itemsInfo.healthDict[item]['amount']} hp): {details['amount']}")    
                i += 1

    print(str(i) + ". Cancel")

def print_gold():
    print("You have " + str(playerStats.inventory["gold"]["amount"]) + " gold.")

def print_inventory():
    print("Inventory:")
    print("----------")
    def print_category(category_name, item_type, extra_fields=None):
        print(f"{category_name}:")
        for item, details in playerStats.inventory.items():
            if isinstance(details, list):
                details = details[0]
            if details["type"] == item_type:
                extra = ""
                if extra_fields:
                    extra = " | " + " | ".join(f"{field.capitalize()} = {details[field]}" for field in extra_fields)
                print(f"{item}{extra}")
        print("----------")

    print_category("Weapons", "sword", ["minDps", "maxDps", "levelReq"])
    print_category("Armour", "armour", ["dmgRed", "levelReq"])

    if playerStats.className == "Warrior":
        print_category("Shield", "shield", ["dmgRed", "levelReq"])

    elif playerStats.className == "Ranger":
        print_category("Arrows", "arrow", ["effect", "levelReq"])

    elif playerStats.className == "Mage":
        print_category("Tomes", "tome", ["effect", "levelReq"])

    print("----------")
    print("Consumables:")
    for item, details in playerStats.inventory.items():
        if details["type"] == "consumable" and details["amount"] > 0:
            print(f"{item}({itemsInfo.healthDict[item]['amount']} hp): {details['amount']}")
    print("----------")
    print_gold()


def addXp(xpEarned):
    if playerStats.playerLevel >= playerStats.maxLevel:
        return
    elif playerStats.playerLevel < playerStats.maxLevel:
        xpRequired = int(100 * (playerStats.playerLevel**1.5))
        playerStats.playerXp += xpEarned
        print("You earned " + str(playerStats.playerXp))
        while playerStats.playerXp >= xpRequired:
            playerStats.playerXp % xpRequired
            playerStats.playerLevel += 1
            print("You Leveled up! You are now level " + str(playerStats.playerLevel))
            playerStats.playerXp -= xpRequired
            xpRequired = int(100 * (playerStats.playerLevel**1.5))
            playerStats.health = playerStats.maximumHealth

    print("current experience (" + str(playerStats.playerXp) + "/" + str(xpRequired) + ")")
    return xpRequired

def xpCalc(pLevel, eLevel):
    baseXp = 50 * (eLevel**1.2) 

    levelDiff = eLevel - pLevel
    if levelDiff >= 3:
        xpMulti = 1 + ((levelDiff - 2) * 0.25)
        if xpMulti > 2:
            xpMulti = 2
    elif levelDiff <= -3:
        xpMulti = max(0.1, 1 - (abs(levelDiff) - 2) * 0.25)
    else:
        xpMulti = 1

    xpEarned = int(baseXp * xpMulti)    
    return xpEarned