# Console user interface

def welcome_screen():
    print("Welcome to Escape the labyrinth")
    print("-" * 40)


def pick_difficulty():
    picked_difficulty = input("choose a difficulty(1-3): ")

    if picked_difficulty not in range(1, 4) or type(
            picked_difficulty) is not int:
        picked_difficulty = 0
        print("You chose invalid difficulty! Demo mode started.")

    return int(picked_difficulty)


def pick_a_hero(game):
    print(game.list_heroes())
    picked_hero = input("choose a hero: ")

    while not game.hero_exists(picked_hero):
        print("you entered incorrect name")
        picked_hero = input("choose a hero: ")

    game.add_hero(picked_hero)


def visualise_map(game):
    print("\nmap:\n{}".format(game.vision()))


def execute_command(game):
    command = input()
    command = command.split()
    if len(command) == 0:
        return
    if command[0] == 'instructions':
        print(game.instructions())
    elif command[0] == 'status':
        print(game.status())
    elif command[0] == 'inventory':
        print(game.inventory())
    elif command[0] == 'move':
        if len(command) > 1:
            if not game.move(command[1]):
                print("you cannot go there..")
    elif command[0] == 'exit':
        exit(0)


def pick_a_weapon(hero, weapon):
    print("you found a {}".format(weapon))
    answer = input("do you want to pick it?(y, n)")
    if answer == 'y':
        hero.equip_weapon(weapon)
        print("you got a new weapon!")


def drink_a_potion():
    print("you drank a potion!")


def won():
    print("you won!")


def next_level():
    print("nice, you got through this level")
    print("now it's time for the next one!")
    print("here be pythons..")
    print("-" * 40)


def stepped_on_an_boss():
    print('\n'.join(["you dared to wake up the boss!",
                     "now you're in trouble..\n"]))


def stepped_on_a_enemy():
    print("you stepped on a enemy!\n")


def init_fight(hero, enemy):
    print("{} vs {}\n".format(hero, enemy))


def status(hero, enemy):
    print("{}\n\n{}\n".format(hero, enemy))


def game_over():
    print("game over..")


def beaten_the(enemy):
    print("good job\nyou've beaten the {}\n\n".format(enemy))


def damage_dealt(hitter, damage):
    print("{} dealt {} damage\n".format(hitter, damage))


def hero_bonuses(health_bonus, damage_bonus):
    print("you got bonus for beating the anaconda:")
    print("your max health is now {}".format(health_bonus))
    print("your damage is now {}".format(damage_bonus))


# have to be beaten at the end but not for now :))
def beaten_by_enemy():
    print("you have been beaten by an "
          "enemy..")


def weapon_bonuses(damage_bonus, crit_bonus):
    print("your weapon damage is now {}".format(damage_bonus))
    print("your critical strike chance is now {}%".format(crit_bonus * 100))
