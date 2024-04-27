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


class Villager():

    def __init__(self, villager):
        self.villager = villager
        self.profession = None
        self.level = None
        # self.type = None{EntityTag:{VillagerData:{type:plains,profession:farmer,level:2},Offers:{Recipes:[{maxUses:1,buy:{id:acacia_button,Count:1},buyB:{id:acacia_door,Count:1}}]}}} 1

class VillagerTrade():
    
    def __init__(self, buy: tuple, sell: str, reward_exp: int = 0, max_uses: int = 9999999):
        self.buy = buy[0]
        self.buyB = buy[1]
        '''
        The format of self.buy is a tuple with len(buy) == 2
        buy[0] is the first item, buy[1] is the second item
        buy[0] and buy[1] are both tuples with len(buy[0]) == 2 and len(buy[1]) == 2
        buy[0][0] is the item id, buy[0][1] is the item count
        buy[1][0] is the item id, buy[1][1] is the item count
        '''
        self.sell = sell
        self.rewardExp = reward_exp
        self.maxUses = max_uses
        
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
    item = Item("minecraft:enchanted_book", True, "efficiency")