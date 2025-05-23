# swords = [name][mindamage][maxdamage][levelrequired][price]

# Warrior weapons
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








# Ranged weapons
grasslandRanged = [
    ["Worn Bow", 3, 8, 1, 15],
    ["Hunting Bow", 6, 13, 3, 50],
    ["Short Recurve Bow", 9, 16, 5, 120],
    ["Longbow", 11, 19, 7, 250],
    ["Outlaw's Crossbow", 14, 21, 9, 400]
]

darkForestRanged = [
    ["Silent Hunter Bow", 17, 23, 11, 600],
    ["Poisoned Arbalest", 20, 27, 13, 800],
    ["Elven Recurve", 23, 30, 15, 1000],
    ["Spectral Bow", 26, 33, 17, 1400],
    ["Viper's Fang Crossbow", 29, 35, 19, 1800]
]

frozenPeakRanged = [
    ["Ice Piercer", 31, 37, 21, 2500],
    ["Frozen Crossbow", 34, 40, 23, 3200],
    ["Blizzard Longbow", 37, 43, 25, 4000],
    ["Hailstorm Repeater", 40, 46, 27, 4800],
    ["Winter's Fang", 43, 49, 29, 5500]
]

lostCavesRanged = [
    ["Tunnel Bow", 45, 52, 31, 6000],
    ["Crystal Arbalest", 48, 54, 33, 6800],
    ["Cavern Splitter", 51, 57, 35, 7500],
    ["Explorer's Bow", 54, 60, 37, 8500],
    ["Geode Repeater", 57, 63, 39, 9200]
]

burningWasteRanged = [
    ["Cinder Bow", 60, 66, 41, 10000],
    ["Molten Recurve", 63, 69, 43, 11500],
    ["Scorched Arbalest", 66, 72, 45, 13000],
    ["Flarepiercer", 69, 75, 47, 15000],
    ["Blazing Crossbow", 72, 78, 49, 18000]
]

dungeonRanged = [
    ["Verdant Longbow", 16, 25, 10, 0],
    ["Fangshot Crossbow", 28, 38, 20, 0],
    ["Frozen Needle", 42, 54, 30, 0],
    ["Crystal Repeater", 56, 68, 40, 0],
    ["Flamepiercer", 70, 84, 50, 0]
]







# Magic weapons
grasslandMagic = [
    ["Cracked Wand", 6, 10, 1, 15],
    ["Amber Wand", 9, 14, 3, 50],
    ["Apprentice's Staff", 12, 18, 5, 120],
    ["Runed Staff", 15, 21, 7, 250],
    ["Seer's Focus", 18, 24, 9, 400]
]

darkForestMagic = [
    ["Wand of Withering", 20, 28, 11, 600],
    ["Venom Rune Wand", 24, 32, 13, 800],
    ["Spiritbinder Staff", 28, 36, 15, 1000],
    ["Wraith Channeler", 32, 40, 17, 1400],
    ["Soulfire Focus", 36, 44, 19, 1800]
]

frozenPeakMagic = [
    ["Chilling Wand", 36, 44, 21, 2500],
    ["Cryo Staff", 40, 48, 23, 3200],
    ["Glacial Focus", 44, 52, 25, 4000],
    ["Stormcaller's Staff", 48, 56, 27, 4800],
    ["Frozen Heart", 52, 60, 29, 5500]
]

lostCavesMagic = [
    ["Rune-Etched Wand", 50, 60, 31, 6000],
    ["Spectral Conduit", 54, 64, 33, 6800],
    ["Crystal Channeler", 58, 68, 35, 7500],
    ["Ancient Staff", 62, 72, 37, 8500],
    ["Runic Nexus", 66, 76, 39, 9200]
]

burningWasteMagic = [
    ["Wand of Embers", 66, 76, 41, 10000],
    ["Hellfire Rod", 70, 80, 43, 11500],
    ["Scorch Staff", 74, 84, 45, 13000],
    ["Inferno Channeler", 78, 88, 47, 15000],
    ["Demonfire Scepter", 82, 92, 49, 18000]
]

