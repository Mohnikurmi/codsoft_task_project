import random


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "scissors" and computer_choice == "paper") or \
            (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"


def main():
    choices = ["rock", "paper", "scissors"]
    print("Welcome to Rock-Paper-Scissors!")
    print("Choose: rock, paper, or scissors")

    while True:
        user_choice = input("Your choice: ").lower()
        if user_choice not in choices:
            print("Invalid choice. Please select rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
