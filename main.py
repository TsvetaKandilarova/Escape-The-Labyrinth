# the script that runs the whole game
import gameplay
import ui


# briefly: gets input from the keyboard to manipulate
# the whole action in a cycle that runs
# until we win or we get eaten
def main():
    ui.welcome_screen()


game = gameplay.Gameplay(ui.pick_difficulty())


hero_name = ui.pick_a_hero(game)

while game.in_game():
    print("\nmap:\n{}".format(game.vision()))
    command = input()
    command = command.split()
    if len(command) == 0:
        continue
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

if __name__ == '__main__':
    main()
