import game_data.itemsInfo as itemsInfo

class playerStats:   
    className = ""
    maximumHealth = 100 
    health = 100 
    weapon = "Wooden Sword"
    armour = "Cloth Scraps"
    damageReduction = itemsInfo.armourDict[armour]["dmgRed"]
    # minimumDamage = itemsInfo.weaponsDict[weapon]["minDps"]
    # maximumDamage = itemsInfo.weaponsDict[weapon]["maxDps"]
    minimumDamage = 10000
    maximumDamage = 10001
    critHitChance = 10
    critHitDamage = 1.5
    level = 50
    xp = 0 

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

def print_weapons():
    i = 1
    for item, details in playerStats.inventory.items():
        if details["type"] == "sword":
            if details["amount"] > 0:
                print(f"{i}. {item}(dmg {itemsInfo.weaponsDict[item]['minDps']} -> {itemsInfo.weaponsDict[item]['maxDps']}) Required level {itemsInfo.weaponsDict[item]['levelReq']}: {details['amount']}")
                i += 1

    print(str(i) + ". Cancel")

def print_armor():
    i = 1
    for item, details in playerStats.inventory.items():
        if details["type"] == "armour":
            if details["amount"] > 0:
                print(f"{i}. {item}: {details['amount']}")
                i += 1

    print(str(i) + ". Cancel")

def print_gold():
    print("You have " + str(playerStats.inventory["gold"]["amount"]) + " gold.")

def print_inventory():
    print("Inventory:")
    print("----------")
    print("Weapons:")
    for item, details in playerStats.inventory.items():
        if isinstance(details, list): 
            details = details[0]
        if details["type"] == "sword":
            print(f"{item} | Damage = {details['minDps']}->{details['maxDps']} | level {details['levelReq']}")
    print("----------")
    print("Armour:")
    for item, details in playerStats.inventory.items():
        if isinstance(details, list): 
            details = details[0]
        if details["type"] == "armour":
            print(f"{item}: | Damage Reduction = {details['dmgRed']} | level {details['levelReq']}")
    print("----------")
    if playerStats.className == "Warrior":
        print("Shield:")
        for item, details in playerStats.inventory.items():
            if isinstance(details, list): 
                details = details[0]
            if details["type"] == "shield":
                print(f"{item} | Damage Reduction = {details['dmgRed']} | level {details['levelReq']}")
    elif playerStats.className == "Ranger":
        print("Arrows:")
        for item, details in playerStats.inventory.items():
            if isinstance(details, list): 
                details = details[0]
            if details["type"] == "arrow":
                print(f"{item} | Effect = {details['effect']} | level {details['levelReq']}")
    elif playerStats.className == "Mage":
        print("Tomes:")
        for item, details in playerStats.inventory.items():
            if isinstance(details, list): 
                details = details[0]
            if details["type"] == "tome":
                print(f"{item} | Effect = {details['effect']} | level {details['levelReq']}")
    print("----------")
    print("Consumables:")
    for item, details in playerStats.inventory.items():
        if details["type"] == "consumable" and details["amount"] > 0:
            print(f"{item}({itemsInfo.healthDict[item]['amount']} hp): {details['amount']}")
    print("----------")
    print_gold()


def addXp(xpEarned):
    xpRequired = int(100 * (playerStats.level**1.5))
    playerStats.xp += xpEarned
    print("You earned " + str(playerStats.xp))
    while playerStats.xp >= xpRequired:
        playerStats.xp % xpRequired
        playerStats.level += 1
        print("You Leveled up! You are now level " + str(playerStats.level))
        playerStats.xp -= xpRequired
        xpRequired = int(100 * (playerStats.level**1.5))
        playerStats.health = playerStats.maximumHealth

    print("current experience (" + str(playerStats.xp) + "/" + str(xpRequired) + ")")
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