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
    grasslandSwords[0][0]: {
        "minDps": grasslandSwords[0][1],
        "maxDps": grasslandSwords[0][2],
        "levelReq": grasslandSwords[0][3],
        "price": grasslandSwords[0][4],
    },
    grasslandSwords[1][0]: {
        "minDps": grasslandSwords[1][1],
        "maxDps": grasslandSwords[1][2],
        "levelReq": grasslandSwords[1][3],
        "price": grasslandSwords[1][4]
    },
    grasslandSwords[2][0]: {
        "minDps": grasslandSwords[2][1],
        "maxDps": grasslandSwords[2][2],
        "levelReq": grasslandSwords[2][3],
        "price": grasslandSwords[2][4]
    },
    grasslandSwords[3][0]: {
        "minDps": grasslandSwords[3][1],
        "maxDps": grasslandSwords[3][2],
        "levelReq": grasslandSwords[3][3],
        "price": grasslandSwords[3][4]
    },
    grasslandSwords[4][0]: {
        "minDps": grasslandSwords[4][1],
        "maxDps": grasslandSwords[4][2],
        "levelReq": grasslandSwords[4][3],
        "price": grasslandSwords[4][4]
    },
    darkForestSword[0][0]: {
        "minDps": darkForestSword[0][1],
        "maxDps": darkForestSword[0][2],
        "levelReq": darkForestSword[0][3],
        "price": darkForestSword[0][4]
    },
    darkForestSword[1][0]: {
        "minDps": darkForestSword[1][1],
        "maxDps": darkForestSword[1][2],
        "levelReq": darkForestSword[1][3],
        "price": darkForestSword[1][4]
    },
    darkForestSword[2][0]: {
        "minDps": darkForestSword[2][1],
        "maxDps": darkForestSword[2][2],
        "levelReq": darkForestSword[2][3],
        "price": darkForestSword[2][3]
    },
    darkForestSword[3][0]: {
        "minDps": darkForestSword[3][1],
        "maxDps": darkForestSword[3][2],
        "levelReq": darkForestSword[3][3],
        "price": darkForestSword[3][4]
    },
    darkForestSword[4][0]: {
        "minDps": darkForestSword[4][1],
        "maxDps": darkForestSword[4][2],
        "levelReq": darkForestSword[4][3],
        "price": darkForestSword[4][4]
    },
    frozenPeakSwords[0][0]: {
        "minDps": frozenPeakSwords[0][1],
        "maxDps": frozenPeakSwords[0][2],
        "levelReq": frozenPeakSwords[0][3],
        "price": frozenPeakSwords[0][4]
    },
    frozenPeakSwords[1][0]: {
        "minDps": frozenPeakSwords[1][1],
        "maxDps": frozenPeakSwords[1][2],
        "levelReq": frozenPeakSwords[1][3],
        "price": frozenPeakSwords[1][4]
    },
    frozenPeakSwords[2][0]: {
        "minDps": frozenPeakSwords[2][1],
        "maxDps": frozenPeakSwords[2][2],
        "levelReq": frozenPeakSwords[2][3],
        "price": frozenPeakSwords[2][4]
    },
    frozenPeakSwords[3][0]: {
        "minDps": frozenPeakSwords[3][1],
        "maxDps": frozenPeakSwords[3][2],
        "levelReq": frozenPeakSwords[3][3],
        "price": frozenPeakSwords[3][4]
    },
    frozenPeakSwords[4][0]: {
        "minDps": frozenPeakSwords[4][1],
        "maxDps": frozenPeakSwords[4][2],
        "levelReq": frozenPeakSwords[4][3],
        "price": frozenPeakSwords[4][4]
    },
    lostCaveSwords[0][0]: {
        "minDps": lostCaveSwords[0][1],
        "maxDps": lostCaveSwords[0][2],
        "levelReq": lostCaveSwords[0][3],
        "price": lostCaveSwords[0][4]
    },
    lostCaveSwords[1][0]: {
        "minDps": lostCaveSwords[1][1],
        "maxDps": lostCaveSwords[1][2],
        "levelReq": lostCaveSwords[1][3],
        "price": lostCaveSwords[1][4]
    },
    lostCaveSwords[2][0]: {
        "minDps": lostCaveSwords[2][1],
        "maxDps": lostCaveSwords[2][2],
        "levelReq": lostCaveSwords[2][3],
        "price": lostCaveSwords[2][4]
    },
    lostCaveSwords[3][0]: {
        "minDps": lostCaveSwords[3][1],
        "maxDps": lostCaveSwords[3][2],
        "levelReq": lostCaveSwords[3][3],
        "price": lostCaveSwords[3][4]
    },
    lostCaveSwords[4][0]: {
        "minDps": lostCaveSwords[4][1],
        "maxDps": lostCaveSwords[4][2],
        "levelReq": lostCaveSwords[4][3],
        "price": lostCaveSwords[4][4]
    },
    burningWasteSwords[0][0]: {
        "minDps": burningWasteSwords[0][1],
        "maxDps": burningWasteSwords[0][2],
        "levelReq": burningWasteSwords[0][3],
        "price": burningWasteSwords[0][4]
    },
    burningWasteSwords[1][0]: {
        "minDps": burningWasteSwords[1][1],
        "maxDps": burningWasteSwords[1][2],
        "levelReq": burningWasteSwords[1][3],
        "price": burningWasteSwords[1][4]
    },
    burningWasteSwords[2][0]: {
        "minDps": burningWasteSwords[2][1],
        "maxDps": burningWasteSwords[2][2],
        "levelReq": burningWasteSwords[2][3],
        "price": burningWasteSwords[2][4]
    },
    burningWasteSwords[3][0]: {
        "minDps": burningWasteSwords[3][1],
        "maxDps": burningWasteSwords[3][2],
        "levelReq": burningWasteSwords[3][3],
        "price": burningWasteSwords[3][4]
    },
    burningWasteSwords[4][0]: {
        "minDps": burningWasteSwords[4][1],
        "maxDps": burningWasteSwords[4][2],
        "levelReq": burningWasteSwords[4][3],
        "price": burningWasteSwords[4][4]
    },
    dungeonSwords[0][0]: {
        "minDps": dungeonSwords[0][1],
        "maxDps": dungeonSwords[0][2],
        "levelReq": dungeonSwords[0][3]
    },
    dungeonSwords[1][0]: {
        "minDps": dungeonSwords[1][1],
        "maxDps": dungeonSwords[1][2],
        "levelReq": dungeonSwords[1][3]
    },
    dungeonSwords[2][0]: {
        "minDps": dungeonSwords[2][1],
        "maxDps": dungeonSwords[2][2],
        "levelReq": dungeonSwords[2][3]
    },
    dungeonSwords[3][0]: {
        "minDps": dungeonSwords[3][1],
        "maxDps": dungeonSwords[3][2],
        "levelReq": dungeonSwords[3][3]
    },
    dungeonSwords[4][0]: {
        "minDps": dungeonSwords[4][1],
        "maxDps": dungeonSwords[4][2],
        "levelReq": dungeonSwords[4][3]
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
    grasslandArmour[0][0]: {
        "dmgRed": grasslandArmour[0][1],
        "levelReq": grasslandArmour[0][2],
        "price": grasslandArmour[0][3]
    },
    grasslandArmour[1][0]: {
        "dmgRed": grasslandArmour[1][1],
        "levelReq": grasslandArmour[1][2],
        "price": grasslandArmour[1][3]
    },
    grasslandArmour[2][0]: {
        "dmgRed": grasslandArmour[2][1],
        "levelReq": grasslandArmour[2][2],
        "price": grasslandArmour[2][3]
    },
    darkForestArmour[0][0]: {
        "dmgRed": darkForestArmour[0][1],
        "levelReq": darkForestArmour[0][2],
        "price": darkForestArmour[0][3]
    },
    darkForestArmour[1][0]: {
        "dmgRed": darkForestArmour[1][1],
        "levelReq": darkForestArmour[1][2],
        "price": darkForestArmour[1][3]
    },
    darkForestArmour[2][0]: {
        "dmgRed": darkForestArmour[2][1],
        "levelReq": darkForestArmour[2][2],
        "price": darkForestArmour[2][3]
    },
    frozenPeakArmour[0][0]: {
        "dmgRed": frozenPeakArmour[0][1],
        "levelReq": frozenPeakArmour[0][2],
        "price": frozenPeakArmour[0][3]
    },
    frozenPeakArmour[1][0]: {
        "dmgRed": frozenPeakArmour[1][1],
        "levelReq": frozenPeakArmour[1][2],
        "price": frozenPeakArmour[1][3]
    },
    frozenPeakArmour[2][0]: {
        "dmgRed": frozenPeakArmour[2][1],
        "levelReq": frozenPeakArmour[2][2],
        "price": frozenPeakArmour[2][3]
    },
    lostCavesArmour[0][0]: {
        "dmgRed": lostCavesArmour[0][1],
        "levelReq": lostCavesArmour[0][2],
        "price": lostCavesArmour[0][3]
    },
    lostCavesArmour[1][0]: {
        "dmgRed": lostCavesArmour[1][1],
        "levelReq": lostCavesArmour[1][2],
        "price": lostCavesArmour[1][3]
    },
    lostCavesArmour[2][0]: {
        "dmgRed": lostCavesArmour[2][1],
        "levelReq": lostCavesArmour[2][2],
        "price": lostCavesArmour[2][3]
    },
    burningWasteArmour[0][0]: {
        "dmgRed": burningWasteArmour[0][1],
        "levelReq": burningWasteArmour[0][2],
        "price": burningWasteArmour[0][3]
    },
    burningWasteArmour[1][0]: {
        "dmgRed": burningWasteArmour[1][1],
        "levelReq": burningWasteArmour[1][2],
        "price": burningWasteArmour[1][3]
    },
    burningWasteArmour[2][0]: {
        "dmgRed": burningWasteArmour[2][1],
        "levelReq": burningWasteArmour[2][2],
        "price": burningWasteArmour[2][3]
    },
    dungeonArmours[0][0]: {
        "dmgRed": dungeonArmours[0][1],
        "levelReq": dungeonArmours[0][2]
    },
    dungeonArmours[1][0]: {
        "dmgRed": dungeonArmours[1][1],
        "levelReq": dungeonArmours[1][2]
    },
    dungeonArmours[2][0]: {
        "dmgRed": dungeonArmours[2][1],
        "levelReq": dungeonArmours[2][2]
    },
    dungeonArmours[3][0]: {
        "dmgRed": dungeonArmours[3][1],
        "levelReq": dungeonArmours[3][2]
    },
    dungeonArmours[4][0]: {
        "dmgRed": dungeonArmours[4][1],
        "levelReq": dungeonArmours[4][2]
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
    healthPotions[0][0]: {
        "amount": healthPotions[0][1],
        "price": healthPotions[0][2]
    },
    healthPotions[1][0]: {
        "amount": healthPotions[1][1],
        "price": healthPotions[1][2]
    },
    healthPotions[2][0]: {
        "amount": healthPotions[2][1],
        "price": healthPotions[2][2]
    },
    healthPotions[3][0]: {
        "amount": healthPotions[3][1],
        "price": healthPotions[3][2]
    },
    healthPotions[4][0]: {
        "amount": healthPotions[4][1],
        "price": healthPotions[4][2]
    }
}