from random import random, choice
from characters import Character
from config import DROPS, FIGHT_LIMIT, GOLD_REWARD, XP_REWARD
from logger import logger


def generate_drop():
    if random() < 0.7:
        return choice(DROPS)
    return None

def player_turn(hero, enemy):
    """
    Returns:
        bool: Сбежал ли с боя
    """
    
    print(f"\n=== Твой ход ===")
    print(f"{hero.name}: HP {hero.hp}/{hero.max_hp} | Gold: {hero.gold} | Инвентарь: {hero.inventory}")
    print(f"{enemy.name}: HP {enemy.hp}/{enemy.max_hp}")
    print()
    print("[1] Атаковать")
    if hero.inventory.items:
        print("[2] Использовать предмет")
        
    print("[3] Выход из боя")
    
    choice = input("Выбор: ").strip()
    
    if choice == "2" and hero.inventory.items:
        for i in range(len(hero.inventory.items)):
            print(f"  [{i}] {hero.inventory.items[i]}")
        
        idx = int(input("Какой предмет: "))
        item = hero.inventory.items[idx]
        if item.style == 'heal':
            hero.inventory.use_item(idx, hero)
            logger.log_use_heal_item(hero, item)
        elif item.style == 'damage':
            hero.inventory.use_item(idx, enemy)
            logger.log_use_damage_item(hero, enemy, item)
    elif choice == '3':
        return True
    else:
        damage = hero.attack(enemy)
        logger.log_attack(hero, enemy, damage)
    
    return False


def fight(player: Character, enemy: Character):
    print(f"\n=== БОЙ ===")
    print(f"{player} vs {enemy}\n")
        
    for _ in range(FIGHT_LIMIT):
        is_player_exit = player_turn(player, enemy)
        
        if is_player_exit:
            logger.log_exit(player)
            return None

        if not enemy.is_alive():
            logger.log_winner(player)
            player.gold += GOLD_REWARD
            player.gain_xp(XP_REWARD)
            drop = generate_drop()
            if drop:
                player.inventory.add_item(drop)
                logger.log_drop(drop)
            return player
        
        damage = enemy.attack(player)
        logger.log_attack(enemy, player, damage)
        if not player.is_alive():
            logger.log_winner(enemy)
            return enemy
