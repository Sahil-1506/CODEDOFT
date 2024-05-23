import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter your choice (rock, paper, or scissors) rock: ").lower()
    computer_choice = random.choice(choices)
    

    print(f"\nComputer's choice: {computer_choice}")

    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win! take a party.")
    else:
        print("Computer wins!")

# Play the game
play_game()
