from abc import ABC, abstractmethod
from random import randint, choice

class Item(ABC):
    def __init__(self, name: str, health=300):
        self.name = name
        self.health = health
    
    @abstractmethod
    def attack(self, another_item):
        pass

    @abstractmethod
    def boost(self):
        pass

class Sword(Item):
    def __init__(self, name, attack_power: int):
        super().__init__(name=name)
        self.__attack_power = attack_power
        self._sharp = 0
    
    def attack(self, another_item: Item):
        current_attack = self.__attack_power + self._sharp + randint(0, 10)
        another_item.health -= current_attack
        return f"⚔️ {self.name} січе лезом! Шкода: {current_attack}. У {another_item.name} HP: {max(0, another_item.health)}"
    
    def boost(self):
        self._sharp += 5
        return f"✨ Ви наточили меч {self.name}! (Гострота +5)"

class Axe(Item):
    def __init__(self, name, attack_power: int):
        super().__init__(name=name)
        self.__attack_power = attack_power
    
    def attack(self, another_item: Item):
        current_attack = self.__attack_power + randint(0, 20)
        another_item.health -= current_attack
        return f"🪓 {self.name} вгатив сокирою! Шкода: {current_attack}. У {another_item.name} HP: {max(0, another_item.health)}"

    def boost(self):
        bonus = randint(5, 10)
        self.health += bonus 
        return f"😡 {self.name} впадає в лють! Відновлено {bonus} HP."

class Bow(Item):
    def __init__(self, name, attack_power: int, range_power: int):
        super().__init__(name=name)
        self.__attack_power = attack_power
        self.range_power = range_power
    
    def attack(self, another_item: Item):
        current_attack = self.__attack_power + randint(5, 15) + self.range_power
        another_item.health -= current_attack
        return f"🏹 {self.name} випускає стрілу! Шкода: {current_attack}. У {another_item.name} HP: {max(0, another_item.health)}"

    def boost(self):
        self.range_power += 2
        return f"🎯 {self.name} покращує позицію! (Дальність +2)"

def start_game():
    weapon_classes = [
        lambda: Sword("Ескалібур", 40),
        lambda: Axe("Кривава Жатва", 45),
        lambda: Bow("Око Сокола", 35, 10)
    ]
    
    player_weapon = choice(weapon_classes)()
    bot_weapon = choice(weapon_classes)()
    
    print(f"Ваша зброя: {player_weapon.name} ({type(player_weapon).__name__})")
    print(f"Супротивник: {bot_weapon.name} ({type(bot_weapon).__name__})")

    while player_weapon.health > 0 and bot_weapon.health > 0:
        print(f"\nВаше HP: {player_weapon.health} | HP Ворога: {bot_weapon.health}")
        action = input("Виберіть дію: 1 - Атакувати, 2 - Покращити: ")
        
        if action == "1":
            print(player_weapon.attack(bot_weapon))
        else:
            print(player_weapon.boost())
            
        if bot_weapon.health <= 0:
            print(f"\n🏆 ПЕРЕМОГА! {bot_weapon.name} знищено.")
            break

        bot_action = randint(1, 2)
        if bot_action == 1:
            print(bot_weapon.attack(player_weapon))
        else:
            print(bot_weapon.boost())

        if player_weapon.health <= 0:
            print(f"\n💀 ВИ ПРОГРАЛИ! {player_weapon.name} зламано.")
            break

if __name__ == "__main__":
    start_game()