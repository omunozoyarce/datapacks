import pyperclip
from villager import Villager, Enchantment, Item, VillagerTrade

'''Armor enchantments:
Protection, Fire Protection, Blast Protection, Projectile Protection, 
Thorns, Mending, Unbreaking, Curse of Binding, Curse of Vanishing'''

'''Helmet exclusive:
Respiration, Aqua Affinity'''

'''Leggings exclusive:
Swift Sneak'''

'''Boots exclusive:	
Depth Strider, Frost Walker, Feather Falling, Soul Speed'''

#enchantments
protection = Enchantment("minecraft:protection", 4)
fire_protection = Enchantment("minecraft:fire_protection", 4)
blast_protection = Enchantment("minecraft:blast_protection", 4)
projectile_protection = Enchantment("minecraft:projectile_protection", 4)

thorns = Enchantment("minecraft:thorns", 3)
mending = Enchantment("minecraft:mending", 1)
unbreaking = Enchantment("minecraft:unbreaking", 3)
curse_of_binding = Enchantment("minecraft:binding_curse", 1)
curse_of_vanishing = Enchantment("minecraft:vanishing_curse", 1)

respiration = Enchantment("minecraft:respiration", 3)
aqua_affinity = Enchantment("minecraft:aqua_affinity", 1)

swift_sneak = Enchantment("minecraft:swift_sneak", 3)

depth_strider = Enchantment("minecraft:depth_strider", 3)
frost_walker = Enchantment("minecraft:frost_walker", 2)
feather_falling = Enchantment("minecraft:feather_falling", 4)
soul_speed = Enchantment("minecraft:soul_speed", 3)

efficiency = Enchantment("minecraft:efficiency", 5)
silk_touch = Enchantment("minecraft:silk_touch", 1)
fortune = Enchantment("minecraft:fortune", 3)

sharpness = Enchantment("minecraft:sharpness", 5)
smite = Enchantment("minecraft:smite", 5)
bane_of_arthropods = Enchantment("minecraft:bane_of_arthropods", 5)
looting = Enchantment("minecraft:looting", 3)
knockback = Enchantment("minecraft:knockback", 2)
fire_aspect = Enchantment("minecraft:fire_aspect", 2)
sweeping_edge = Enchantment("minecraft:sweeping", 3)

power = Enchantment("minecraft:power", 5)
punch = Enchantment("minecraft:punch", 2)
flame = Enchantment("minecraft:flame", 1)
infinity = Enchantment("minecraft:infinity", 1)

quick_charge = Enchantment("minecraft:quick_charge", 3)
piercing = Enchantment("minecraft:piercing", 4)
multishot = Enchantment("minecraft:multishot", 1)

riptide = Enchantment("minecraft:riptide", 3)
loyalty = Enchantment("minecraft:loyalty", 3)
impaling = Enchantment("minecraft:impaling", 5)
channeling = Enchantment("minecraft:channeling", 1)


# items
# armor order: protection, exclusive, thorns, standard (mending, unbreaking)

# helmet enchantments
helmet_enchantments, helmet_master_table = [], []
chestplate_enchantments, chestplate_master_table = [], []
leggings_enchantments, leggings_master_table = [], []
boots_enchantments, boots_master_table = [], []

for protection_type in [protection, fire_protection, blast_protection, projectile_protection]:
    helmet_enchantments.append(Item("minecraft:diamond_helmet", name="Perfect Helmet" , color="gold", 
                                    enchantments=[protection_type, respiration, aqua_affinity, mending, unbreaking]))
    helmet_enchantments.append(Item("minecraft:diamond_helmet", name="Spiked Helmet", color="red", 
                                    enchantments=[protection_type, respiration, aqua_affinity, thorns, mending, unbreaking]))
    
    chestplate_enchantments.append(Item("minecraft:diamond_chestplate", name="Perfect Chestplate" , color="gold", 
                                        enchantments=[protection_type, mending, unbreaking]))
    chestplate_enchantments.append(Item("minecraft:diamond_chestplate", name="Spiked Chestplate", color="red", 
                                        enchantments=[protection_type, thorns, mending, unbreaking]))
    
    leggings_enchantments.append(Item("minecraft:diamond_leggings", name="Perfect Leggings" , color="gold",
                    enchantments=[protection_type, swift_sneak, mending, unbreaking]))
    leggings_enchantments.append(Item("minecraft:diamond_leggings", name="Spiked Leggings", color="red",
                    enchantments=[protection_type, swift_sneak, thorns, mending, unbreaking]))
    
    boots_enchantments.append(Item("minecraft:diamond_boots", name="Perfect Walkers" , color="gold",
                    enchantments=[protection_type, frost_walker, feather_falling, soul_speed, mending, unbreaking]))
    boots_enchantments.append(Item("minecraft:diamond_boots", name="Spiked Walkers", color="red",
                    enchantments=[protection_type, frost_walker, feather_falling, soul_speed, thorns, mending, unbreaking]))
    boots_enchantments.append(Item("minecraft:diamond_boots", name="Perfect Striders", color="gold",
                    enchantments=[protection_type, depth_strider, feather_falling, soul_speed, mending, unbreaking]))
    boots_enchantments.append(Item("minecraft:diamond_boots", name="Spiked Striders", color="red",
                    enchantments=[protection_type, depth_strider, feather_falling, soul_speed, thorns, mending, unbreaking]))

