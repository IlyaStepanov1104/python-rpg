from random import randint
from characters import Character
from config import FIGHT_LIMIT

def fight(a: Character, b: Character):
    if randint(0, 1):
        a, b = b, a
    for _ in range(FIGHT_LIMIT):
        a.attack(b)
        if not b.is_alive():
            return a
        b.attack(a)
        if not a.is_alive():
            return b