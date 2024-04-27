# summon villager ~ ~1 ~ 
# {VillagerData:
#     {profession:farmer,
#      level:2,
#      type:plains},
#     PersistenceRequired:1,
#     Offers:{Recipes:[{buy:{id:acacia_boat,Count:1},sell:{id:acacia_chest_boat,Count:1},rewardExp:0b,maxUses:9999999}]}}

#egg
# give @p villager_spawn_egg nbt:
# {EntityTag:{VillagerData:{type:plains,profession:farmer,level:2},Offers:{Recipes:[{maxUses:1,buy:{id:acacia_button,Count:1},buyB:{id:acacia_door,Count:1}}]}}} 1
import pyperclip

class Villager():

    def __init__(self, name: str, type: str, profession: str, level: int, offers: list = [], persistent: bool = True):
        self.name = "CustomName:'[{\"text\":" + "\"" + name + "\"}]'" + "}"
        # identifiers = {type:str,profession:str,level:int}
        self.type = type if type else "plains"
        self.profession = profession if profession else "farmer"
        self.level = level if level else 1
        ''' Vanilla type table:
        desert, jungle, plains, savanna, snow, swamp, taiga'''
        
        ''' Vanilla profession table:
        armorer, butcher, cartographer, cleric, farmer, 
        fisherman, fletcher, leatherworker, librarian, 
        mason, nitwit, shepherd, toolsmith, weaponsmith
        '''
        self.identifiers = {"type":self.type, "profession":self.profession, "level":self.level}
        self.offers = offers
        persistent = 1 if persistent else 0
        # format {EntityTag:{VillagerData:{identifiers}}

        # Offers:{Recipes:[{maxUses:1,buy:{id:acacia_button,Count:1},buyB:{id:acacia_door,Count:1}}]}}} 1

    def give_spawn_egg(self):
        return "give @p villager_spawn_egg{EntityTag:{"+ str(self.name) + "}"

#         return f'give @p villager_spawn_egg{{EntityTag:{{  ,VillagerData:{self.identifiers},
# Offers:{{Recipes:[{self.offers}]}}}},}} 1'
    

    
    def __str__(self):
        return f'''{{profession:{self.profession},
level:{self.level},
type:{self.type},
PersistenceRequired:1,
Offers:{{Recipes:[{self.offers}]}}}}
'''


class VillagerTrade():
    
    def __init__(self, buy: tuple, sell: str, reward_exp: int = 0, max_uses: int = 9999999):
        self.buy = buy[0] if buy else None
        self.buyB = buy[1] if buy else None
        '''
        The format of self.buy is a tuple with len(buy) == 2
        buy[0] is the first item, buy[1] is the second item
        buy[0] and buy[1] are both tuples with len(buy[0]) == 2 and len(buy[1]) == 2
        buy[0][0] is the item id, buy[0][1] is the item count
        buy[1][0] is the item id, buy[1][1] is the item count
        '''
        self.sell = sell if sell else None
        self.rewardExp = reward_exp
        self.maxUses = max_uses
    def give_spawn_egg(self):
        return f'give @p villager_spawn_egg{{EntityTag:{{VillagerData:{{type:plains,profession:farmer,level:2}},Offers:{{Recipes:[{self}]}}}}}} 1'
        
    def __str__(self):
        return f'''{{maxUses: {self.maxUses}, 
buyB: {self.buyB[0] if self.buyB else None}, 
buyBQuantity: {self.buyB[1] if self.buyB else 1}, 
buy: {self.buy[0] if self.buy else None}, 
buyQuantity: {self.buy[1] if self.buy else 1},
sell: {self.sell}, 
rewardExp: {self.rewardExp}b}}
'''
class Item():
        def __init__(self, id: str, is_enchanted=False, enchantments=None):
            self.id = id 
            self.is_enchanted = is_enchanted
            self.enchantments = enchantments if is_enchanted else None
    
        def __str__(self):
            return f'''{{id: "{self.id}",
Count: 1b,
tag: {self.enchantments if self.is_enchanted else None}}}
'''

if __name__ == "__main__":
    villager = Villager("Bob", "jungle", "fisherman", 2)
    print(villager.give_spawn_egg())
    print("give @p rabbit_spawn_egg{EntityTag:{CustomName:" + "\'[{\"text\":\"bob\"}]\'}} 1")
    
    pyperclip.copy(villager.give_spawn_egg())

