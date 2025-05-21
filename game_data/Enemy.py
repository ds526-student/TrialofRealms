#enemyStats[health][minimumDamage][maximumDamage][EnemyLevel][minCoins][maxCoins][maxspecdrop]
grasslandStats = [
    #Grass Lands
    [15, 3, 9, 1, 8, 18],  # Wild Boar (Level 1)
    [25, 7, 12, 3, 12, 25],  # Stray Wolf (Level 3)
    [40, 10, 15, 5, 18, 35],  # Giant Hornet (Level 5)
    [75, 12, 18, 7, 25, 50],  # Goblin Scout (Level 7)
    [100, 15, 20, 9, 35, 70],  # Bandit Ruffian (Level 9)
    [150, 20, 30, 10, 100, 150],  # Ravaging Boar King (Level 10)
]

darkForestStats = [
    #Dark Forest
    [150, 18, 22, 11, 45, 90],  # Shadow Stalker (Level 11)
    [175, 20, 25, 13, 55, 110],  # Venomfang Spider (Level 13)
    [200, 22, 28, 15, 70, 130],  # Cursed Treant (Level 15)
    [225, 25, 30, 17, 85, 160],  # Wraith of the Woods (Level 17)
    [250, 28, 32, 19, 100, 200],  # Nightfang Wolf (Level 19)
    [350, 35, 50, 20, 150, 300], # Hallowborn Ent (Level 20)
]

frozenPeakStats = [
    #Frozen Peaks
    [275, 30, 35, 21, 120, 250],  # Frostbite Bear (Level 21)
    [300, 32, 38, 23, 140, 280],  # Ice Golem (Level 23)
    [325, 35, 40, 25, 160, 320],  # Snow Harpy (Level 25)
    [350, 38, 42, 27, 180, 370],  # Avalanche Beast (Level 27)
    [375, 40, 45, 29, 200, 420],  # Frost Wraith (Level 29)
    [600, 50, 70, 30, 300, 600], # Stormbound Titan (Level 30)
]

lostCaveStats = [
    #Lost Caves
    [400, 42, 48, 31, 250, 500],  # Cave Dweller (Level 31)
    [425, 45, 50, 33, 280, 550],  # Stone Serpent (Level 33)
    [450, 48, 52, 35, 320, 600],  # Phantom Miner (Level 35)
    [475, 50, 55, 37, 350, 650],  # Undead Explorer (Level 37)
    [500, 52, 58, 39, 400, 700],  # Crystal Guardian (Level 39)
    [850, 70, 95, 40, 500, 1000], # Echoing Warden (Level 40)
]

burningWastesStats = [
    #Burning Wastes
    [525, 55, 60, 41, 450, 900],  # Ashen Revenant (Level 41)
    [550, 58, 62, 43, 500, 1000],  # Flame Wyrm (Level 43)
    [575, 60, 65, 45, 600, 1200],  # Magma Golem (Level 45)
    [600, 62, 68, 47, 700, 1400],  # Infernal Hound (Level 47)
    [625, 65, 70, 49, 800, 1600],   # Blazing Demon (Level 49)
    [1150, 90, 120, 50, 1000, 2000], # Pyre Lord Azgarn (Level 50)
]

grasslandEnemies = [
    "Wild Boar",
    "Stray Wolf",
    "Giant Hornet",
    "Goblin Scout",
    "Bandit Ruffian"
]

darkForestEnemies = [
    "Shadow Stalker",
    "Venomfang Spider",
    "Cursed Treant",
    "Wraith of the Woods",
    "Nightfang Wolf"
]

frozenPeaksEnemies = [
    "Frostbite Bear",
    "Ice Golem",
    "Snow Harpy",
    "Avalanche Beast",
    "Frost Wraith"
]

lostCavesEnemies = [
    "Cave Dweller",
    "Stone Serpent",
    "Phantom Miner",
    "Undead Explorer",
    "Crystal Guardian"
]

burningWastesEnemies = [
    "Ashen Revenant",
    "Flame Wyrm",
    "Magma Golem",
    "Infernal Hound",
    "Blazing Demon"
]