dungeonMagic = [
    ["Staff of Renewal", 22, 32, 10, 0],
    ["Nightshade Channeler", 36, 48, 20, 0],
    ["Icicle Staff", 52, 64, 30, 0],
    ["Echoing Spellblade", 68, 80, 40, 0],
    ["Volcanic Orb", 84, 96, 50, 0]
]



# creates a weapon object
def makeWeapon(min_dps, max_dps, level_req, price, type, className, damageType):
    weapon = {
        "minDps": min_dps,
        "maxDps": max_dps,
        "levelReq": level_req,
        "price": price,
        "type": type,
        "className": className,
        "damageType": damageType
    }
    return weapon

# a dictionary of weapons
weaponsDict = {
    #Swords
    "Wooden Sword": makeWeapon(4, 7, 1, 15, "sword", "Warrior", "physical"),
    "Rusty Iron Sword": makeWeapon(7, 12, 3, 50, "sword", "Warrior", "physical"),
    "Iron Shortsword": makeWeapon(10, 15, 5, 120, "sword", "Warrior", "physical"),
    "Steel Cutlass": makeWeapon(12, 18, 7, 250, "sword", "Warrior", "physical"),
    "Bandit's Saber": makeWeapon(15, 20, 9, 400, "sword", "Warrior", "physical"),
    "Shadowfang Blade": makeWeapon(18, 22, 11, 600, "sword", "Warrior", "physical"),
    "Venomous Rapier": makeWeapon(20, 25, 13, 800, "sword", "Warrior", "physical"),
    "Treant Cleaver": makeWeapon(22, 28, 15, 1000, "sword", "Warrior", "physical"),
    "Phantom Saber": makeWeapon(25, 30, 17, 1400, "sword", "Warrior", "physical"),
    "Nightfang Greatsword": makeWeapon(28, 32, 19, 1800, "sword", "Warrior", "physical"),
    "Frostbite Blade": makeWeapon(30, 35, 21, 2500, "sword", "Warrior", "physical"),
    "Glacial Edge": makeWeapon(32, 38, 23, 3200, "sword", "Warrior", "physical"),
    "Avalanche Cleaver": makeWeapon(35, 40, 25, 4000, "sword", "Warrior", "physical"),
    "Stormbreaker Sword": makeWeapon(38, 42, 27, 4800, "sword", "Warrior", "physical"),
    "Frozen Fang": makeWeapon(40, 45, 29, 5500, "sword", "Warrior", "physical"),
    "Stonecrusher Blade": makeWeapon(42, 48, 31, 6000, "sword", "Warrior", "physical"),
    "Serpent Fang Dagger": makeWeapon(45, 50, 33,6800, "sword", "Warrior", "physical"),
    "Phantom Scimitar": makeWeapon(48 ,52 ,35 ,7500, "sword", "Warrior", "physical"),
    "Explorer's Katana": makeWeapon(50 ,55 ,37 ,8500, "sword", "Warrior", "physical"),
    "Crystal Cleaver": makeWeapon(52 ,58 ,39 ,9200, "sword", "Warrior", "physical"),
    "Infernal Saber": makeWeapon(55 ,60 ,41 ,10000, "sword", "Warrior", "physical"),
    "Molten Edge": makeWeapon(58 ,62 ,43 ,11500, "sword", "Warrior", "physical"),
    "Blazefang Sword": makeWeapon(60 ,65 ,45 ,13000, "sword", "Warrior", "physical"),
    "Hellfire Claymore": makeWeapon(62 ,68 ,47 ,15000, "sword", "Warrior", "physical"),
    "Demon's Wrath": makeWeapon(65 ,70 ,49 ,18000, "sword", "Warrior", "physical"),
    "Blade of the Verdant Guardian": makeWeapon(18, 24, 10, 0, "sword", "Warrior", "physical"),
    "Nightshade Fang": makeWeapon(30, 36, 20, 0, "sword", "Warrior", "physical"),
    "Glacier's Bite": makeWeapon(45, 52, 30, 0, "sword", "Warrior", "physical"),
    "Crystal Reaver": makeWeapon(58, 65, 40, 0, "sword", "Warrior", "physical"),
    "Infernal Judgement": makeWeapon(72, 80, 50, 0, "sword", "Warrior", "physical"),


    #Ranged
    "Worn Bow": makeWeapon(3, 8, 1, 15, "bow", "Ranger", "physical"),
    "Hunting Bow": makeWeapon(6, 13, 3, 50, "bow", "Ranger", "physical"),
    "Short Recurve Bow": makeWeapon(9, 16, 5, 120, "bow", "Ranger", "physical"),
    "Longbow": makeWeapon(11, 19, 7, 250, "bow", "Ranger", "physical"),
    "Outlaw's Crossbow": makeWeapon(14, 21, 9, 400, "bow", "Ranger", "physical"),
    "Silent Hunter Bow": makeWeapon(17, 23, 11, 600, "bow", "Ranger", "physical"),
    "Poisoned Arbalest": makeWeapon(20, 27, 13, 800, "bow", "Ranger", "physical"),
    "Elven Recurve": makeWeapon(23, 30, 15, 1000, "bow", "Ranger", "physical"),
    "Spectral Bow": makeWeapon(26, 33, 17, 1400, "bow", "Ranger", "physical"),
    "Viper's Fang Crossbow": makeWeapon(29, 35, 19, 1800, "bow", "Ranger", "physical"),
    "Ice Piercer": makeWeapon(31, 37, 21, 2500, "bow", "Ranger", "physical"),
    "Frozen Crossbow": makeWeapon(34, 40, 23, 3200, "bow", "Ranger", "physical"),
    "Blizzard Longbow": makeWeapon(37, 43, 25, 4000, "bow", "Ranger", "physical"),
    "Hailstorm Repeater": makeWeapon(40, 46, 27, 4800, "bow", "Ranger", "physical"),
    "Winter's Fang": makeWeapon(43, 49, 29, 5500, "bow", "Ranger", "physical"),
    "Tunnel Bow": makeWeapon(45, 52, 31, 6000, "bow", "Ranger", "physical"),
    "Crystal Arbalest": makeWeapon(48, 54, 33, 6800, "bow", "Ranger", "physical"),
    "Cavern Splitter": makeWeapon(51, 57, 35, 7500, "bow", "Ranger", "physical"),
    "Explorer's Bow": makeWeapon(54, 60, 37, 8500, "bow", "Ranger", "physical"),
    "Geode Repeater": makeWeapon(57, 63, 39, 9200, "bow", "Ranger", "physical"),
    "Cinder Bow": makeWeapon(60, 66, 41, 10000, "bow", "Ranger", "physical"),
    "Molten Recurve": makeWeapon(63, 69, 43, 11500, "bow", "Ranger", "physical"),
    "Scorched Arbalest": makeWeapon(66, 72, 45, 13000, "bow", "Ranger", "physical"),
    "Flarepiercer": makeWeapon(69, 75, 47, 15000, "bow", "Ranger", "physical"),
    "Blazing Crossbow": makeWeapon(72, 78, 49, 18000, "bow", "Ranger", "physical"),
    "Verdant Longbow": makeWeapon(16, 25, 10, 0, "bow", "Ranger", "physical"),
    "Fangshot Crossbow": makeWeapon(28, 38, 20, 0, "bow", "Ranger", "physical"),
    "Frozen Needle": makeWeapon(42, 54, 30, 0, "bow", "Ranger", "physical"),
    "Crystal Repeater": makeWeapon(56, 68, 40, 0, "bow", "Ranger", "physical"),
    "Flamepiercer": makeWeapon(70, 84, 50, 0, "bow", "Ranger", "physical"),


    #Magic
    "Cracked Wand": makeWeapon(6, 10, 1, 15, "wand", "Mage", "poison"),
    "Amber Wand": makeWeapon(9, 14, 3, 50, "wand", "Mage", "poison"),
    "Apprentice's Staff": makeWeapon(12, 18, 5, 120, "wand", "Mage", "poison"),
    "Runed Staff": makeWeapon(15, 21, 7, 250, "wand", "Mage", "poison"),
    "Seer's Focus": makeWeapon(18, 24, 9, 400, "wand", "Mage", "poison"),
    "Wand of Withering": makeWeapon(20, 28, 11, 600, "wand", "Mage", "dark"),
    "Venom Rune Wand": makeWeapon(24, 32, 13, 800, "wand", "Mage", "dark"),
    "Spiritbinder Staff": makeWeapon(28, 36, 15, 1000, "wand", "Mage", "dark"),
    "Wraith Channeler": makeWeapon(32, 40, 17, 1400, "wand", "Mage", "dark"),
    "Soulfire Focus": makeWeapon(36, 44, 19, 1800, "wand", "Mage", "dark"),
    "Chilling Wand": makeWeapon(36, 44, 21, 2500, "wand", "Mage", "ice"),
    "Cryo Staff": makeWeapon(40, 48, 23, 3200, "wand", "Mage", "ice"),
    "Glacial Focus": makeWeapon(44, 52, 25, 4000, "wand", "Mage", "ice"),
    "Stormcaller's Staff": makeWeapon(48, 56, 27, 4800, "wand", "Mage", "ice"),
    "Frozen Heart": makeWeapon(52, 60, 29, 5500, "wand", "Mage", "ice"),
    "Rune-Etched Wand": makeWeapon(50, 60, 31, 6000, "wand", "Mage", "earth"),
    "Spectral Conduit": makeWeapon(54, 64, 33, 6800, "wand", "Mage", "earth"),
    "Crystal Channeler": makeWeapon(58, 68, 35, 7500, "wand", "Mage", "earth"),
    "Ancient Staff": makeWeapon(62, 72, 37, 8500, "wand", "Mage", "earth"),
    "Runic Nexus": makeWeapon(66, 76, 39, 9200, "wand", "Mage", "earth"),
    "Wand of Embers": makeWeapon(66, 76, 41, 10000, "wand", "Mage", "fire"),
    "Hellfire Rod": makeWeapon(70, 80, 43, 11500, "wand", "Mage", "fire"),
    "Scorch Staff": makeWeapon(74, 84, 45, 13000, "wand", "Mage", "fire"),
    "Inferno Channeler": makeWeapon(78, 88, 47, 15000, "wand", "Mage", "fire"),
    "Demonfire Scepter": makeWeapon(82, 92, 49, 18000, "wand", "Mage", "fire"),
    "Staff of Renewal": makeWeapon(22, 32, 10, 0, "wand", "Mage", "poison"),
    "Nightshade Channeler": makeWeapon(36, 48, 20, 0, "wand", "Mage", "dark"),
    "Icicle Staff": makeWeapon(52, 64, 30, 0, "wand", "Mage", "ice"),
    "Echoing Spellblade": makeWeapon(68, 80, 40, 0, "wand", "Mage", "earth"),
    "Volcanic Orb": makeWeapon(84, 96, 50, 0, "wand", "Mage", "fire")
}








