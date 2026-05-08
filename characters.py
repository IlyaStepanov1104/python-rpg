from abc import ABC, abstractmethod
from random import randint
from inventory import Inventory

class Character(ABC):
    _hp = 100
    max_hp = 150
    damage = 20
    
    def __init__(self, name):
        self.inventory = Inventory()
        self.name = name
    
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
        
    def __str__(self):
        # "'Артур' [HP 100/120]"
        return f"'{self.name}' [HP {self._hp} / {self.max_hp}]"
        
    @abstractmethod
    def attack(self, target: Character) -> int:
        pass
    
class Warior(Character):
    _hp = 120
    damage = 20
    armour = 5
    
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
    
    def attack(self, target: Character) -> int:
        self.counter_attack += 1
        amount = self.damage * 3 if self.counter_attack % 3 == 0 else self.damage
        target.take_damage(amount)
        return amount

class Archer(Character):
    _hp = 90
    damage = 15
    
    def attack(self, target: Character) -> int:
        target.take_damage(self.damage)
        
        if randint(0, 1):
            target.take_damage(self.damage)
            return self.damage * 2

        return self.damage
    