for helmet in helmet_enchantments:
    helmet_master_table.append(VillagerTrade("diamond_helmet", ("emerald", 32), helmet))
for chestplate in chestplate_enchantments:
    chestplate_master_table.append(VillagerTrade("diamond_chestplate", ("emerald", 32), chestplate))
for leggings in leggings_enchantments:
    leggings_master_table.append(VillagerTrade("diamond_leggings", ("emerald", 32), leggings))
for boots in boots_enchantments:
    boots_master_table.append(VillagerTrade("diamond_boots", ("emerald", 32), boots))

helmet_master = Villager("Helmet Armorsmith", color="light_purple", profession="armorer", level=5, trades=helmet_master_table, ai=True)
chestplate_master = Villager("Chestplate Armorsmith", color="light_purple", profession="armorer", level=5, trades=chestplate_master_table, ai=True)
leggings_master = Villager("Leggings Armorsmith", color="light_purple", profession="armorer", level=5, trades=leggings_master_table, ai=True)
boots_master = Villager("Boots Armorsmith", color="light_purple", profession="armorer", level=5, trades=boots_master_table, ai=True)

# pet master
pet_master_table = []
pet_master_table.append(VillagerTrade(("emerald", 16),None, sell="saddle"))
pet_master_table.append(VillagerTrade(buy=("emerald", 16), sell=("lead", 4)))
pet_master_table.append(VillagerTrade(buy=("emerald", 20), sell=("name_tag", 1)))
pet_master_table.append(VillagerTrade(("leather_helmet"),("leather_chestplate"),("leather_horse_armor")))
pet_master_table.append(VillagerTrade(("golden_helmet"),("golden_chestplate"),("golden_horse_armor")))
pet_master_table.append(VillagerTrade(("iron_helmet"),("iron_chestplate"),("iron_horse_armor")))
pet_master_table.append(VillagerTrade(("diamond_helmet"),("diamond_chestplate"),("diamond_horse_armor")))
pet_master = Villager("Pet Master", color="light_purple", profession="butcher", level=5, trades=pet_master_table, ai=True)

# construction master
nature_master_table = []
nature = ["grass_block","podzol","mycelium","dirt","mud","clay","gravel","sand","red_sand","ice","snow_block",
          "moss_block","stone", "cobblestone","deepslate","cobbled_deepslate","blackstone","basalt","smooth_basalt","andesite","diorite","granite","calcite","tuff","dripstone_block",
          "prismarine","dark_prismarine","amethyst_block","lantern","soul_lantern"]
for block in nature:
    nature_master_table.append(VillagerTrade(("emerald"), None, sell=(block,16)))
nature_master = Villager("Nature Master", color="light_purple", type="jungle", profession="mason", level=5, trades=nature_master_table, ai=True)

flora_master_table = []
flora = ["oak_sapling","spruce_sapling","birch_sapling","jungle_sapling","acacia_sapling","dark_oak_sapling","mangrove_propagule","azalea","flowering_azalea",
         "warped_fungus","crimson_fungus","brown_mushroom","red_mushroom","sweet_berries","cactus","sugar_cane","bamboo","kelp",
         "vine","glow_lichen","wheat_seeds","beetroot_seeds","melon_seeds","pumpkin_seeds","nether_wart","carrot","potato","cocoa_beans","chorus_fruit"]
for block in flora:
    flora_master_table.append(VillagerTrade(("emerald"), None, sell=(block,16)))
flora_master = Villager("Flora Master", color="light_purple", type="jungle", profession="mason", level=5, trades=flora_master_table, ai=True)

