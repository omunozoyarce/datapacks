import pyperclip
from villager_trade import VillagerTrade, Item, Enchantment
from random import randint

class Villager():
    

    def __init__(self, name: str, color: str = None, type: str = None, profession: str = None, 
                 level: int = None, persistent: bool = True, trades: list = [], ai: bool = True):
        vanilla_colors = ("dark_red, red, gold, yellow, dark_green, green, aqua, dark_aqua, dark_blue, blue, light_purple, dark_purple, white, gray, dark_gray, black").split(", ")
        if color:
            if color in vanilla_colors or color == "random":
                if color == "random":
                    color = vanilla_colors[randint(0, 15)]
                self.name = f"CustomName:'{{\"text\":\"{name}\", \"color\":\"{color}\"}}'"
            else:
                self.name = f"CustomName:'{{\"text\":\"{name}\"}}'"
        elif name:
            self.name = f"CustomName:'{{\"text\":\"{name}\"}}'"
        else:
            self.name = None
        self.type = type if type != None else "plains"
        self.profession = profession if profession != None else None
        self.level = level if level != None else 0
        ''' Vanilla type table:
        desert, jungle, plains, savanna, snow, swamp, taiga'''
        
        ''' Vanilla profession table:
        armorer, butcher, cartographer, cleric, farmer, 
        fisherman, fletcher, leatherworker, librarian, 
        mason, nitwit, shepherd, toolsmith, weaponsmith'''
        
        ''' Vanilla color table:
        dark_red, red, gold, yellow, dark_green, green,
        aqua, dark_aqua, dark_blue, blue, light_purple,
        dark_purple, white, gray, dark_gray, black'''
        self.persistent = "PersistenceRequired:1" if persistent else "PersistenceRequired:0"
        self.trades = trades
        if self.profession != None:
            self.villager_data = f"VillagerData:{{type:{self.type},profession:{self.profession},level:{self.level}}}"
        else:
            self.villager_data = f"VillagerData:{{type:{self.type}}}"
        self.ai = "NoAI:1b" if not ai else ""
    
    def give_spawn_egg(self):
        if self.name:
            if self.ai:
                return f"give @p minecraft:villager_spawn_egg{{EntityTag:{{{self.name},{self.villager_data},{self.persistent},Offers:{{Recipes:{self.trades}}},{self.ai}}}}} 1"
            return f"give @p minecraft:villager_spawn_egg{{EntityTag:{{{self.name},{self.villager_data},{self.persistent},Offers:{{Recipes:{self.trades}}}}}}} 1"
        if self.ai:
            return f"give @p minecraft:villager_spawn_egg{{EntityTag:{{{self.villager_data},{self.persistent},Offers:{{Recipes:{self.trades}}},{self.ai}}}}} 1"
        return f"give @p minecraft:villager_spawn_egg{{EntityTag:{{{self.villager_data},{self.persistent},Offers:{{Recipes:{self.trades}}}}}}} 1"
    
    def summon(self):
        if self.name:
            if self.ai:
                return f"summon minecraft:villager ~ ~1 ~ {{{self.name},{self.villager_data},{self.persistent},Offers:{{Recipes:{self.trades}}},{self.ai}}}"
            return f"summon minecraft:villager ~ ~1 ~ {{{self.name},{self.villager_data},{self.persistent},Offers:{{Recipes:{self.trades}}}}}"
        if self.ai:
            return f"summon minecraft:villager ~ ~1 ~ {{{self.villager_data},{self.persistent},Offers:{{Recipes:{self.trades}}},{self.ai}}}"
        return f"summon minecraft:villager ~ ~1 ~ {{{self.villager_data},{self.persistent},Offers:{{Recipes:{self.trades}}}}}"



    def __str__(self):
        return f'''{{profession:{self.profession},
level:{self.level},
type:{self.type},
PersistenceRequired:1,
Offers:{{Recipes:[{self.offers}]}}}}
'''



if __name__ == "__main__":
    # enchanted_book = Item("minecraft:enchanted_book", name="sex 2",  enchantments = [Enchantment("minecraft:sharpness", 5), Enchantment("minecraft:unbreaking", 3),
    #                                                                   Enchantment("minecraft:looting", 3), Enchantment("minecraft:fire_aspect", 2),
    #                                                                   Enchantment("minecraft:knockback", 2), Enchantment("minecraft:mending", 1)])
    # trade = VillagerTrade("emerald", None, enchanted_book)
    villager = Villager("Papa Meat", "red", "plains", "armorer", None, True, None, False)
    pyperclip.copy(villager.summon())
    
    # summon minecraft:villager ~ ~1 ~ {CustomName:'{"text":"Papa Meat", "color":"red"}',PersistenceRequired:1,Offers:{Recipes:None},NoAI:1b}