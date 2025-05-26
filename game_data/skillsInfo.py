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

# axes = [name, levelRequired, damage]
axes = [
    ["Wooden Axe", 1, 1],
    ["Bronze Axe", 15, 2],
    ["Iron Axe", 30, 4],
    ["Steel Axe", 35, 5],
    ["Mithril Axe", 45, 6],
    ["Adamant Axe", 50, 7],
    ["Rune Axe", 60, 8],
    ["Dragon Axe", 75, 10],
    ["Infernal Axe", 90, 12]
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
