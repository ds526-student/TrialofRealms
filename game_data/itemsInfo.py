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

SwordsDict = {
    "Wooden Sword": {
        "minDps": 4,
        "maxDps": 7,
        "levelReq": 1,
        "price": 15,
    },
    "Rusty Iron Sword": {
        "minDps": 7,
        "maxDps": 12,
        "levelReq": 3,
        "price": 50
    },
    "Iron Shortsword": {
        "minDps": 10,
        "maxDps": 15,
        "levelReq": 5,
        "price": 120
    },
    "Steel Cutlass": {
        "minDps": 12,
        "maxDps": 18,
        "levelReq": 7,
        "price": 250
    },
    "Bandit's Saber": {
        "minDps": 15,
        "maxDps": 20,
        "levelReq": 9,
        "price": 400
    },
    "Shadowfang Blade": {
        "minDps": 18,
        "maxDps": 22,
        "levelReq": 11,
        "price": 600
    },
    "Venomous Rapier": {
        "minDps": 20,
        "maxDps": 25,
        "levelReq": 13,
        "price": 800
    },
    "Treant Cleaver": {
        "minDps": 22,
        "maxDps": 28,
        "levelReq": 15,
        "price": 1000
    },
    "Phantom Saber": {
        "minDps": 25,
        "maxDps": 30,
        "levelReq": 17,
        "price": 1400
    },
    "Nightfang Greatsword": {
        "minDps": 28,
        "maxDps": 32,
        "levelReq": 19,
        "price": 1800
    },
    "Frostbite Blade": {
        "minDps": 30,
        "maxDps": 35,
        "levelReq": 21,
        "price": 2500
    },
    "Glacial Edge": {
        "minDps": 32,
        "maxDps": 38,
        "levelReq": 23,
        "price": 3200
    },
    "Avalanche Cleaver": {
        "minDps": 35,
        "maxDps": 40,
        "levelReq": 25,
        "price": 4000
    },
    "Stormbreaker Sword": {
        "minDps": 38,
        "maxDps": 42,
        "levelReq": 27,
        "price": 4800
    },
    "Frozen Fang": {
        "minDps": 40,
        "maxDps": 45,
        "levelReq": 29,
        "price": 5500
    },
    "Stonecrusher Blade": {
        "minDps": 42,
        "maxDps": 48,
        "levelReq": 31,
        "price": 6000
    },
    "Serpent Fang Dagger": {
        "minDps": 45,
        "maxDps": 50,
        "levelReq": 33,
        "price": 6800
    },
    "Phantom Scimitar": {
        "minDps": 48,
        "maxDps": 52,
        "levelReq": 35,
        "price": 7500
    },
    "Explorer's Katana": {
        "minDps": 50,
        "maxDps": 55,
        "levelReq": 37,
        "price": 8500
    },
    "Crystal Cleaver": {
        "minDps": 52,
        "maxDps": 58,
        "levelReq": 39,
        "price": 9200
    },
    "Infernal Saber": {
        "minDps": 55,
        "maxDps": 60,
        "levelReq": 41,
        "price": 10000
    },
    "Molten Edge": {
        "minDps": 58,
        "maxDps": 62,
        "levelReq": 43,
        "price": 11500
    },
    "Blazefang Sword": {
        "minDps": 60,
        "maxDps": 65,
        "levelReq": 45,
        "price": 13000
    },
    "Hellfire Claymore": {
        "minDps": 62,
        "maxDps": 68,
        "levelReq": 47,
        "price": 15000
    },
    "Demon's Wrath": {
        "minDps": 65,
        "maxDps": 70,
        "levelReq": 49,
        "price": 18000
    },
    "Blade of the Verdant Guardian": {
        "minDps": 18,
        "maxDps": 24,
        "levelReq": 10
    },
    "Nightshade Fang": {
        "minDps": 30,
        "maxDps": 36,
        "levelReq": 20
    },
    "Glacier's Bite": {
        "minDps": 45,
        "maxDps": 52,
        "levelReq": 30
    },
    "Crystal Reaver": {
        "minDps": 58,
        "maxDps": 65,
        "levelReq": 40
    },
    "Infernal Judgement": {
        "minDps": 72,
        "maxDps": 80,
        "levelReq": 50
    }
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

ArmourDict = {
    "Cloth Scraps": {
        "dmgRed": 0,
        "levelReq": 0,
        "price": 0
    },
    "Leather Vest": {
        "dmgRed": 3,
        "levelReq": 1,
        "price": 50
    },
    "ChainMail Shirt": {
        "dmgRed": 6,
        "levelReq": 5,
        "price": 200
    },
    "Iron Chestplate": {
        "dmgRed": 9,
        "levelReq": 9,
        "price": 400
    },
    "Shadow Cloak": {
        "dmgRed": 12,
        "levelReq": 11,
        "price": 600
    },
    "Reinforced Hide": {
        "dmgRed": 16,
        "levelReq": 15,
        "price": 1000
    },
    "Darksteel Cloak": {
        "dmgRed": 20,
        "levelReq": 19,
        "price": 1500
    },
    "Frostweave Coat": {
        "dmgRed": 22,
        "levelReq": 21,
        "price": 2500
    },
    "Glacial Plate": {
        "dmgRed": 26,
        "levelReq": 25,
        "price": 4000
    },
    "Avalanche Armour": {
        "dmgRed": 30,
        "levelReq": 29,
        "price": 5500
    },
    "Phantom Robe": {
        "dmgRed": 32,
        "levelReq": 31,
        "price": 6500
    },
    "Runed Plate": {
        "dmgRed": 36,
        "levelReq": 35,
        "price": 8000
    },
    "Crystal Fortress": {
        "dmgRed": 40,
        "levelReq": 39,
        "price": 10000
    },
    "Emberweave Cloak": {
        "dmgRed": 42,
        "levelReq": 41,
        "price": 12000
    },
    "Infernal Shell": {
        "dmgRed": 46,
        "levelReq": 45,
        "price": 15000
    },
    "Hellfire Plate": {
        "dmgRed": 50,
        "levelReq": 49,
        "price": 18000
    },
    "Sentinel's Aegis": {
        "dmgRed": 12,
        "levelReq": 10
    },
    "Wraithbinder Vest": {
        "dmgRed": 18,
        "levelReq": 20
    },
    "Glacier Ward": {
        "dmgRed": 28,
        "levelReq": 30
    },
    "Echoing Plate": {
        "dmgRed": 38,
        "levelReq": 40
    },
    "Molten King's Mantle": {
        "dmgRed": 50,
        "levelReq": 50
    },
}

healthPotions = [
    #Health Potions[amountrecovered][price]
    ["Minor Health Potion", 10, 5], 
    ["Lesser Health Potion", 25, 12], 
    ["Health Potion", 50, 25], 
    ["Greater Health Potion", 75, 40], 
    ["Superior Health Potion", 100, 60]
]

healthDict = {
    "Minor Health Potion": {
        "amount": 10,
        "price": 5
    },
    "Lesser Health Potion": {
        "amount": 25,
        "price": 12
    },
    "Health Potion": {
        "amount": 50,
        "price": 25
    },
    "Greater Health Potion": {
        "amount": 75,
        "price": 40
    },
    "Superior Health Potion": {
        "amount": 100,
        "price": 60
    }
}