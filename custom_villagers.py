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

swift_sneak = Enchantment("minecraft:swift_sneak", 1)

depth_strider = Enchantment("minecraft:depth_strider", 3)
frost_walker = Enchantment("minecraft:frost_walker", 2)
feather_falling = Enchantment("minecraft:feather_falling", 4)
soul_speed = Enchantment("minecraft:soul_speed", 3)

# items
# armor order: protection, exclusive, thorns, standard (mending, unbreaking)

# helmet enchantments
helmet_enchantments, helmet_master_table = [], []
chestplate_enchantments, chestplate_master_table = [], []
leggings_enchantments, leggings_master_table = [], []
boots_enchantments, boots_master_table = [], []

for protection_type in [protection, fire_protection, blast_protection, projectile_protection]:
    helmet_enchantments.append(Item("minecraft:enchanted_book", name="Perfect Helmet" , color="gold", 
                                    enchantments=[protection_type, respiration, aqua_affinity, mending, unbreaking]))
    helmet_enchantments.append(Item("minecraft:enchanted_book", name="Spiked Helmet", color="red", 
                                    enchantments=[protection_type, respiration, aqua_affinity, thorns, mending, unbreaking]))
    
    chestplate_enchantments.append(Item("minecraft:enchanted_book", name="Perfect Chestplate" , color="gold", 
                                        enchantments=[protection_type, mending, unbreaking]))
    chestplate_enchantments.append(Item("minecraft:enchanted_book", name="Spiked Chestplate", color="red", 
                                        enchantments=[protection_type, thorns, mending, unbreaking]))
    
    leggings_enchantments.append(Item("minecraft:enchanted_book", name="Perfect Leggings" , color="gold",
                    enchantments=[protection_type, swift_sneak, mending, unbreaking]))
    leggings_enchantments.append(Item("minecraft:enchanted_book", name="Spiked Leggings", color="red",
                    enchantments=[protection_type, swift_sneak, thorns, mending, unbreaking]))
    
    boots_enchantments.append(Item("minecraft:enchanted_book", name="Perfect Walkers" , color="gold",
                    enchantments=[protection_type, frost_walker, feather_falling, soul_speed, mending, unbreaking]))
    boots_enchantments.append(Item("minecraft:enchanted_book", name="Spiked Walkers", color="red",
                    enchantments=[protection_type, frost_walker, feather_falling, soul_speed, thorns, mending, unbreaking]))
    boots_enchantments.append(Item("minecraft:enchanted_book", name="Perfect Striders", color="gold",
                    enchantments=[protection_type, depth_strider, feather_falling, soul_speed, mending, unbreaking]))
    boots_enchantments.append(Item("minecraft:enchanted_book", name="Spiked Striders", color="red",
                    enchantments=[protection_type, depth_strider, feather_falling, soul_speed, thorns, mending, unbreaking]))

for helmet in helmet_enchantments:
    helmet_master_table.append(VillagerTrade("diamond_helmet", ("emerald", 16), helmet))
for chestplate in chestplate_enchantments:
    chestplate_master_table.append(VillagerTrade("diamond_chestplate", ("emerald", 16), chestplate))
for leggings in leggings_enchantments:
    leggings_master_table.append(VillagerTrade("diamond_leggings", ("emerald", 16), leggings))
for boots in boots_enchantments:
    boots_master_table.append(VillagerTrade("diamond_boots", ("emerald", 16), boots))

helmet_master = Villager("Helmet Armorsmith", color="light_purple", profession="armorer", level=5, trades=helmet_master_table, ai=False)
chestplate_master = Villager("Chestplate Armorsmith", color="light_purple", profession="armorer", level=5, trades=chestplate_master_table, ai=False)
leggings_master = Villager("Leggings Armorsmith", color="light_purple", profession="armorer", level=5, trades=leggings_master_table, ai=False)
boots_master = Villager("Boots Armorsmith", color="light_purple", profession="armorer", level=5, trades=boots_master_table, ai=False)

# input("Press enter to copy to clipboard")
# pyperclip.copy(helmet_master.summon())
# print("Copied Helmet Master to clipboard")

# input("Press enter to copy to clipboard")
# pyperclip.copy(chestplate_master.summon())
# print("Copied Chestplate Master to clipboard")

# input("Press enter to copy to clipboard")
# pyperclip.copy(leggings_master.summon())
# print("Copied Leggings Master to clipboard")

# input("Press enter to copy to clipboard")
# pyperclip.copy(boots_master.summon())
# print("Copied Boots Master to clipboard")