# armour = [name][damage reduction][levelrequired][price]
grasslandMeleeArmour = [
    #Grasslands Armours
    ["Leather Vest", 3, 1, 50], 
    ["ChainMail Shirt", 6, 5, 200],  
    ["Iron Chestplate", 9, 9, 400]
]

darkForestMeleeArmour = [
    #Dark Forest Armours
    ["Shadow Cloak", 12, 11, 600], 
    ["Reinforced Hide", 16, 15, 1000],  
    ["Darksteel Cuirass", 20, 19, 1500]
]

frozenPeakMeleeArmour = [
    #Frozen Peak Armours
    ["Frostweave Coat", 22, 21, 2500], 
    ["Glacial Plate", 26, 25, 4000],  
    ["Avalanche Armour", 30, 29, 5500]
]

lostCavesMeleeArmour = [
    #Lost Caves Armours
    ["Phantom Robe", 32, 31, 6500], 
    ["Runed Plate", 36, 35, 8000],  
    ["Crystal Fortress", 40, 39, 10000]
]

burningWasteMeleeArmour = [
    #Burning Wastes Armours
    ["Emberweave Cloak", 42, 41, 12000], 
    ["Infernal Shell", 46, 45, 15000],  
    ["Hellfire Plate", 50, 49, 18000]
]

