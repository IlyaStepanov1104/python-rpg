from characters import Character
from items import HEALTH_POTION, BIG_HEALTH_POTION, POISON_POTION, BIG_POISON_POTION

SHOP = [
    (HEALTH_POTION, 30),
    (BIG_HEALTH_POTION, 60),
    (POISON_POTION, 25),
    (BIG_POISON_POTION, 50),
]

def tavern(hero: Character):
    print(f"\n=== ТАВЕРНА === | Gold: {hero.gold}")
    
    while True:
        print()
        
        for i, (item, price) in enumerate(SHOP):
            print(f"[{i}] {item.name} - {price}")
        print('[q] Выйти')
    
        choice = input('Выбор: ').strip()
        
        if choice == 'q':
            break
            
        if not choice.isdigit() or int(choice) >= len(SHOP):
            print("Неверный выбор")
            continue
        
        id = int(choice)
        item, price = SHOP[id]
        
        if hero.gold < price:
            print(f"Не хватает gold. Нужно {price}, есть {hero.gold}")
            continue
            
        hero.gold -= price
        hero.inventory.add_item(item)
        print(f"Куплено: {item.name}. Осталось gold: {hero.gold}")