# swords = [name][mindamage][maxdamage][levelrequired][price]
grasslandSwords = [
    #Grasslands swords
    ["Wooden Sword", 4, 7, 1, 15], 
    ["Rusty Iron Sword", 7, 12, 3, 50],  
    ["Iron Shortsword", 10, 15, 5, 120],
    ["Steel Cutlass", 12, 18, 7, 250],  
    ["Bandit's Saber", 15, 20, 9, 400]
]

darkForestSword = [
    #Dark Forest swords
    ["Shadowfang Blade", 18, 22, 11, 600], 
    ["Venomous Rapier", 20, 25, 13, 800], 
    ["Treant Cleaver", 22, 28, 15, 1000], 
    ["Phantom Saber", 25, 30, 17, 1400],
    ["Nightfang Greatesword", 28, 32, 19, 1800]
]

frozenPeakSwords = [
    #Frozen Peaks swords
    ["Frostbite Blade", 30, 35, 21, 2500], 
    ["Glacial Edge", 32, 38, 23, 3200], 
    ["Avalanche Cleaver", 35, 40, 25, 4000], 
    ["Stormbreaker Sword", 38, 42, 27, 4800], 
    ["Frozen Fang", 40, 45, 29, 5500] 
]

lostCaveSwords = [
    #Lost Caves swords
    ["Stonecrusher Blade", 42, 48, 31, 6000], 
    ["Serpent Fang Dagger", 45, 50, 33, 6800], 
    ["Phantom Scimitar", 48, 52, 35, 7500], 
    ["Explorer's Katana", 50, 55, 37, 8500], 
    ["Crystal Cleaver", 52, 58, 39, 9200]
]

burningWasteSwords = [
    #Burning Wastes Swords
    ["Infernal Saber", 55, 60, 41, 10000], 
    ["Molten Edge", 58, 62, 43, 11500], 
    ["Blazefang Sword", 60, 65, 45, 13000],
    ["Hellfire Claymore", 62, 68, 47, 15000], 
    ["Demon's Wrath", 65, 70, 49, 18000]
]

dungeonSwords = [
    #10% chance to regen 5 hp per hit
    ["Blade of the Verdant Guardian", 18, 24, 10, 0],
    #15% chance to inflict poison dealing 5dmg per turn for 3 turns
    ["Nightshade Fang", 30, 36, 20, 0],
    #20% chance to freeze an enemy for 1 turn
    ["Glacier's Bite", 45, 52, 30, 0],
    #10% chance to critical hit dealing double damage
    ["Crystal Reaver", 58, 65, 40, 0],
    #25% chance to ignite an enemy, dealing 10dmg per turn for 3 turns
    ["Infernal Judgement", 72, 80, 50, 0]
]

def makeSword(min_dps, max_dps, level_req, price):
    sword = {
        "minDps": min_dps,
        "maxDps": max_dps,
        "levelReq": level_req,
        "price": price
    }
    return sword

SwordsDict = {
    "Wooden Sword": makeSword(4, 7, 1, 15),
    "Rusty Iron Sword": makeSword(7, 12, 3, 50),
    "Iron Shortsword": makeSword(10, 15, 5, 120),
    "Steel Cutlass": makeSword(12, 18, 7, 250),
    "Bandit's Saber": makeSword(15, 20, 9, 400),
    "Shadowfang Blade": makeSword(18, 22, 11, 600),
    "Venomous Rapier": makeSword(20, 25, 13, 800),
    "Treant Cleaver": makeSword(22, 28, 15, 1000),
    "Phantom Saber": makeSword(25, 30, 17, 1400),
    "Nightfang Greatsword": makeSword(28, 32, 19, 1800),
    "Frostbite Blade": makeSword(30, 35, 21, 2500),
    "Glacial Edge": makeSword(32, 38, 23, 3200),
    "Avalanche Cleaver": makeSword(35, 40, 25, 4000),
    "Stormbreaker Sword": makeSword(38, 42, 27, 4800),
    "Frozen Fang": makeSword(40, 45, 29, 5500),
    "Stonecrusher Blade": makeSword(42, 48, 31, 6000),
    "Serpent Fang Dagger": makeSword(45, 50, 33,6800),
    "Phantom Scimitar": makeSword(48 ,52 ,35 ,7500),
    "Explorer's Katana": makeSword(50 ,55 ,37 ,8500),
    "Crystal Cleaver": makeSword(52 ,58 ,39 ,9200),
    "Infernal Saber": makeSword(55 ,60 ,41 ,10000),
    "Molten Edge": makeSword(58 ,62 ,43 ,11500),
    "Blazefang Sword": makeSword(60 ,65 ,45 ,13000),
    "Hellfire Claymore": makeSword(62 ,68 ,47 ,15000),
    "Demon's Wrath": makeSword(65 ,70 ,49 ,18000),
    "Blade of the Verdant Guardian": makeSword(18, 24, 10, 0),
    "Nightshade Fang": makeSword(30, 36, 20, 0),
    "Glacier's Bite": makeSword(45, 52, 30, 0),
    "Crystal Reaver": makeSword(58, 65, 40, 0),
    "Infernal Judgement": makeSword(72, 80, 50, 0)
}

