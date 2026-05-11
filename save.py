import json

from characters import Archer, Mage, Warior
from items import HEALTH_POTION, BIG_HEALTH_POTION, POISON_POTION, BIG_POISON_POTION
from config import SAVE_PATH

CLASSES = {
    "Warior": Warior,
    "Mage": Mage,
    "Archer": Archer,
}

ITEMS = {
    HEALTH_POTION.name: HEALTH_POTION,
    BIG_HEALTH_POTION.name: BIG_HEALTH_POTION,
    POISON_POTION.name: POISON_POTION,
    BIG_POISON_POTION.name: BIG_POISON_POTION,   
}

def save_hero(hero, path=SAVE_PATH):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(hero.to_dict(), f, ensure_ascii=False, indent=2)    
    
    
def load_hero(path=SAVE_PATH):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    cls = CLASSES[data['class']]
    hero = cls.from_dict(data)
    for name in data.get('inventory', []):
        if name in ITEMS:
            hero.inventory.add_item(ITEMS[name])
    return hero