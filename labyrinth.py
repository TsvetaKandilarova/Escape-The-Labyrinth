# the labyrinth module
from random import randint

import map_
import ui
import enemy
import boss
import fight
import weapon
import potion
from database_manager import DatabaseManager

_enemy_base_health = 100
_enemy_health_per_level = 50
_enemy_base_damage = 0
_enemy_damage_per_level = 10

_boss_base_health = 370
_boss_health_per_level = 40
_boss_base_damage = 10
_boss_damage_per_level = 20
_boss_base_berserk_chance = 4
_boss_berserk_critical = 1.50


class Labyrinth:
    # labyrinth's constructor method
    def __init__(self, level, hero, max_level):
        self.map_ = map_.Map("./maps/%s_map" % level)
        self.hero = hero
        self.level = int(level)
        self.max_level = int(max_level)
        self.position = None
        self._weapons_types = DatabaseManager().get_weapons_type()
        self._weapons = DatabaseManager().get_weapons()

    # this spawns our hero at the top left corner of the map
    def spawn(self):
        self.position = (0, 0)
        self.map_.spawn()

    # returns the visible, to our hero, map
    def show_map(self):
        return self.map_.show_map(self.position)

    def _get_new_position(self, direction):
        if direction == 'up':
            return self.position[0] - 1, self.position[1]
        elif direction == 'down':
            return self.position[0] + 1, self.position[1]
        elif direction == 'left':
            return self.position[0], self.position[1] - 1
        elif direction == 'right':
            return self.position[0], self.position[1] + 1
        else:
            return self.position

    # moves the hero through the map
    # return false is move isn't possible
    # i.e. the field is an obstacle or is outside the map
    def move(self, direction):
        new_position = self._get_new_position(direction)

        if not self.map_.on_map(new_position) or \
                self.map_.is_obstacle(new_position):
            return False

        if self.map_.is_gate(new_position):
            if not self.level_up():
                exit(0)
            return True
        elif self.map_.is_enemy(new_position):
            self.fight_with_enemy()
        elif self.map_.is_boss(new_position):
            self.fight_with_boss()
        elif self.map_.is_item(new_position):
            self.get_item()

        self.map_.update_map(self.position, new_position)
        self.position = new_position

        return True

    # returns us a sweet little python based on level
    def _get_enemy_for_current_level(self):
        return enemy.Enemy(
            _enemy_base_health + _enemy_health_per_level * self.level,
            _enemy_base_damage + _enemy_damage_per_level * self.level)

    def _get_boss_for_current_level(self):
        boss_berserk_tuple = \
            (_boss_base_berserk_chance + 1 - self.level,
             _boss_berserk_critical)
        return boss.Boss(
            _boss_base_health + _boss_health_per_level * self.level,
            _boss_base_damage + _boss_damage_per_level * self.level,
            boss_berserk_tuple)

    # here we fight with our little python
    def fight_with_enemy(self):
        enemy_ = self._get_enemy_for_current_level()
        fight_ = fight.Fight(self.hero, enemy_)
        fight_.simulate_fight()

    # here hero fights with an anaconda
    def fight_with_boss(self):
        boss_ = self._get_boss_for_current_level()
        fight_ = fight.Fight(self.hero, boss_)
        fight_.simulate_fight()

    # gets the map for the new level, spawns the hero
    # returns true and prints some messaged
    # if no more levels, returns false
    def level_up(self):
        if self.level >= self.max_level:
            ui.won()
            return False

        self.level += 1
        ui.next_level()
        self.map_ = map_.Map("./maps/{}_map".format(self.level))
        self.hero.take_healing(potion.Potion(self.hero.max_health))
        self.spawn()

        return True

    # get's our hero a weapon or a potion
    # based on (not so) completely random circumstances
    def get_item(self):
        chance = randint(1, 100)

        if chance >= 50:
            weapon_ = self.get_weapon()
            ui.pick_a_weapon(self.hero, weapon_)
        else:
            potion_ = self.get_potion()
            self.hero.take_healing(potion_)
            ui.drink_a_potion()

    # returns a random weapon from the set of weapons based on level
    # for level 1 - only the first one,
    # for level 2 - the first four ones and
    # for level 3 all weapons are available
    # (level 0 is a demo/test mode)

    def get_weapon(self):
        if self.level == 0:
            chance = randint(1, len(self._weapons_types))
        else:
            chance = randint(1, (self.level * 3 - 3) or 1)

        type_ = self._weapons_types[chance - 1]
        weapon_ = weapon.Weapon(type_, self._weapons[type_][0],
                                self._weapons[type_][1], 1)
        return weapon_

    # returns a potion healing 50% of our hero's missing health
    def get_potion(self):
        missing_health = self.hero.max_health - self.hero.health
        potion_ = potion.Potion(missing_health * 0.50)
        return potion_
