# swords = [name][mindamage][maxdamage][levelrequired][price]
grasslandSwords = [
    #Grasslands swords
    ["Wooden Sword", 4, 7, 1, 15], 
    ["Rusty Iron Sword", 7, 12, 3, 50],  
    ["Iron Shortsword", 10, 15, 5, 120],
    ["Steel Cutlass", 12, 18, 7, 250],  
    ["Bandit's Saber", 15, 20, 9, 400]
]

grasslandRanged = [
    ["Worn Bow", 3, 8, 1, 15],
    ["Hunting Bow", 6, 13, 3, 50],
    ["Short Recurve Bow", 9, 16, 5, 120],
    ["Longbow", 11, 19, 7, 250],
    ["Outlaw's Crossbow", 14, 21, 9, 400]
]

grasslandMagic = [
    ["Cracked Wand", 6, 10, 1, 15],
    ["Amber Wand", 9, 14, 3, 50],
    ["Apprentice's Staff", 12, 18, 5, 120],
    ["Runed Staff", 15, 21, 7, 250],
    ["Seer's Focus", 18, 24, 9, 400]
]

darkForestSword = [
    #Dark Forest swords
    ["Shadowfang Blade", 18, 22, 11, 600], 
    ["Venomous Rapier", 20, 25, 13, 800], 
    ["Treant Cleaver", 22, 28, 15, 1000], 
    ["Phantom Saber", 25, 30, 17, 1400],
    ["Nightfang Greatesword", 28, 32, 19, 1800]
]

darkForestRanged = [
    ["Silent Hunter Bow", 17, 23, 11, 600],
    ["Poisoned Arbalest", 20, 27, 13, 800],
    ["Elven Recurve", 23, 30, 15, 1000],
    ["Spectral Bow", 26, 33, 17, 1400],
    ["Viper's Fang Crossbow", 29, 35, 19, 1800]
]

darkForestMagic = [
    ["Wand of Withering", 20, 28, 11, 600],
    ["Venom Rune Wand", 24, 32, 13, 800],
    ["Spiritbinder Staff", 28, 36, 15, 1000],
    ["Wraith Channeler", 32, 40, 17, 1400],
    ["Soulfire Focus", 36, 44, 19, 1800]
]

frozenPeakSwords = [
    #Frozen Peaks swords
    ["Frostbite Blade", 30, 35, 21, 2500], 
    ["Glacial Edge", 32, 38, 23, 3200], 
    ["Avalanche Cleaver", 35, 40, 25, 4000], 
    ["Stormbreaker Sword", 38, 42, 27, 4800], 
    ["Frozen Fang", 40, 45, 29, 5500] 
]

frozenPeakRanged = [
    ["Ice Piercer", 31, 37, 21, 2500],
    ["Frozen Crossbow", 34, 40, 23, 3200],
    ["Blizzard Longbow", 37, 43, 25, 4000],
    ["Hailstorm Repeater", 40, 46, 27, 4800],
    ["Winter's Fang", 43, 49, 29, 5500]
]

frozenPeakMagic = [
    ["Chilling Wand", 36, 44, 21, 2500],
    ["Cryo Staff", 40, 48, 23, 3200],
    ["Glacial Focus", 44, 52, 25, 4000],
    ["Stormcaller's Staff", 48, 56, 27, 4800],
    ["Frozen Heart", 52, 60, 29, 5500]
]

lostCaveSwords = [
    #Lost Caves swords
    ["Stonecrusher Blade", 42, 48, 31, 6000], 
    ["Serpent Fang Dagger", 45, 50, 33, 6800], 
    ["Phantom Scimitar", 48, 52, 35, 7500], 
    ["Explorer's Katana", 50, 55, 37, 8500], 
    ["Crystal Cleaver", 52, 58, 39, 9200]
]

lostCavesRanged = [
    ["Tunnel Bow", 45, 52, 31, 6000],
    ["Crystal Arbalest", 48, 54, 33, 6800],
    ["Cavern Splitter", 51, 57, 35, 7500],
    ["Explorer's Bow", 54, 60, 37, 8500],
    ["Geode Repeater", 57, 63, 39, 9200]
]

lostCavesMagic = [
    ["Rune-Etched Wand", 50, 60, 31, 6000],
    ["Spectral Conduit", 54, 64, 33, 6800],
    ["Crystal Channeler", 58, 68, 35, 7500],
    ["Ancient Staff", 62, 72, 37, 8500],
    ["Runic Nexus", 66, 76, 39, 9200]
]

