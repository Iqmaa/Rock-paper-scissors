import random

while True:
    user_action = input("Enter a choice ('R' for rock, 'P' for paper, 'S' for scissors): ")
    user_action = user_action.upper()
    possible_actions = ["R", "P", "S"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "R":
        if computer_action == "S":
            print(f"player{user_action}: computer{computer_action}, you win!")
        else:
            print(f"player{user_action}: computer{computer_action}, you lose!")
    elif user_action == "P":
        if computer_action == "R":
            print(f"player{user_action}: computer{computer_action}, you win!")
        else:
            print(f"player{user_action}: computer{computer_action}, you lose!")
    elif user_action == "S":
        if computer_action == "P":
            print(f"player{user_action}: computer{computer_action}, you win!")
        else:
            print(f"player{user_action}: computer{computer_action}, you lose!")
    elif user_action != ("R","P","S"):
            print("Invalid input, please choose from the given parameters")

    play_again = input("Input 'yes' for a rematch : ")
    if play_again.lower() != "yes":
        break