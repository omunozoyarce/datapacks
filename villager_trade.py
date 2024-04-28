import pyperclip
from pprint import pprint

class Item():
    def __init__(self, id: str, name: str = None, color : str = None, enchantments: list = []):
        self.id = id 
        
        if name and color:
            self.name = f"display:{{Name:'{{\"text\":\"{name}\", \"color\":\"{color}\"}}'}}"
        elif name and not color:
            self.name = f"display:{{Name:'{{\"text\":\"{name}\"}}'}}" if name else None        
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
        elif self.enchantments != [] and self.name == None:
            return f"give @p {self.id}{{{self.enchantments}}}"
        elif self.enchantments == [] and self.name == None:
            return f"give @p {self.id}"
        return f"give @p {self.id}{{{self.name}, {self.enchantments}}}"
    
    def __repr__(self):
        if self.enchantments == [] and self.name != None:
            return f"{{id:{self.id},name:{self.name}}}"
        elif self.enchantments != [] and self.name == None:
            return f"{{id:{self.id},{self.enchantments}}}"
        elif self.enchantments == [] and self.name == None:
            return f"{{id:{self.id}}}"
        return f"{{id:{self.id},name:{self.name},{self.enchantments}}}"
    
    def tag(self, count = 1):
        if self.enchantments == [] and self.name != None:
            return f"{{id:\"{self.id}\",Count:{count},tag:{{{self.name}}}}}"
        if self.enchantments != [] and self.name == None:
            return f"{{id:\"{self.id}\",Count:{count},tag:{{{self.enchantments}}}}}"
        if self.enchantments == [] and self.name == None:
            return f"{{id:\"{self.id}\",Count:{count}}}"
        return f"{{id:\"{self.id}\",Count:{count},tag:{{{self.name}, {self.enchantments}}}}}"
        
# {id:"bookshelf",Count:1,tag:{display:{Name:'{"text":"Fart", "color":"blue"}'}}}

# /give @p villager_spawn_egg
# {EntityTag:
# {VillagerData:
# {type:plains,profession:farmer,level:2},
# 
# Offers:{Recipes:[{buy:{id:book,Count:1},sell:{id:emerald,Count:1}}]},CustomName:'[{"text":"bob"}]'}} 1

# Offers: 
#                     {Recipes: 
#                         [{maxUses: 2147483647, 
#                             buyB: {id: "minecraft:emerald", Count: 16b}, 
#                             buy: {id: "minecraft:diamond_helmet", Count: 1b, tag: {Damage: 0}}, 
#                             sell: {id: "minecraft:enchanted_book", Count: 1b, tag: {RepairCost: 7, 
#                             StoredEnchantments: 
#                                 [{lvl: 3s, id: "minecraft:respiration"}, 
#                                 {lvl: 1s, id: "minecraft:aqua_affinity"}, 
#                                 {lvl: 4s, id: "minecraft:protection"}, 
#                                 {lvl: 3s, id: "minecraft:unbreaking"}, 
#                                 {lvl: 1s, id: "minecraft:mending"}], 
#                             display: {Name: '{"text":"Helm. Prot."}'}}}, 
#                             xp: 1, 
#                             uses: 0, 
#                             priceMultiplier: 0.0f, 
#                             specialPrice: 0, 
#                             demand: 0, 
#                             rewardExp: 1b}]}


class Enchantment(): 
    def __init__(self, id: str, level: int = 1):
        self.id = id
        self.level = level
    def __str__(self):
        return f'{{lvl:{self.level}s, id:"{self.id}"}}'



class VillagerTrade():
    def __init__(self, buy: Item = None, buy_B: Item = None, sell: Item = None, reward_exp: int = 0, max_uses: int = 9999999):
        self.buy = buy if buy else None
        self.buyB = buy_B if buy_B else None
        self.sell = sell if sell else None
        self.rewardExp = reward_exp
        self.maxUses = max_uses
    
    def give_spawn_egg(self):
        return




item = Item("minecraft:diamond_hoe", "Fart", "blue", [Enchantment("minecraft:sharpness", 1), Enchantment("minecraft:unbreaking", 2)])
pyperclip.copy(item.tag())
print(item.tag())

# give @p minecraft:villager_spawn_egg{display:{Name:'{"text":"Fart", "color":"blue"}'}}
# /give @p villager_spawn_egg{EntityTag:{VillagerData:{type:plains,profession:farmer,level:2},Offers:{Recipes:[{buy:{id:"minecraft:diamond_hoe",Count:1,tag:{display:{Name:'{"text":"Fart", "color":"blue"}'}, Enchantments:[{lvl:1s, id:"minecraft:sharpness"},{lvl:2s, id:"minecraft:unbreaking"}]}},sell:{id:emerald,Count:1}}]},CustomName:'[{"text":"bob"}]'}} 1

# give @p minecraft:acacia_boat{display:{Name:'{"text":"Tunic of Destiny", "color":"blue"}'}} this one works
# give @p minecraft:acacia_boat{display:{Name:'{"text":"Tunic of Destiny", "color":"blue"}',Lore:['{"text":"Fart"}']}} 
# give @p minecraft:acacia_boat{display:{Name:'{"text":"Tunic of Destiny","color":"blue"}

# give @p minecraft:acacia_boat{display:{Name:'{"text":"My love for my wife Yvain <3"}, color:16777215}'}
# give @p minecraft:acacia_boat{display:{Name:'{"text":"My love for my wife Yvain <3", color:16777215}'}}