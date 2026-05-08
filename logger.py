from time import sleep
from colorama import Fore, Style, init


class Logger:
    personStyle = Fore.GREEN
    damageStyle = Fore.RED
    itemStyle = Fore.BLUE
    
    def __init__(self) -> None:
        init()
        
    def log_attack(self, attacker, defender, damage):
        print(
            f"{self.personStyle}{attacker.name}{Style.RESET_ALL} наносит "
            f"{self.damageStyle}{damage}{Style.RESET_ALL} урона персонажу "
            f"{self.personStyle}{defender.name}{Style.RESET_ALL} "
            f"HP: {defender.hp}/{defender.max_hp}"
        )
        sleep(0.5)
        
    def log_winner(self, winner):
        print(
            f"{self.personStyle}{winner.name}{Style.RESET_ALL} одержал победу "
            f"HP: {winner.hp}/{winner.max_hp}"
        )
    
    def log_use_item(self, hero, item):
        print(
            f"{self.personStyle}{hero.name}{Style.RESET_ALL} использует {self.itemStyle}{item.name}{Style.RESET_ALL} "
            f"HP: {hero.hp}/{hero.max_hp}"
        )
        
logger = Logger()