dungeonMeleeArmours = [
    #Dungeon Armours
    ["Sentinel's Aegis", 12, 10, 0], #Guardian Hollow
    ["Wraithbinder Vest", 18, 20, 0], #Shadowfall Grove
    ["Glacier Ward", 28, 30, 0], #Icebound Citadel
    ["Echoing Plate", 38, 40, 0], #Abyssal Tomb
    ["Molten King's Mantle", 50, 50, 0] #Infernal Depths
]



# shield = [name][damage reduction][levelrequired][price]
grasslandShields = [
    ["Worn Wooden Shield", 2, 2, 25],
    ["Iron Buckler", 4, 7, 75]
]

darkForestShields = [
    ["Spiked Hide Shield", 6, 12, 250],
    ["Sahdowguard", 8, 17, 400]
]

frozenPeakShields = [
    ["Frosted Tower Shield", 10, 22, 700],
    ["Iceforged Barrier", 12, 27, 1000]
]

lostCavesShields = [
    ["Runestone Pavise", 14, 32, 1500],
    ["Crystal Warden", 16, 37, 1800]
]

burningWasteShields = [
    ["Emberplate Bulwark", 18, 42, 2200],
    ["Infernal Bastion", 20, 47, 2700]
]





# Ranged armours
grasslandRangedArmour = [
    ["Padded Leather", 2, 1, 50],
    ["Hunter's Vest", 5, 5, 200],
    ["Ranger's Jacket", 8, 9, 400]
]

