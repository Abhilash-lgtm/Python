from game_module import get_computer_choice
from game_module import determine_winner

print("===== ROCK PAPER SCISSORS =====")

while True:

    user_choice = input(
        "\nEnter Rock, Paper, Scissors or Quit: "
    ).lower()

    if user_choice == "quit":
        print("Game Over!")
        break

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid Choice!")
        continue

    computer_choice = get_computer_choice()

    print(f"You      : {user_choice}")
    print(f"Computer : {computer_choice}")

    result = determine_winner(
        user_choice,
        computer_choice
    )

    if result == "Tie":
        print("🤝 Match Tie")

    elif result == "User":
        print("🏆 You Win")

    else:
        print("💻 Computer Wins")
