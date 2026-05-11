import os
from characters import Archer, Mage, Warior
from config import SAVE_PATH
from fight import fight
from items import HEALTH_POTION, POISON_POTION
from logger import logger
from tavern import tavern
from save import save_hero, load_hero

def get_hero():
    if os.path.exists(SAVE_PATH):
        choice = input("Найдено сохранение. Загрузить? (y/n): ").strip()
        if choice == "y":
            return load_hero(SAVE_PATH)
    
    # TODO: HW - Сделать выбор персонажа и ввод имени через input
    hero = Warior("Артур")
    hero.inventory.add_item(HEALTH_POTION)
    hero.inventory.add_item(POISON_POTION)
    return hero

ENEMY_LIST = [
    Warior('Алекс'),
    Archer("Робин Гуд"),
    Mage("Мерлин"),
]

hero = get_hero()

for enemy in ENEMY_LIST:
    save_hero(hero)
    winner = fight(hero, enemy)
    if not hero.is_alive():
        logger.log_death(hero)
        break
    tavern(hero)