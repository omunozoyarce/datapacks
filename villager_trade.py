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