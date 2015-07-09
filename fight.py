# our fight module
from random import randint
from hero import Hero
from boss import Boss
import ui


# the bonuses we get for slaining bosses!
_health_bonus = 0.10
_damage_bonus = 0.10
_weapon_damage_bonus = 0.05
_weapon_critical_hit_chance_bonus = 0.05


class Fight:
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy

    # returns true if Hero should hit first,
    # else false
    @staticmethod
    def flip_coin():
        chance = randint(1, 100)
        return chance >= 50

    # returns a tuple from fight's hero and enemy in the
    # following form: attacker, attacked
    def pick_order(self):
        if self.flip_coin():
            return self.hero, self.enemy

        return self.enemy, self.hero

    # some informational messages to help us know
    # what's going on during the fight
    def init_fight(self):
        enemy = "enemy"
        if isinstance(self.enemy, Boss):
            ui.stepped_on_an_boss()
            enemy = "boss"
        else:
            ui.stepped_on_a_enemy()

        ui.init_fight(self.hero.known_as(), enemy)

    def status(self):
        ui.status(self.hero, self.enemy)

    @staticmethod
    def game_over():
        ui.game_over()
        exit(0)

    def won(self):
        enemy = "enemy"

        if isinstance(self.enemy, Boss):
            enemy = "boss"

        ui.beaten_the(enemy)

    # information about every hit during the fight
    # (i.e. damage dealt and taken)

    # calculates the bonuses we get for defeating a boss
    # (no bonuses for a enemy)
    def bonus(self):
        self.hero.max_health += int(self.hero.max_health * _health_bonus)
        self.hero.damage += int(self.hero.damage * _damage_bonus)
        self.hero.health = self.hero.max_health

        ui.hero_bonuses(self.hero.max_health, self.hero.damage)

        if self.hero.weapon is not None:
            self.hero.weapon.damage += \
                int(self.hero.weapon.damage * _weapon_damage_bonus)

            self.hero.weapon.critical_strike_percent += \
                self.hero.weapon.critical_strike_percent * \
                _weapon_critical_hit_chance_bonus
            if self.hero.weapon.critical_strike_percent > 1.0:
                self.hero.weapon.critical_strike_percent = 1.0

            ui.weapon_bonuses(self.hero.weapon.damage,
                              self.hero.weapon.critical_strike_percent)

    def simulate_fight(self):
        attacker, attacked = self.pick_order()

        self.init_fight()

        while attacker.is_alive() and attacked.is_alive():
            self.status()
            damage = attacker.attack()
            battle(damage, attacker)
            attacked.take_damage(damage)
            attacker, attacked = attacked, attacker

        if attacker == self.hero:
            ui.beaten_by_enemy()
            self.game_over()
        elif isinstance(attacker, Boss):
            self.won()
            self.bonus()
        else:
            self.won()

        return attacked


def battle(damage, attacker):
    hitter = "enemy"
    if isinstance(attacker, Hero):
        hitter = "you"

    ui.damage_dealt(hitter, damage)
