from abc import ABC, abstractmethod
from random import randint
from inventory import Inventory
from logger import logger
class Character(ABC):
    _hp = 100
    max_hp = 150
    damage = 20
    
    def __init__(self, name):
        self.inventory = Inventory()
        self.name = name
        self._gold = 0
        self.level = 1
        self.xp = 0
        self.xp_threshold = 100
    
    def is_alive(self):
        return self.hp > 0
        
    def take_damage(self, amount):
        self.hp -= amount
        
    @property
    def hp(self):   
        return self._hp

    @hp.setter
    def hp(self, value):
        # _hp in [0, max_hp]
        self._hp = max(0, min(self.max_hp, value))
        
    @property
    def gold(self):   
        return self._gold

    @gold.setter
    def gold(self, value):
        self._gold = max(0, value)
        
    def gain_xp(self, amount):
        self.xp += amount
        if self.xp >= self.xp_threshold:
            self.level_up()
            
    def level_up(self):
        self.level += 1
        self.max_hp += 20
        self.hp = self.max_hp
        self.damage += 5
        self.xp_threshold = int(self.xp_threshold * 1.5)
        logger.log_level_up(self)
        
    def to_dict(self):
        return {
            "class": self.__class__.__name__,
            "name": self.name,
            "level": self.level,
            "xp":  self.xp,
            "xp_threshold": self.xp_threshold,
            "gold": self.gold,
            "damage": self.damage,
            "hp": self.hp,
            "max_hp": self.max_hp,
            "inventory": [item.name for item in self.inventory.items],
        }
        
    @classmethod
    def from_dict(cls, data):
        hero = cls(data['name'])
        hero.level = data['level']
        hero.xp = data['xp']
        hero.xp_threshold = data["xp_threshold"]
        hero.gold = data["gold"]
        hero.damage = data['damage']
        hero.max_hp = data["max_hp"]
        hero.hp = data["hp"]
        return hero
    
    def __str__(self):
        # "'Артур' [HP 100/120]"
        return f"'{self.name}' [HP {self._hp} / {self.max_hp}]"
        
    @abstractmethod
    def attack(self, target: Character) -> int:
        pass
    
class Warior(Character):
    _hp = 145
    damage = 20
    armour = 5
    max_hp = 170
    
    def take_damage(self, amount):
        real_amount = max(0, amount - self.armour)
        
        super().take_damage(real_amount)
    
    def attack(self, target: Character) -> int:
        target.take_damage(self.damage)
        return self.damage
    
class Mage(Character):
    _hp = 70
    damage = 30
    counter_attack = 0
    max_hp = 120
    
    def attack(self, target: Character) -> int:
        self.counter_attack += 1
        amount = self.damage * 3 if self.counter_attack % 3 == 0 else self.damage
        target.take_damage(amount)
        return amount

class Archer(Character):
    _hp = 90
    damage = 15
    max_hp = 140
    
    def attack(self, target: Character) -> int:
        target.take_damage(self.damage)
        
        if randint(0, 1):
            target.take_damage(self.damage)
            return self.damage * 2

        return self.damage
    