burningWasteSwords = [
    #Burning Wastes Swords
    ["Infernal Saber", 55, 60, 41, 10000], 
    ["Molten Edge", 58, 62, 43, 11500], 
    ["Blazefang Sword", 60, 65, 45, 13000],
    ["Hellfire Claymore", 62, 68, 47, 15000], 
    ["Demon's Wrath", 65, 70, 49, 18000]
]

burningWasteRanged = [
    ["Cinder Bow", 60, 66, 41, 10000],
    ["Molten Recurve", 63, 69, 43, 11500],
    ["Scorched Arbalest", 66, 72, 45, 13000],
    ["Flarepiercer", 69, 75, 47, 15000],
    ["Blazing Crossbow", 72, 78, 49, 18000]
]

burningWasteMagic = [
    ["Wand of Embers", 66, 76, 41, 10000],
    ["Hellfire Rod", 70, 80, 43, 11500],
    ["Scorch Staff", 74, 84, 45, 13000],
    ["Inferno Channeler", 78, 88, 47, 15000],
    ["Demonfire Scepter", 82, 92, 49, 18000]
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

dungeonRanged = [
    ["Verdant Longbow", 16, 25, 10, 0],
    ["Fangshot Crossbow", 28, 38, 20, 0],
    ["Frozen Needle", 42, 54, 30, 0],
    ["Crystal Repeater", 56, 68, 40, 0],
    ["Flamepiercer", 70, 84, 50, 0]
]

dungeonMagic = [
    ["Staff of Renewal", 22, 32, 10, 0],
    ["Nightshade Channeler", 36, 48, 20, 0],
    ["Icicle Staff", 52, 64, 30, 0],
    ["Echoing Spellblade", 68, 80, 40, 0],
    ["Volcanic Orb", 84, 96, 50, 0]
]

def makeWeapon(min_dps, max_dps, level_req, price):
    weapon = {
        "minDps": min_dps,
        "maxDps": max_dps,
        "levelReq": level_req,
        "price": price
    }
    return weapon

weaponsDict = {
    #Swords
    "Wooden Sword": makeWeapon(4, 7, 1, 15),
    "Rusty Iron Sword": makeWeapon(7, 12, 3, 50),
    "Iron Shortsword": makeWeapon(10, 15, 5, 120),
    "Steel Cutlass": makeWeapon(12, 18, 7, 250),
    "Bandit's Saber": makeWeapon(15, 20, 9, 400),
    "Shadowfang Blade": makeWeapon(18, 22, 11, 600),
    "Venomous Rapier": makeWeapon(20, 25, 13, 800),
    "Treant Cleaver": makeWeapon(22, 28, 15, 1000),
    "Phantom Saber": makeWeapon(25, 30, 17, 1400),
    "Nightfang Greatsword": makeWeapon(28, 32, 19, 1800),
    "Frostbite Blade": makeWeapon(30, 35, 21, 2500),
    "Glacial Edge": makeWeapon(32, 38, 23, 3200),
    "Avalanche Cleaver": makeWeapon(35, 40, 25, 4000),
    "Stormbreaker Sword": makeWeapon(38, 42, 27, 4800),
    "Frozen Fang": makeWeapon(40, 45, 29, 5500),
    "Stonecrusher Blade": makeWeapon(42, 48, 31, 6000),
    "Serpent Fang Dagger": makeWeapon(45, 50, 33,6800),
    "Phantom Scimitar": makeWeapon(48 ,52 ,35 ,7500),
    "Explorer's Katana": makeWeapon(50 ,55 ,37 ,8500),
    "Crystal Cleaver": makeWeapon(52 ,58 ,39 ,9200),
    "Infernal Saber": makeWeapon(55 ,60 ,41 ,10000),
    "Molten Edge": makeWeapon(58 ,62 ,43 ,11500),
    "Blazefang Sword": makeWeapon(60 ,65 ,45 ,13000),
    "Hellfire Claymore": makeWeapon(62 ,68 ,47 ,15000),
    "Demon's Wrath": makeWeapon(65 ,70 ,49 ,18000),
    "Blade of the Verdant Guardian": makeWeapon(18, 24, 10, 0),
    "Nightshade Fang": makeWeapon(30, 36, 20, 0),
    "Glacier's Bite": makeWeapon(45, 52, 30, 0),
    "Crystal Reaver": makeWeapon(58, 65, 40, 0),
    "Infernal Judgement": makeWeapon(72, 80, 50, 0),

    #Ranged
    "Worn Bow": makeWeapon(3, 8, 1, 15),
    "Hunting Bow": makeWeapon(6, 13, 3, 50),
    "Short Recurve Bow": makeWeapon(9, 16, 5, 120),
    "Longbow": makeWeapon(11, 19, 7, 250),
    "Outlaw's Crossbow": makeWeapon(14, 21, 9, 400),
    "Silent Hunter Bow": makeWeapon(17, 23, 11, 600),
    "Poisoned Arbalest": makeWeapon(20, 27, 13, 800),
    "Elven Recurve": makeWeapon(23, 30, 15, 1000),
    "Spectral Bow": makeWeapon(26, 33, 17, 1400),
    "Viper's Fang Crossbow": makeWeapon(29, 35, 19, 1800),
    "Ice Piercer": makeWeapon(31, 37, 21, 2500),
    "Frozen Crossbow": makeWeapon(34, 40, 23, 3200),
    "Blizzard Longbow": makeWeapon(37, 43, 25, 4000),
    "Hailstorm Repeater": makeWeapon(40, 46, 27, 4800),
    "Winter's Fang": makeWeapon(43, 49, 29, 5500),
    "Tunnel Bow": makeWeapon(45, 52, 31, 6000),
    "Crystal Arbalest": makeWeapon(48, 54, 33, 6800),
    "Cavern Splitter": makeWeapon(51, 57, 35, 7500),
    "Explorer's Bow": makeWeapon(54, 60, 37, 8500),
    "Geode Repeater": makeWeapon(57, 63, 39, 9200),
    "Cinder Bow": makeWeapon(60, 66, 41, 10000),
    "Molten Recurve": makeWeapon(63, 69, 43, 11500),
    "Scorched Arbalest": makeWeapon(66, 72, 45, 13000),
    "Flarepiercer": makeWeapon(69, 75, 47, 15000),
    "Blazing Crossbow": makeWeapon(72, 78, 49, 18000),
    "Verdant Longbow": makeWeapon(16, 25, 10, 0),
    "Fangshot Crossbow": makeWeapon(28, 38, 20, 0),
    "Frozen Needle": makeWeapon(42, 54, 30, 0),
    "Crystal Repeater": makeWeapon(56, 68, 40, 0),
    "Flamepiercer": makeWeapon(70, 84, 50, 0),

    #Magic
    "Cracked Wand": makeWeapon(6, 10, 1, 15),
    "Amber Wand": makeWeapon(9, 14, 3, 50),
    "Apprentice's Staff": makeWeapon(12, 18, 5, 120),
    "Runed Staff": makeWeapon(15, 21, 7, 250),
    "Seer's Focus": makeWeapon(18, 24, 9, 400),
    "Wand of Withering": makeWeapon(20, 28, 11, 600),
    "Venom Rune Wand": makeWeapon(24, 32, 13, 800),
    "Spiritbinder Staff": makeWeapon(28, 36, 15, 1000),
    "Wraith Channeler": makeWeapon(32, 40, 17, 1400),
    "Soulfire Focus": makeWeapon(36, 44, 19, 1800),
    "Chilling Wand": makeWeapon(36, 44, 21, 2500),
    "Cryo Staff": makeWeapon(40, 48, 23, 3200),
    "Glacial Focus": makeWeapon(44, 52, 25, 4000),
    "Stormcaller's Staff": makeWeapon(48, 56, 27, 4800),
    "Frozen Heart": makeWeapon(52, 60, 29, 5500),
    "Rune-Etched Wand": makeWeapon(50, 60, 31, 6000),
    "Spectral Conduit": makeWeapon(54, 64, 33, 6800),
    "Crystal Channeler": makeWeapon(58, 68, 35, 7500),
    "Ancient Staff": makeWeapon(62, 72, 37, 8500),
    "Runic Nexus": makeWeapon(66, 76, 39, 9200),
    "Wand of Embers": makeWeapon(66, 76, 41, 10000),
    "Hellfire Rod": makeWeapon(70, 80, 43, 11500),
    "Scorch Staff": makeWeapon(74, 84, 45, 13000),
    "Inferno Channeler": makeWeapon(78, 88, 47, 15000),
    "Demonfire Scepter": makeWeapon(82, 92, 49, 18000),
    "Staff of Renewal": makeWeapon(22, 32, 10, 0),
    "Nightshade Channeler": makeWeapon(36, 48, 20, 0),
    "Icicle Staff": makeWeapon(52, 64, 30, 0),
    "Echoing Spellblade": makeWeapon(68, 80, 40, 0),
    "Volcanic Orb": makeWeapon(84, 96, 50, 0)
}

# armour = [name][damage reduction][levelrequired][price]
grasslandMeleeArmour = [
    #Grasslands Armours
    ["Leather Vest", 3, 1, 50], 
    ["ChainMail Shirt", 6, 5, 200],  
    ["Iron Chestplate", 9, 9, 400]
]

grasslandRangedArmour = [
    ["Padded Leather", 2, 1, 50],
    ["Hunter's Vest", 5, 5, 200],
    ["Ranger's Jacket", 8, 9, 400]
]

grasslandMageArmour = [
    ["Tattered Robe", 1, 1, 50],
    ["Apprentice Robe", 3, 5, 200],
    ["Enchanted Wraps", 5, 9, 400]
]

darkForestMeleeArmour = [
    #Dark Forest Armours
    ["Shadow Cloak", 12, 11, 600], 
    ["Reinforced Hide", 16, 15, 1000],  
    ["Darksteel Cuirass", 20, 19, 1500]
]

darkForestRangedArmour = [
    ["Camouflaged Tunic", 11, 11, 600],
    ["Silent Stalker Wrap", 14, 15, 1000],
    ["Darkwood Brigandine", 18, 19, 1500]
]

darkForestMageArmour = [
    ["Nightwoven Cloak", 7, 11, 600],
    ["Poisoner's Shroud", 10, 15, 1000],
    ["Hexed Silk Vestments", 14, 19, 1500]
]

frozenPeakMeleeArmour = [
    #Frozen Peak Armours
    ["Frostweave Coat", 22, 21, 2500], 
    ["Glacial Plate", 26, 25, 4000],  
    ["Avalanche Armour", 30, 29, 5500]
]

frozenPeakRangedArmour = [
    ["Snowstalker Garb", 20, 21, 2500],
    ["Iceshot Vest", 23, 25, 4000],
    ["Blizzard Mail", 27, 29, 5500]
]

frozenPeakMageArmour = [
    ["Snowthread Robes", 15, 21, 2500],
    ["Arcane Frostweave", 18, 25, 4000],
    ["Mystic Ice Vestments", 22, 29, 5500]
]

lostCavesMeleeArmour = [
    #Lost Caves Armours
    ["Phantom Robe", 32, 31, 6500], 
    ["Runed Plate", 36, 35, 8000],  
    ["Crystal Fortress", 40, 39, 10000]
]

lostCavesRangedArmour = [
    ["Wraithskin Cloak", 29, 31, 6500],
    ["Marksworn Armor", 33, 35, 8000],
    ["Shardscale Vest", 37, 39, 10000]
]

lostCavesMageArmour = [
    ["Echo Shroud", 24, 31, 6500],
    ["Runed Spectral Vest", 28, 35, 8000],
    ["Crystal Thaumaturge Robe", 32, 39, 10000]
]

burningWasteMeleeArmour = [
    #Burning Wastes Armours
    ["Emberweave Cloak", 42, 41, 12000], 
    ["Infernal Shell", 46, 45, 15000],  
    ["Hellfire Plate", 50, 49, 18000]
]

burningWasteRangedArmour = [
    ["Ashhide Wrap", 39, 41, 12000],
    ["Scorchguard Plate", 43, 45, 15000],
    ["Flamewarden Jacket", 47, 49, 18000]
]

burningWasteMageArmour = [
    ["Smoldering Wrap", 34, 41, 12000],
    ["Inferno Mystic Coat", 38, 45, 15000],
    ["Hellflame Mantle", 42, 49, 18000]
]

dungeonMeleeArmours = [
    #Dungeon Armours
    ["Sentinel's Aegis", 12, 10, 0], #Guardian Hollow
    ["Wraithbinder Vest", 18, 20, 0], #Shadowfall Grove
    ["Glacier Ward", 28, 30, 0], #Icebound Citadel
    ["Echoing Plate", 38, 40, 0], #Abyssal Tomb
    ["Molten King's Mantle", 50, 50, 0] #Infernal Depths
]

dungeonRangedArmours = [
    ["Vigilant Camo", 11, 10, 0],     # Guardian Hollow
    ["Cloak of Shadowsight", 17, 20, 0],  # Shadowfall Grove
    ["Arctic Hunter Gear", 26, 30, 0],    # Icebound Citadel
    ["Gloomwalker's Mantle", 36, 40, 0],  # Abyssal Tomb
    ["Inferno Sharpshooter Vest", 48, 50, 0]  # Infernal Depths
]

dungeonMageArmours = [
    ["Guardian's Arcana", 9, 10, 0],          # Guardian Hollow
    ["Shroud of Echoes", 15, 20, 0],          # Shadowfall Grove
    ["Glacierbound Vestments", 24, 30, 0],    # Icebound Citadel
    ["Voidwoven Mantle", 34, 40, 0],          # Abyssal Tomb
    ["Molten Arcanist Robe", 46, 50, 0]       # Infernal Depths
]

def makeArmour(dmg_red, level_req, price):
    armour = {
        "dmgRed": dmg_red,
        "levelReq": level_req,
        "price": price
    }
    return armour

armourDict = {
    #Melee Armours
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
    "Molten King's Mantle": makeArmour(50, 50, 0),

    #Ranged Armours
    "Padded Leather": makeArmour(2, 1, 50),
    "Hunter's Vest": makeArmour(5, 5, 200),
    "Ranger's Jacket": makeArmour(8, 9, 400),
    "Camouflaged Tunic": makeArmour(11, 11, 600),
    "Silent Stalker Wrap": makeArmour(14, 15, 1000),
    "Darkwood Brigandine": makeArmour(18, 19, 1500),
    "Snowstalker Garb": makeArmour(20, 21, 2500),
    "Iceshot Vest": makeArmour(23, 25, 4000),
    "Blizzard Mail": makeArmour(27, 29, 5500),
    "Wraithskin Cloak": makeArmour(29, 31, 6500),
    "Marksworn Armor": makeArmour(33, 35, 8000),
    "Shardscale Vest": makeArmour(37, 39, 10000),
    "Ashhide Wrap": makeArmour(39, 41, 12000),
    "Scorchguard Plate": makeArmour(43, 45, 15000),
    "Flamewarden Jacket": makeArmour(47, 49, 18000),
    "Vigilant Camo": makeArmour(11, 10, 0),
    "Cloak of Shadowsight": makeArmour(17, 20, 0),
    "Arctic Hunter Gear": makeArmour(26, 30, 0),
    "Gloomwalker's Mantle": makeArmour(36, 40, 0),
    "Inferno Sharpshooter Vest": makeArmour(48 ,50 ,0),

    #Mage Armours
    "Tattered Robe": makeArmour(1, 1, 50),
    "Apprentice Robe": makeArmour(3, 5, 200),
    "Enchanted Wraps": makeArmour(5, 9, 400),
    "Nightwoven Cloak": makeArmour(7, 11, 600),
    "Poisoner's Shroud": makeArmour(10, 15, 1000),
    "Hexed Silk Vestments": makeArmour(14, 19, 1500),
    "Snowthread Robes": makeArmour(15, 21, 2500),
    "Arcane Frostweave": makeArmour(18, 25, 4000),
    "Mystic Ice Vestments": makeArmour(22, 29, 5500),
    "Echo Shroud": makeArmour(24, 31, 6500),
    "Runed Spectral Vest": makeArmour(28 ,35 ,8000),
    "Crystal Thaumaturge Robe": makeArmour(32 ,39 ,10000),
    "Smoldering Wrap": makeArmour(34 ,41 ,12000),
    "Inferno Mystic Coat": makeArmour(38 ,45 ,15000),
    "Hellflame Mantle": makeArmour(42 ,49 ,18000),
    "Guardian's Arcana": makeArmour(9 ,10 ,0),
    "Shroud of Echoes": makeArmour(15 ,20 ,0),
    "Glacierbound Vestments": makeArmour(24 ,30 ,0),
    "Voidwoven Mantle": makeArmour(34 ,40 ,0),
    "Molten Arcanist Robe": makeArmour(46 ,50 ,0)
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