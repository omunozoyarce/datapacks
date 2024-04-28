import pyperclip
from villager_trade import VillagerTrade
from random import randint

class Villager():
    

    def __init__(self, name: str, color: str = None, type: str = None, profession: str = None, level: int = None, persistent: bool = True, trades: list = [], ai: bool = True):
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
        self.profession = profession if profession != None else "farmer"
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
        self.villager_data = f"VillagerData:{{type:{self.type},profession:{self.profession},level:{self.level}}}"
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
    trades = [VillagerTrade(("diamond_hoe"), ("tnt"), ("ice")), VillagerTrade(("bow"),None, ("arrow"))]
    villager = Villager("bob", "cafa", level=2, persistent=True, trades=trades, ai=False)
    egg = (villager.summon())
    print(egg)
    pyperclip.copy(egg)