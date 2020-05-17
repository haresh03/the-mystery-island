import time
import random


def print_slow(s):
    print(s)
    time.sleep(3)


def valid_input():
    while True:
        choice = input()
        if choice == '1':
            return choice
            break
        elif choice == '2':
            return choice
            break
        else:
            print(">> Enter either 1 or 2! <<")


def start():
    print_slow("#DAY 1: You are stuck on some island in the vast"
               " sea after your ship got sunk.")
    print_slow(">> You are the only survivor alive!")
    print_slow(">> You figured out ways to stay alive on this island\n")
    print_slow("#DAY 19: You spend weeks, after which you saw"
               " a ship far away from you!")
    print_slow("==> What would you do?\n"
               "1: Wave your hand at the ship\n"
               "2: Swim to approach it\n[ Enter 1  or 2 ]")
    choice = valid_input()
    if choice == '1':
        print_slow(">> Seems good. But this didn't work and"
                   " the ship sailed away!\n")
        day45()
    else:
        print_slow(">> While swimming you found out"
                   " there are sharks out there. oops!")
        game_over()


def day45():
    print_slow("#Day 45: Roaming on the island you found a box.")
    print_slow("==> What would you want to do?\n"
               "1: Open it!\n"
               "2: Throw it in the ocean.\n[ Enter 1  or 2 ]")
    choice = valid_input()
    if choice == '1':
        box = random.choice(['Teleporter', 'Clothes', 'Gold', 'Silver',
                             'Camera', 'Lamp'])
        print_slow(">> Well you found: " + box)
        if box == 'Teleporter':
            print_slow('>> You used it to go home')
            end()
        elif box == 'Lamp':
            print_slow(">> You played with the lamp and found a magical genie,"
                       " who offered you only one wish")
            print_slow("==> What would you wish for?\n"
                       "1: Wish to go home.\n"
                       "2: Wish for $100 billion dollars.\n[ Enter 1  or 2 ]")
            choice = valid_input()
            if choice == '1':
                end()
            else:
                print_slow('>> Keep it safe with you :-)\n')
                day78()
        else:
            print_slow('>> Keep it safe with you :-)\n')
            day78()
    else:
        print_slow(">> Well doesn't matter. :-) \n")
        day78()


def day78():
    print_slow("#Day 78: You tried to go deep inside "
               "the island and found a cave")
    print_slow("==> What would you want to do?\n"
               "1: Go inside!\n"
               "2: Return back.\n[ Enter 1  or 2 ]")
    choice = valid_input()
    if choice == '1':
        print_slow(">> There was a hungry lion inside, oops!")
        game_over()
    else:
        print_slow(">> Well, good! :-)")
        print_slow("#Day 99: You saw a helicopter asked it for help,"
                   " it passed you a rope to climb.")
        end()


def end():
    print_slow('>> You successfully escaped the island, congrats! <<')
    game_over()


def game_over():
    print_slow("** GAME OVER! **")
    print_slow(">> Would you like to play again? <<\n1.YES\n2.NO")
    choice = valid_input()
    if choice == '1':
        start()
    else:
        print_slow("*** Thanks for playing! ***")


print_slow("** WELCOME! **")
print_slow("The Mystery Island - A Text Based Adventure Game\n"
           "By -- Haresh Gaikwad\n")

if __name__ == "__main__":
    start()
