import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    choices = ["rock", "paper", "scissors"]

    print("Welcome to Rock, Paper, Scissors!")
    print("Please choose one of the following options:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_choice = int(input("Enter your choice (1-3): ")) - 1
    if user_choice < 0 or user_choice >= len(choices):
        print("Invalid choice. Please try again.")
        return

    computer_choice = random.choice(choices)

    print(f"\nYou chose: {choices[user_choice]}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(choices[user_choice], computer_choice)
    print(result)

play_game()