# armour = [name][damage reduction][levelrequired][price]
grasslandArmour = [
    #Grasslands Armours
    ["Leather Vest", 3, 1, 50], 
    ["ChainMail Shirt", 6, 5, 200],  
    ["Iron Chestplate", 9, 9, 400]
]

darkForestArmour = [
    #Dark Forest Armours
    ["Shadow Cloak", 12, 11, 600], 
    ["Reinforced Hide", 16, 15, 1000],  
    ["Darksteel Cuirass", 20, 19, 1500]
]

frozenPeakArmour = [
    #Frozen Peak Armours
    ["Frostweave Coat", 22, 21, 2500], 
    ["Glacial Plate", 26, 25, 4000],  
    ["Avalanche Armour", 30, 29, 5500]
]

lostCavesArmour = [
    #Lost Caves Armours
    ["Phantom Robe", 32, 31, 6500], 
    ["Runed Plate", 36, 35, 8000],  
    ["Crystal Fortress", 40, 39, 10000]
]

burningWasteArmour = [
    #Burning Wastes Armours
    ["Emberweave Cloak", 42, 41, 12000], 
    ["Infernal Shell", 46, 45, 15000],  
    ["Hellfire Plate", 50, 49, 18000]
]

dungeonArmours = [
    #Dungeon Armours
    ["Sentinel's Aegis", 12, 10, 0], #Guardian Hollow
    ["Wraithbinder Vest", 18, 20, 0], #Shadowfall Grove
    ["Glacier Ward", 28, 30, 0], #Icebound Citadel
    ["Echoing Plate", 38, 40, 0], #Abyssal Tomb
    ["Molten King's Mantle", 50, 50, 0] #Infernal Depths
]

def makeArmour(dmg_red, level_req, price):
    armour = {
        "dmgRed": dmg_red,
        "levelReq": level_req,
        "price": price
    }
    return armour

ArmourDict = {
    "Cloth Scraps": makeArmour(0, 0, 0),
    "Leather Vest": makeArmour(3, 1, 50),
    "ChainMail Shirt": makeArmour(6, 5, 200),
    "Iron Chestplate": makeArmour(9, 9, 400),
    "Shadow Cloak": makeArmour(12, 11, 600),
    "Reinforced Hide": makeArmour(16, 15, 1000),
    "Darksteel Cuirass": makeArmour(20, 19, 1500),
    "Frostweave Coat": makeArmour(22, 21, 2500),
    "Glacial Plate": makeArmour(26, 25, 4000),
    "Avalanche Armour": makeArmour(30, 29, 5500),
    "Phantom Robe": makeArmour(32, 31, 6500),
    "Runed Plate": makeArmour(36, 35, 8000),
    "Crystal Fortress": makeArmour(40, 39, 10000),
    "Emberweave Cloak": makeArmour(42, 41, 12000),
    "Infernal Shell": makeArmour(46, 45, 15000),
    "Hellfire Plate": makeArmour(50, 49, 18000),
    "Sentinel's Aegis": makeArmour(12, 10, 0),
    "Wraithbinder Vest": makeArmour(18, 20, 0),
    "Glacier Ward": makeArmour(28, 30, 0),
    "Echoing Plate": makeArmour(38, 40, 0),
    "Molten King's Mantle": makeArmour(50, 50, 0)
}

healthPotions = [
    #Health Potions[amountrecovered][price]
    ["Minor Health Potion", 10, 5], 
    ["Lesser Health Potion", 25, 12], 
    ["Health Potion", 50, 25], 
    ["Greater Health Potion", 75, 40], 
    ["Superior Health Potion", 100, 60]
]

def makeHealthPotion(amount, price):
    healthPotion = {
        "amount": amount,
        "price": price
    }
    return healthPotion

healthDict = {
    "Minor Health Potion": makeHealthPotion(10, 5),
    "Lesser Health Potion": makeHealthPotion(25, 12),
    "Health Potion": makeHealthPotion(50, 25),
    "Greater Health Potion": makeHealthPotion(75, 40),
    "Superior Health Potion": makeHealthPotion(100, 60)
}