darkForestRangedArmour = [
    ["Camouflaged Tunic", 11, 11, 600],
    ["Silent Stalker Wrap", 14, 15, 1000],
    ["Darkwood Brigandine", 18, 19, 1500]
]

frozenPeakRangedArmour = [
    ["Snowstalker Garb", 20, 21, 2500],
    ["Iceshot Vest", 23, 25, 4000],
    ["Blizzard Mail", 27, 29, 5500]
]

lostCavesRangedArmour = [
    ["Wraithskin Cloak", 29, 31, 6500],
    ["Marksworn Armor", 33, 35, 8000],
    ["Shardscale Vest", 37, 39, 10000]
]

burningWasteRangedArmour = [
    ["Ashhide Wrap", 39, 41, 12000],
    ["Scorchguard Plate", 43, 45, 15000],
    ["Flamewarden Jacket", 47, 49, 18000]
]

dungeonRangedArmours = [
    ["Vigilant Camo", 11, 10, 0],     # Guardian Hollow
    ["Cloak of Shadowsight", 17, 20, 0],  # Shadowfall Grove
    ["Arctic Hunter Gear", 26, 30, 0],    # Icebound Citadel
    ["Gloomwalker's Mantle", 36, 40, 0],  # Abyssal Tomb
    ["Inferno Sharpshooter Vest", 48, 50, 0]  # Infernal Depths
]







# Mage armours
grasslandMageArmour = [
    ["Tattered Robe", 1, 1, 50],
    ["Apprentice Robe", 3, 5, 200],
    ["Enchanted Wraps", 5, 9, 400]
]

darkForestMageArmour = [
    ["Nightwoven Cloak", 7, 11, 600],
    ["Poisoner's Shroud", 10, 15, 1000],
    ["Hexed Silk Vestments", 14, 19, 1500]
]

