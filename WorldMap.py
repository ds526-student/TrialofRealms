import player

locationsList = [
    "Open Inventory",
    "Town",
    "The Grasslands (Level 1-10)",
    "The Dark Forest (Level 11-20)",
    "The Frozen Peaks (Level 21-30)",
    "The Lost Caves (Level 31-40)",
    "The Burning Wastes (Level 41-50)",
    "Area Dungeons (Level 10-50)"
]

displayLocationsList = [
    "Open Inventory",
    "Town",
    "The Grasslands",
    "The Dark Forest",
    "The Frozen Peaks",
    "The Lost Caves",
    "The Burning Wastes",
    "Area Dungeons"
]

def weaponsDealer():
    if player.playerStats.className == "Warrior":
        return "Sword Smith"
    elif player.playerStats.className == "Ranger":
        return "Fletcher"
    elif player.playerStats.className == "Mage":
        return "Archmage"

def get_town_list():
    return [
        weaponsDealer(),
        "Armourments Dealer",
        "Potion Brewer",
        "Beastiary",
        "Player Stats"
    ]
