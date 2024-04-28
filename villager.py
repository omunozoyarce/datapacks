# give @p villager_spawn_egg nbt:
# {EntityTag:{VillagerData:{type:plains,profession:farmer,level:2},Offers:{Recipes:[{maxUses:1,buy:{id:acacia_button,Count:1},buyB:{id:acacia_door,Count:1}}]}}} 1
import pyperclip

class Villager():

    def __init__(self, name: str, type: str, profession: str, level: int, persistent: bool = True, trades: list = []):
        self.name = f"CustomName:'[{{\"text\":\"{name}\"}}]'" if name else None
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
        self.persistent = "PersistenceRequired:1" if persistent else "PersistenceRequired:0"
        self.trades = trades
        self.villager_data = f"VillagerData:{{type:{self.type},profession:{self.profession},level:{self.level}}}"
    
    def give_spawn_egg(self):
        return f"give @p villager_spawn_egg{{EntityTag:{{{self.name},{self.villager_data},{self.persistent}}}}} 1"

    def __str__(self):
        return f'''{{profession:{self.profession},
level:{self.level},
type:{self.type},
PersistenceRequired:1,
Offers:{{Recipes:[{self.offers}]}}}}
'''



if __name__ == "__main__":
    villager = Villager("bob", "jungle", "fisherman", 2)
    print(villager.give_spawn_egg())
    
    pyperclip.copy(villager.give_spawn_egg())

