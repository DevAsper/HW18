from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return 10

class Bow(Weapon):
    def attack(self):
        return 5

class MagicWand(Weapon):
    def attack(self):
        return 8


class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def changeWeapon(self, new_weapon: Weapon):
        self.weapon = new_weapon

    def fight(self, monster):
        damage = self.weapon.attack()
        monster.take_damage(damage)
        print(f"Fighter attacks with {self.weapon.__class__.__name__} dealing {damage} damage.")


class Monster:
    def __init__(self, health):
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        print(f"Monster takes {damage} damage, remaining health {self.health}")


def battle(fighter, monster):
    while monster.health > 0:
        fighter.fight(monster)
        if monster.health <= 0:
            print("Monster is defeated!")
            break

fighter = Fighter(Sword())
monster = Monster(30)
battle(fighter, monster)
fighter.changeWeapon(Bow())
monster = Monster(30)
battle(fighter, monster)