dungeons =[
    "Burrow of the Ravager (Level 10)",
    "Heart of the Hallow (Level 20)",
    "Cradle of Stormbound (Level 30)",
    "Vault of Forgotten Echoes (Level 40)",
    "Infernal Abyss (Level 50)"
]

burrowEnemies = [
    grasslandEnemies[1],
    grasslandEnemies[2],
    grasslandEnemies[3],
    "Ravaging Boar King (Level " + str(grasslandStats[5][3]) + ")"
]

heartEnemies = [
    darkForestEnemies[1],
    darkForestEnemies[2],
    darkForestEnemies[3],
    "Hallowborn Ent (Level " + str(darkForestStats[5][3]) + ")"
]

cradleEnemies = [
    frozenPeaksEnemies[1],
    frozenPeaksEnemies[2],
    frozenPeaksEnemies[3],
    "Stormbound Titan (Level " + str(frozenPeakStats[5][3]) + ")"
]

vaultEnemies = [
    lostCavesEnemies[1],
    lostCavesEnemies[2],
    lostCavesEnemies[3],
    "Echoing Warden (Level " + str(lostCaveStats[5][3]) + ")"
]

infernalEnemies = [
    burningWastesEnemies[1],
    burningWastesEnemies[2],
    burningWastesEnemies[3],
    "Pyre Lord Azgarn (Level " + str(burningWastesStats[5][3]) + ")"
]

def makeEnemy(level, health, min_dps, max_dps, min_coins=None, max_coins=None):
    enemy = {
        "Level": level,
        "Health": health,
        "minDps": min_dps,
        "maxDps": max_dps,
        "kills": 0,
    }
    if min_coins is not None:
        enemy["minCoins"] = min_coins
    if max_coins is not None:
        enemy["maxCoins"] = max_coins
    return enemy

grasslandBeast = {
    "Wild Boar": makeEnemy(1, 15, 3, 9, 1, 8),
    "Stray Wolf": makeEnemy(3, 25, 7, 12, 3, 12),
    "Giant Hornet": makeEnemy(5, 40, 10, 15),
    "Goblin Scout": makeEnemy(7, 75, 12, 18),
    "Bandit Ruffian": makeEnemy(9, 100, 15, 20),
    "Ravaging Boar King": makeEnemy(10, 150, 20, 30, 10, 100)
}

darkForestBeast = {
    "Shadow Stalker": makeEnemy(11, 150, 18, 22),
    "Venomfang Spider": makeEnemy(13, 175, 20, 25),
    "Cursed Treant": makeEnemy(15, 200, 22, 28),
    "Wraith of the Woods": makeEnemy(17, 225, 25, 30),
    "Nightfang Wolf": makeEnemy(19, 250, 28, 32),
    "Hallowborn Ent": makeEnemy(20, 350, 35, 50)
}

frozenPeakBeast = {
    "Frostbite Bear": makeEnemy(21, 275, 30, 35),
    "Ice Golem": makeEnemy(23, 300, 32, 38),
    "Snow Harpy": makeEnemy(25, 325, 35, 40),
    "Avalanche Beast": makeEnemy(27, 350, 38, 42),
    "Frost Wraith": makeEnemy(29, 375, 40, 45),
    "Stormbound Titan": makeEnemy(30, 600, 50, 70)
}

lostCaveBeast = {
    "Cave Dweller": makeEnemy(31, 400, 42, 48),
    "Stone Serpent": makeEnemy(33, 425, 45, 50),
    "Phantom Miner": makeEnemy(35, 450, 48, 52),
    "Undead Explorer": makeEnemy(37, 475, 50, 55),
    "Crystal Guardian": makeEnemy(39, 500, 52, 58),
    "Echoing Warden": makeEnemy(40, 850, 70, 95)
}

burningWastesBeast = {
    "Ashen Revenant": makeEnemy(41, 525, 55, 60),
    "Flame Wyrm": makeEnemy(43, 550, 58, 62),
    "Magma Golem": makeEnemy(45, 575, 60, 65),
    "Infernal Hound": makeEnemy(47, 600, 62, 68),
    "Blazing Demon": makeEnemy(49, 625, 65, 70),
    "Pyre Lord Azgarn": makeEnemy(50, 1150, 90, 120)
}