frozenPeakMageArmour = [
    ["Snowthread Robes", 15, 21, 2500],
    ["Arcane Frostweave", 18, 25, 4000],
    ["Mystic Ice Vestments", 22, 29, 5500]
]

lostCavesMageArmour = [
    ["Echo Shroud", 24, 31, 6500],
    ["Runed Spectral Vest", 28, 35, 8000],
    ["Crystal Thaumaturge Robe", 32, 39, 10000]
]

burningWasteMageArmour = [
    ["Smoldering Wrap", 34, 41, 12000],
    ["Inferno Mystic Coat", 38, 45, 15000],
    ["Hellflame Mantle", 42, 49, 18000]
]

dungeonMageArmours = [
    ["Guardian's Arcana", 9, 10, 0],          # Guardian Hollow
    ["Shroud of Echoes", 15, 20, 0],          # Shadowfall Grove
    ["Glacierbound Vestments", 24, 30, 0],    # Icebound Citadel
    ["Voidwoven Mantle", 34, 40, 0],          # Abyssal Tomb
    ["Molten Arcanist Robe", 46, 50, 0]       # Infernal Depths
]



# creates an armour object
def makeArmour(dmg_red, level_req, price, type, className):
    armour = {
        "dmgRed": dmg_red,
        "levelReq": level_req,
        "price": price,
        "type": type,
        "className": className
    }
    return armour