color_master_table = []
colors = ["white","red","orange","pink","yellow","lime","green","cyan","light_blue","blue","purple","magenta","brown","black","gray","light_gray"]
items = ["_dye","_wool","_concrete","_concrete_powder","_terracotta","_glazed_terracotta","_stained_glass"]
for item in items:
    for color in colors:
        color_master_table.append(VillagerTrade(("emerald"), None, sell=(color+item,16)))

color_master = Villager("Color Master", color="light_purple", type="jungle", profession="mason", level=5, trades=color_master_table, ai=True)

redstone_master_table = []
redstone = ["redstone","redstone_torch","redstone_block","repeater","comparator","target","sculk_sensor","calibrated_sculk_sensor",
            "tripwire_hook","lectern","daylight_detector","lightning_rod","piston","sticky_piston","slime_block","honey_block","dispenser",
            "dropper","hopper","observer","note_block","tnt","redstone_lamp"]
for block in redstone:
    redstone_master_table.append(VillagerTrade(("emerald",16), None, sell=(block,32)))
redstone_master = Villager("Redstone Master", color="light_purple", type="jungle", profession="mason", level=5, trades=redstone_master_table, ai=True)

dj_master_table = []
music_discs = ["13","cat","blocks","chirp","far","mall","mellohi","stal","strad","ward","11","wait","otherside","5","pigstep","relic"]
dj_master_table.append(VillagerTrade(("emerald",4), None, sell=("jukebox",1)))
for disc in music_discs:
    dj_master_table.append(VillagerTrade(("emerald",4), None, sell=("music_disc_"+disc,1)))
dj_master = Villager("DJ Master", color="light_purple", type="jungle", profession="mason", level=5, trades=dj_master_table, ai=True)

# tools 

tool_master_table = []

for tool in ["diamond_pickaxe","diamond_axe","diamond_shovel","diamond_hoe"]:
    tool_master_table.append(VillagerTrade(tool,("emerald", 32), sell=Item(tool,"Perfect Silk", color="light_purple", enchantments=[efficiency, silk_touch, unbreaking, mending])))
    tool_master_table.append(VillagerTrade(tool,("emerald", 32), sell=Item(tool,"Perfect Fortune", color="gold", enchantments=[efficiency, fortune, unbreaking, mending])))
for enchant in [sharpness, smite, bane_of_arthropods]:
    enchant_name = enchant.name().split(":")[1].capitalize().replace("_"," ")
    tool_master_table.append(VillagerTrade("diamond_sword",("emerald", 32), sell=Item("diamond_sword","Perfect "+enchant_name, color="gold", enchantments=[enchant,looting, fire_aspect, knockback, sweeping_edge, unbreaking, mending])))
for enchant in [infinity, mending]:
    enchant_name = enchant.name().split(":")[1].capitalize()
    tool_master_table.append(VillagerTrade("bow",("emerald", 32), sell=Item("bow","Perfect "+enchant_name, color="gold", enchantments=[enchant, power, punch, flame, unbreaking])))
tool_master_table.append(VillagerTrade("crossbow",("emerald", 32), sell=Item("crossbow","Perfect Quickdraw", color="gold", enchantments=[quick_charge, multishot, unbreaking, mending])))
tool_master_table.append(VillagerTrade("trident",("emerald", 32), sell=Item("trident","Perfect Aquatic", color="aqua", enchantments=[riptide, impaling, unbreaking, mending])))
tool_master_table.append(VillagerTrade("trident",("emerald", 32), sell=Item("trident","Perfect Storm", color="blue", enchantments=[channeling, loyalty, impaling,unbreaking, mending])))
tool_master = Villager("Tool Master", color="light_purple", profession="toolsmith", level=5, trades=tool_master_table, ai=True)


emerald_master_table = []
emerald_master_table.append(VillagerTrade(("stick",32), None, sell=("emerald",1)))
emerald_master = Villager("Emerald Master", color="light_purple", profession="fletcher", level=5, trades=emerald_master_table, ai=True)


axe = Item("diamond_shovel","Tragic Allium", "dark_purple", enchantments=[efficiency,silk_touch,unbreaking, mending])
print(axe.give_item())
pyperclip.copy(axe.give_item())
give @p diamond_shovel{display:{Name:'{"text":"Tragic Allium", "color":"dark_purple"}'},Damage:449, Enchantments:[{lvl:5s, id:"minecraft:efficiency"},{lvl:1s, id:"minecraft:silk_touch"},{lvl:3s, id:"minecraft:unbreaking"},{lvl:1s, id:"minecraft:mending"}]}