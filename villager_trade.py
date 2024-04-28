import pyperclip

class Item():
    def __init__(self, id: str, name: str = None, enchantments: list = []):
        self.id = id 
        self.name = f"display:{{Name:'{{\"text\":\"{name}\"}}'}}" if name else None        
        self.enchantments = enchantments
        self.enchantments = f"Enchantments:[{','.join(str(enchantment) for enchantment in self.enchantments)}]"
    def __str__(self):
        if self.enchantments == "Enchantments:[]":
            return f"give @p {self.id}{{{self.name}}}"
        return f"give @p {self.id}{{{self.name},{self.enchantments}}}"

class VillagerTrade():
    def __init__(self, buy: Item = None, buy_B: Item = None, sell: Item = None, reward_exp: int = 0, max_uses: int = 9999999):
        self.buy = buy if buy else None
        self.buyB = buy_B if buy_B else None
        self.sell = sell if sell else None
        self.rewardExp = reward_exp
        self.maxUses = max_uses
    
    def __str__(self):
        return str((self.buy, self.buyB, self.sell, self.rewardExp, self.maxUses))





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
    def __init__(self, id: str, level: int):
        self.id = id
        self.level = level
    def __str__(self):
        return f'{{lvl: {self.level}s, id: "{self.id}"}}'
enchantments = [
    Enchantment("minecraft:protection", 3),
    Enchantment("minecraft:aqua_affinity", 1)
]

item_1 = Item("minecraft:diamond_helmet", "Helm. Prot")
item_2 = Item("minecraft:enchanted_book", "Helm. Prot", enchantments)
print(item_1)
print(item_2)

trade = VillagerTrade(item_1, item_2, 1, 0)
print(trade)