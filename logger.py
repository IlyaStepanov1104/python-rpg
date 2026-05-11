from time import sleep
from colorama import Fore, Style, init


class Logger:
    personStyle = Fore.GREEN
    damageStyle = Fore.RED
    itemStyle = Fore.BLUE
    levelStyle = Fore.YELLOW
    
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
        
    def log_exit(self, hero):
        print(
            f"{self.personStyle}{hero.name}{Style.RESET_ALL} сбежал с боя"
        )
    
    def log_use_heal_item(self, hero, item):
        print(
            f"{self.personStyle}{hero.name}{Style.RESET_ALL} использует {self.itemStyle}{item.name}{Style.RESET_ALL} "
            f"HP: {hero.hp}/{hero.max_hp}"
        )
    
    def log_use_damage_item(self, hero, enemy, item):
        print(
            f"{self.personStyle}{hero.name}{Style.RESET_ALL} использует {self.itemStyle}{item.name}{Style.RESET_ALL} на {self.personStyle}{enemy.name}{Style.RESET_ALL} "
            f"HP: {enemy.hp}/{enemy.max_hp}"
        )
        
    def log_drop(self, drop):
        print(
            f"Выпал дроп: {self.itemStyle}{drop.name}{Style.RESET_ALL}"
        )
        
    def log_death(self, hero):
        print(
            f"{self.personStyle}{hero.name}{Style.RESET_ALL} погиб!"
        )
        print(f"{self.damageStyle}Вы проиграли{Style.RESET_ALL}")
        
    def log_level_up(self, hero):
        print(
            f"{self.personStyle}{hero.name}{Style.RESET_ALL} достиг уровня {self.levelStyle}{hero.level}{Style.RESET_ALL}!"
        )
logger = Logger()