# a dictionary of armours
armourDict = {
    #Melee Armours
    "Cloth Scraps": makeArmour(0, 0, 0, "armour", "Warrior"),
    "Leather Vest": makeArmour(3, 1, 50, "armour", "Warrior"),
    "ChainMail Shirt": makeArmour(6, 5, 200, "armour", "Warrior"),
    "Iron Chestplate": makeArmour(9, 9, 400, "armour", "Warrior"),
    "Shadow Cloak": makeArmour(12, 11, 600, "armour", "Warrior"),
    "Reinforced Hide": makeArmour(16, 15, 1000, "armour", "Warrior"),
    "Darksteel Cuirass": makeArmour(20, 19, 1500, "armour", "Warrior"),
    "Frostweave Coat": makeArmour(22, 21, 2500, "armour", "Warrior"),
    "Glacial Plate": makeArmour(26, 25, 4000, "armour", "Warrior"),
    "Avalanche Armour": makeArmour(30, 29, 5500, "armour", "Warrior"),
    "Phantom Robe": makeArmour(32, 31, 6500, "armour", "Warrior"),
    "Runed Plate": makeArmour(36, 35, 8000, "armour", "Warrior"),
    "Crystal Fortress": makeArmour(40, 39, 10000, "armour", "Warrior"),
    "Emberweave Cloak": makeArmour(42, 41, 12000, "armour", "Warrior"),
    "Infernal Shell": makeArmour(46, 45, 15000, "armour", "Warrior"),
    "Hellfire Plate": makeArmour(50, 49, 18000, "armour", "Warrior"),
    "Sentinel's Aegis": makeArmour(12, 10, 0, "armour", "Warrior"),
    "Wraithbinder Vest": makeArmour(18, 20, 0, "armour", "Warrior"),
    "Glacier Ward": makeArmour(28, 30, 0, "armour", "Warrior"),
    "Echoing Plate": makeArmour(38, 40, 0, "armour", "Warrior"),
    "Molten King's Mantle": makeArmour(50, 50, 0, "armour", "Warrior"),

    #Shields
    "Broken Shield": makeArmour(0, 0, 0, "shield", "Warrior"),
    "Worn Wooden Shield": makeArmour(2, 2, 25, "shield", "Warrior"),
    "Iron Buckler": makeArmour(4, 7, 75, "shield", "Warrior"),
    "Spiked Hide Shield": makeArmour(6, 12, 250, "shield", "Warrior"),
    "Sahdowguard": makeArmour(8, 17, 400, "shield", "Warrior"),
    "Frosted Tower Shield": makeArmour(10, 22, 700, "shield", "Warrior"),
    "Iceforged Barrier": makeArmour(12, 27, 1000, "shield", "Warrior"),
    "Runestone Pavise": makeArmour(14, 32, 1500, "shield", "Warrior"),
    "Crystal Warden": makeArmour(16, 37, 1800, "shield", "Warrior"),
    "Emberplate Bulwark": makeArmour(18, 42, 2200, "shield", "Warrior"),
    "Infernal Bastion": makeArmour(20, 47, 2700, "shield", "Warrior"),

    #Ranged Armours
    "Padded Leather": makeArmour(2, 1, 50, "armour", "Ranger"),
    "Hunter's Vest": makeArmour(5, 5, 200, "armour", "Ranger"),
    "Ranger's Jacket": makeArmour(8, 9, 400, "armour", "Ranger"),
    "Camouflaged Tunic": makeArmour(11, 11, 600, "armour", "Ranger"),
    "Silent Stalker Wrap": makeArmour(14, 15, 1000, "armour", "Ranger"),
    "Darkwood Brigandine": makeArmour(18, 19, 1500, "armour", "Ranger"),
    "Snowstalker Garb": makeArmour(20, 21, 2500, "armour", "Ranger"),
    "Iceshot Vest": makeArmour(23, 25, 4000, "armour", "Ranger"),
    "Blizzard Mail": makeArmour(27, 29, 5500, "armour", "Ranger"),
    "Wraithskin Cloak": makeArmour(29, 31, 6500, "armour", "Ranger"),
    "Marksworn Armor": makeArmour(33, 35, 8000, "armour", "Ranger"),
    "Shardscale Vest": makeArmour(37, 39, 10000, "armour", "Ranger"),
    "Ashhide Wrap": makeArmour(39, 41, 12000, "armour", "Ranger"),
    "Scorchguard Plate": makeArmour(43, 45, 15000, "armour", "Ranger"),
    "Flamewarden Jacket": makeArmour(47, 49, 18000, "armour", "Ranger"),
    "Vigilant Camo": makeArmour(11, 10, 0, "armour", "Ranger"),
    "Cloak of Shadowsight": makeArmour(17, 20, 0, "armour", "Ranger"),
    "Arctic Hunter Gear": makeArmour(26, 30, 0, "armour", "Ranger"),
    "Gloomwalker's Mantle": makeArmour(36, 40, 0, "armour", "Ranger"),
    "Inferno Sharpshooter Vest": makeArmour(48 ,50 ,0, "armour", "Ranger"),


    #Mage Armours
    "Tattered Robe": makeArmour(1, 1, 50, "armour", "Mage"),
    "Apprentice Robe": makeArmour(3, 5, 200, "armour", "Mage"),
    "Enchanted Wraps": makeArmour(5, 9, 400, "armour", "Mage"),
    "Nightwoven Cloak": makeArmour(7, 11, 600, "armour", "Mage"),
    "Poisoner's Shroud": makeArmour(10, 15, 1000, "armour", "Mage"),
    "Hexed Silk Vestments": makeArmour(14, 19, 1500, "armour", "Mage"),
    "Snowthread Robes": makeArmour(15, 21, 2500, "armour", "Mage"),
    "Arcane Frostweave": makeArmour(18, 25, 4000, "armour", "Mage"),
    "Mystic Ice Vestments": makeArmour(22, 29, 5500, "armour", "Mage"),
    "Echo Shroud": makeArmour(24, 31, 6500, "armour", "Mage"),
    "Runed Spectral Vest": makeArmour(28 ,35 ,8000, "armour", "Mage"),
    "Crystal Thaumaturge Robe": makeArmour(32 ,39 ,10000, "armour", "Mage"),
    "Smoldering Wrap": makeArmour(34 ,41 ,12000, "armour", "Mage"),
    "Inferno Mystic Coat": makeArmour(38 ,45 ,15000, "armour", "Mage"),
    "Hellflame Mantle": makeArmour(42 ,49 ,18000, "armour", "Mage"),
    "Guardian's Arcana": makeArmour(9 ,10 ,0, "armour", "Mage"),
    "Shroud of Echoes": makeArmour(15 ,20 ,0, "armour", "Mage"),
    "Glacierbound Vestments": makeArmour(24 ,30 ,0, "armour", "Mage"),
    "Voidwoven Mantle": makeArmour(34 ,40 ,0, "armour", "Mage"),
    "Molten Arcanist Robe": makeArmour(46 ,50 ,0, "armour", "Mage")
}







