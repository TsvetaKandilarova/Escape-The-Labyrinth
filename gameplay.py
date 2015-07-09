# gameplay module

import hero
import labyrinth
import copy

_heroes = [hero.Hero("sharik", 400, "pythonslayer", 40),
           hero.Hero("arya", 380, "shadow princess", 40),
           hero.Hero("silmarillion iv", 420, "lost king of pyland", 35)]

_heroes_by_name = {"sharik": _heroes[0],
                   "arya": _heroes[1],
                   "silmarillion": _heroes[2]}


class Gameplay:
    def __init__(self, difficulty):
        self.difficulty = int(difficulty)
        self.labyrinth = None

    def add_hero(self, hero_name):
        hero_ = self.pick_a_hero(hero_name)
        starting_level = self.difficulty
        if self.difficulty == 0:
            starting_level = 0
        self.labyrinth = labyrinth.Labyrinth(starting_level, hero_,
                                             self.difficulty)
        self.labyrinth.spawn()

    # returns a hero object depending on 'hero_name'
    @staticmethod
    def pick_a_hero(hero_name):
        return copy.deepcopy(_heroes_by_name[hero_name])

    @staticmethod
    def list_heroes():
        heroes = ["\nheroes:"]
        for _ in _heroes_by_name:
            heroes.append("-" * 40)
            heroes.append(str(_heroes_by_name[_]))
            heroes.append("-" * 40)
        return '\n'.join(heroes)

    # return true if a hero with name 'hero_name' exists
    @staticmethod
    def hero_exists(hero_name):
        return hero_name in _heroes_by_name

    def vision(self):
        return self.labyrinth.show_map()

    # moves our hero in 'direction' and returns true if
    # the move is possible, else false
    def move(self, direction):
        return self.labyrinth.move(direction)

    # returns our hero's status - health points and damage
    def status(self):
        return self.labyrinth.hero

    # returns our hero's inventory
    # (for this version, the hero can have only one weapon)
    def inventory(self):
        if 'weapon' not in self.labyrinth.hero.__dict__:
            return "your inventory is empty"
        else:
            return self.labyrinth.hero.weapon

    # prints some instructions to help playing the game

    @staticmethod
    def instructions():
        commands = "available commands:\n" \
                   + "move <direction=up/down/right/left>\n" + \
                   " status\ninventory\nexit"
        map_key = "\n\nmap key:\n" \
                  + "B - boss\nE - enemy\nH - hero\nI - item\nG - gate"
        more_help = "\n\nreach the gate to go to the next level,\n" \
                    + "but be careful with the evil creatures!\n"

        return commands + map_key + more_help

    # returns true if we're still playing and
    # false if we've beaten eaten by an enemy
    def in_game(self):
        return self.labyrinth.hero.is_alive()
