'''EXERSISE # 4
Time : this program was written on 19 october 2023 when i was doing a yt course on pyhton basics by codewithharry
use : in this program user palys rock paper sissor game with computer '''
import random

def play_rps_game(user_choice, computer_choice):
    options = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
    user_option = options[user_choice]
    computer_option = options[computer_choice]

    print(f"Your choice: {user_option}")
    print(f"Computer's choice: {computer_option}")

    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice - computer_choice) in [1, -2]:
        print("Congratulations, you win!")
    else:
        print("Sorry, you lose. Better luck next time.")


print("WELCOME TO THE ROCK, PAPER, SCISSORS GAME".center(125))
try :
    game_menu = int(input("Enter 1 to play and 2 for rules: "))
except ValueError:
    print("Please enter a number")
else:
    if game_menu == 2:
        print('''In this game, you are the player, and your opponent is the computer. You and the computer will be given three options: Rock, Paper, and Scissors. You will win the game if your choice beats the computer's choice. Here, Scissors beat Paper, Paper beats Rock, and Rock beats Scissors. If your choice and the computer's choice match, the game will be a draw.\n''')
        try:
            proceed = int(input("Now enter 1 to play and 2 to exit: "))
        except ValueError:
            print("Please enter a number")
        else:
            if proceed == 1:
                try:
                    user_choice = int(input('''Choose from the following options:
                    1 for Rock
                    2 for Paper
                    3 for Scissors\n'''))

                    if user_choice in [1, 2, 3]:
                        computer_choice = random.randint(1, 3)
                        play_rps_game(user_choice, computer_choice)
                    else:
                        print("You chose an invalid number. Please select 1, 2, or 3.")
                except ValueError:
                    print("Please enter a number")
            elif proceed == 2:
                print("Game over.")
            else:
                print("You entered an invalid option.")
    elif game_menu == 1:

        try:
            user_choice = int(input('''Choose from the following options:
            1 for Rock
            2 for Paper
            3 for Scissors\n'''))

            if user_choice in [1, 2, 3]:
                computer_choice = random.randint(1, 3)
                play_rps_game(user_choice, computer_choice)
            else:
                print("You chose an invalid number. Please select 1, 2, or 3.")
        except ValueError:
            print("Please enter a number")
    else:
        print("You have not selected the correct option.")

