from random import randint
from characters import Character
from config import FIGHT_LIMIT
from logger import logger


def player_turn(hero, enemy):
    print(f"\n=== Твой ход ===")
    # TODO: вынести в logger
    print(f"{hero.name}: HP {hero.hp}/{hero.max_hp} | Инвентарь: {hero.inventory}")
    print(f"{enemy.name}: HP {enemy.hp}/{enemy.max_hp}")
    print()
    print("[1] Атаковать")
    if hero.inventory.items:
        print("[2] Использовать предмет")
        
    choice = input("Выбор: ").strip()
    
    if choice == "2" and hero.inventory.items:
        for i in range(len(hero.inventory.items)):
            print(f"  [{i}] {hero.inventory.items[i]}")
        
        idx = int(input("Какой предмет: "))
        item = hero.inventory.items[idx]
        # TODO: только лечение
        hero.inventory.use_item(idx, hero)
        logger.log_use_item(hero, item)
    else:
        damage = hero.attack(enemy)
        logger.log_attack(hero, enemy, damage)


def fight(player: Character, enemy: Character):
    print(f"\n=== БОЙ ===")
    print(f"{player} vs {enemy}\n")
        
    for _ in range(FIGHT_LIMIT):
        player_turn(player, enemy)
        
        # TODO: HW - Если пользователь сбежал, то return
        
        if not enemy.is_alive():
            logger.log_winner(player)
            return player
        
        damage = enemy.attack(player)
        logger.log_attack(enemy, player, damage)
        if not player.is_alive():
            logger.log_winner(enemy)
            return enemy
