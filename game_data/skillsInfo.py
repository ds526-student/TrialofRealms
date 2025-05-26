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

# trees = [treeName, levelRequired, health, exp, logType] 
trees = [
    ["Normal Tree", 1, 5, 10, "Normal Log"],         # 10 exp
    ["Oak Tree", 15, 10, 150, "Oak Log"],            # 150 exp
    ["Willow Tree", 30, 20, 500, "Willow Log"],      # 500 exp
    ["Teak Tree", 35, 25, 800, "Teak Log"],          # 800 exp
    ["Maple Tree", 45, 30, 1200, "Maple Log"],       # 1200 exp
    ["Mahogany Tree", 50, 35, 1750, "Mahogany Log"], # 1750 exp
    ["Yew Tree", 60, 40, 2800, "Yew Log"],           # 2800 exp
    ["Magic Tree", 75, 50, 5000, "Magic Log"],       # 5000 exp
    ["Redwood Tree", 90, 60, 9000, "Redwood Log"]    # 9000 exp
]

# creates an axe object
def makeAxe(level_required, damage, type="axe"):
    return {
        "levelReq": level_required,
        "damage": damage,
        "type": type
    }   

# a dictionary of axes
axesDict = {
    "Wooden Axe": makeAxe(1, 1),
    "Bronze Axe": makeAxe(15, 2),
    "Iron Axe": makeAxe(30, 4),
    "Steel Axe": makeAxe(35, 5),
    "Mithril Axe": makeAxe(45, 6),
    "Adamant Axe": makeAxe(50, 7),
    "Rune Axe": makeAxe(60, 8),
    "Dragon Axe": makeAxe(75, 10),
    "Infernal Axe": makeAxe(90, 12)
}






# fishing areas = [areaName, levelRequired, fishChance]
fishingAreas = [
    ["Shallow Shores", 1, 75],          
    ["Shrapnel River", 15, 80],     
    ["Trench of Despair", 30, 70],
    ["Lemvor Pier", 45, 70],
    ["Open Waters", 60, 85],
    ["Barren Ocean", 75, 90]
]

# creates a fish object
def makeFish(level_required, exp, catch_name):
    return {
        "levelReq": level_required,
        "exp": exp,
        "catchName": catch_name
    }

# a dictionary of fish
fishDict = {
    "Shrimp": makeFish(1, 5, "Raw Shrimp"),
    "Sardine": makeFish(5, 15, "Raw Sardine"),
    "Herring": makeFish(10, 25, "Raw Herring"),
    "Trout": makeFish(20, 50, "Raw Trout"),
    "Salmon": makeFish(30, 75, "Raw Salmon"),
    "Tuna": makeFish(35, 100, "Raw Tuna"),
    "Swordfish": makeFish(45, 150, "Raw Swordfish"),
    "Lobster": makeFish(50, 200, "Raw Lobster"),
    "Cavefish": makeFish(62, 300, "Raw Cavefish"),
    "Shark": makeFish(76, 500, "Raw Shark"),
    "Manta Ray": makeFish(90, 750, "Raw Manta Ray"),
    "Whale": makeFish(99, 1000, "Raw Whale")
}

# creates a fishingRod object
def makeFishingRod(level_required, price, time_reduction, type="fishing rod"):
    return {
        "levelReq": level_required,
        "price": price,
        "timeReduction": time_reduction,
        "type": type
    }

# a dictionary of fishing rods
fishingRodDict = {
    "Iron Fishing Rod": makeFishingRod(1, 100, 0),
    "Steel Fishing Rod": makeFishingRod(15, 500, 10),
    "Black Fishing Rod": makeFishingRod(30, 1000, 15),
    "Mithril Fishing Rod": makeFishingRod(45, 1500, 20),
    "Adamant Fishing Rod": makeFishingRod(60, 2500, 25),
    "Rune Fishing Rod": makeFishingRod(75, 5000, 30),
    "Dragon Fishing Rod": makeFishingRod(90, 10000, 40),
}