# specialArrows = [name][effect][chance][damage][period][levelrequired][price] - consumable arrows
grasslandArrows = [
    ["Piercing Arrow", "Pierce", 10, 0, 0, 2, 100],
    ["Barbed Arrow", "Bleed", 20, 5, 2, 7, 150]
]

darkForestArrows = [
    ["Poisoned Arrow", "Poison", 30, 5, 3, 12, 300],
    ["Splinter Arrow", "Split", 40, 25, 0, 17, 400]
]

frozenPeakArrows = [
    ["Frost Arrow", "Freeze", 20, 0, 1, 22, 600],
    ["Chilling Arrow", "Slow", 100, 0, 3, 27, 800]
]

lostCavesArrows = [
    ["Blinding Arrow", "Blind", 20, 0, 2, 32, 1000],
    ["Explosive Arrow", "Pierce", 20, 0, 0, 37, 1300]
]

burningWasteArrows = [
    ["Scorching Arrow", "Bleed", 100, 10, 3, 42, 1600],
    ["Piercer Bolts", "Pierce", 40, 0, 0, 47, 2000]
]

# creates an arrow object
def makeArrow(effect, chance, damage, period, level_req, price):
    arrow = {
        "effect": effect,
        "chance": chance,
        "damage": damage,
        "period": period,
        "levelReq": level_req,
        "price": price
    }
    return arrow

# a dictionary of arrows
arrowsDict = {
    "Piercing Arrow": makeArrow("Pierce", 10, 0, 0, 2, 100),
    "Barbed Arrow": makeArrow("Bleed", 20, 5, 2, 7, 150),
    "Poisoned Arrow": makeArrow("Poison", 30, 5, 3, 12, 300),
    "Splinter Arrow": makeArrow("Split", 40, 25, 0, 17, 400),
    "Frost Arrow": makeArrow("Freeze", 20, 0, 1, 22, 600),
    "Chilling Arrow": makeArrow("Slow", 100, 0, 3, 27, 800),
    "Blinding Arrow": makeArrow("Blind", 20, 0, 2, 32, 1000),
    "Explosive Arrow": makeArrow("Pierce", 20, 0, 0, 37, 1300),
    "Scorching Arrow": makeArrow("Bleed", 100, 10, 3, 42, 1600),
    "Piercer Bolts": makeArrow("Pierce", 40, 0, 0, 47, 2000)
}








# tomes = [name][damageType][bonusDamage(%)][levelrequired][price]
tomes = [
    ["Nature Tome", "poison", 10, 1, 500],
    ["Shadow Tome", "dark", 15, 11, 1000],
    ["Frost Tome", "ice", 20, 21, 2000],
    ["Earth Tome", "earth", 25, 31, 3500],
    ["Fire Tome", "fire", 30, 41, 5000]
]

# creates a rune object
def makeTome(effect, bonusDamage, level_req, price):
    tome = {
        "effect": effect,
        "bonusDamage": bonusDamage,
        "levelReq": level_req,
        "price": price
    }
    return tome

# a dictionary of runes
tomeDict = {
    "Old Leather Tome": makeTome("written", 0, 0, 0),
    "Nature Tome": makeTome ("Poison", 10, 1, 500),
    "Shadow Tome": makeTome ("Dark", 15, 11, 1000),
    "Frost Tome": makeTome ("Ice", 20, 21, 2000),
    "Earth Tome": makeTome ("Earth", 25, 31, 3500),
    "Fire Tome": makeTome ("Fire", 30, 41, 5000)
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