import pyperclip
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



class Item():
    def __init__(self, id: str, name: str = None, color : str = None, enchantments: list = []):
        self.id = id 
        
        if color:
            if name:
                self.name = f"display:{{Name:'{{\"text\":\"{name}\", \"color\":\"{color}\"}}'}}"
            else:
                self.name = f"display:{{Name:'{{\"color\":\"{color}\"}}'}}"
        elif name:
            self.name = f"display:{{Name:'{{\"text\":\"{name}\"}}'}}"
        else:
            self.name = None
        
        self.enchantments = enchantments
        
        if enchantments != []:
            if self.id == "minecraft:enchanted_book":
                if type(self.enchantments) == Enchantment:
                    self.enchantments = f"StoredEnchantments:[{self.enchantments}]"
                else:
                    self.enchantments = f"StoredEnchantments:[{','.join(str(enchantment) for enchantment in self.enchantments)}]"
            else:
                if type(self.enchantments) == Enchantment:
                    self.enchantments = f"Enchantments:[{self.enchantments}]"
                else:
                    self.enchantments = f"Enchantments:[{','.join(str(enchantment) for enchantment in self.enchantments)}]"
    
    def give_item(self):
        if self.enchantments == [] and self.name != None:
            return f"give @p {self.id}{{{self.name}}}"
        elif self.enchantments == [] and self.name == None:
            return f"give @p {self.id}"
        elif self.enchantments != [] and self.name != None:
            return f"give @p {self.id}{{{self.name}, {self.enchantments}}}"
        elif self.enchantments != [] and self.name == None:
            return f"give @p {self.id}{{{self.enchantments}}}"
    
    def __repr__(self):
        if self.enchantments == [] and self.name != None:
            return f"{{id:{self.id},name:{self.name}}}"
        elif self.enchantments == [] and self.name == None:
            return f"{{id:{self.id}}}"
        elif self.enchantments != [] and self.name != None:
            return f"{{id:{self.id},name:{self.name},enchantments:{self.enchantments}}}"
        elif self.enchantments != [] and self.name == None:
            return f"{{id:{self.id},enchantments:{self.enchantments}}}"

    def tag(self, count = 1):
        if self.enchantments == [] and self.name != None:
            return f"{{id:\"{self.id}\",Count:{count},tag:{{{self.name}}}}}"
        elif self.enchantments == [] and self.name == None:
            return f"{{id:\"{self.id}\",Count:{count}}}"
        elif self.enchantments != [] and self.name == None:
            return f"{{id:\"{self.id}\",Count:{count},tag:{{{self.enchantments}}}}}"
        elif self.enchantments != [] and self.name != None:
            return f"{{id:\"{self.id}\",Count:{count},tag:{{{self.name}, {self.enchantments}}}}}"



class Enchantment(): 
    def __init__(self, id: str, level: int = 1):
        self.id = id
        self.level = level
    def __str__(self):
        return f'{{lvl:{self.level}s, id:"{self.id}"}}'



class VillagerTrade():
    def __init__(self, buy: tuple = None, buy_B: tuple = None, sell: tuple = None, reward_exp: int = 0, max_uses: int = 9999999):
        self.rewardExp = reward_exp
        self.maxUses = max_uses
        
        if type(buy) == tuple:
            if type(buy[0]) == Item:
                self.buy = buy[0].tag(buy[1])
            elif type(buy[0]) == str:
                self.buy = f"{{id:{buy[0]},Count:{buy[1]}}}"
        
        elif type(buy) == str:
            self.buy = f"{{id:{buy},Count:1}}"
        
        elif type(buy) == Item:
            self.buy = buy.tag()
        
        if buy_B:
            if type(buy_B) == tuple:
                if type(buy_B[0]) == Item:
                    self.buyB = buy_B[0].tag(buy_B[1])
                elif type(buy_B[0]) == str:
                    self.buyB = f"{{id:{buy_B[0]},Count:{buy_B[1]}}}"
            elif type(buy_B) == str:
                self.buyB = f"{{id:{buy_B},Count:1}}"
        else:
            self.buyB = None
        
        if type(sell) == tuple:
            if type(sell[0]) == Item:
                self.sell = sell[0].tag(sell[1])
            elif type(sell[0]) == str:
                self.sell = f"{{id:{sell[0]},Count:{sell[1]}}}"
        elif type(sell) == str:
            self.sell = f"{{id:{sell},Count:1}}"
        elif type(sell) == Item:
            self.sell = sell.tag()
        
    def __repr__(self):
        if self.buyB == None:
            return f"{{buy:{self.buy},sell:{self.sell},rewardExp:{self.rewardExp}b,maxUses:{self.maxUses}}}"
        return f"{{buy:{self.buy},buyB:{self.buyB},sell:{self.sell},rewardExp:{self.rewardExp}b,maxUses:{self.maxUses}}}"



if __name__ == "__main__":
    item = Item("minecraft:dirt", "fart", color = "gold")
    pyperclip.copy(item.give_item())