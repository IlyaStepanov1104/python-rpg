from characters import Mage, Warior
from fight import fight
from items import HEALTH_POTION

hero = Warior("Артур")
enemy = Mage("Мерлин")

hero.inventory.add_item(HEALTH_POTION)

winner = fight(hero, enemy)