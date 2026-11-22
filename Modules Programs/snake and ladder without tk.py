import random

# ----------------------------
# Dice Function
# ----------------------------

def roll_dice():
    return random.randint(1, 6)

# ----------------------------
# Snakes and Ladders
# ----------------------------

snakes = {
    29: 15,
    35: 21,
    42: 12,
    56: 22,
    74: 39,
    87: 3,
    92: 64,
    99: 44
}

ladders = {
    5: 17,
    19: 43,
    36: 67,
    45: 93,
    51: 77,
    61: 85,
    83: 95
}

# ----------------------------
# Player Details
# ----------------------------

print("\n===== SNAKE AND LADDER GAME =====\n")

player1 = input("Enter Player 1 Name: ")
player2 = input("Enter Player 2 Name: ")

player1_score = 0
player2_score = 0

WINNING_POINT = 100

# ----------------------------
# Game Loop
# ----------------------------

while True:

    # ------------------------
    # Player 1 Turn
    # ------------------------

    print("\n----------------------------------")
    print(f"{player1}'s Turn")
    print("----------------------------------")

    choice = input("Press P to Play or Q to Quit: ").upper()

    if choice == "Q":
        print(f"\n🏆 {player2} Wins the Game!")
        break

    dice = roll_dice()

    print(f"🎲 Dice Value: {dice}")

    if player1_score + dice <= WINNING_POINT:
        player1_score += dice

    if player1_score in snakes:
        print("🐍 Oh No! Snake Bite")
        player1_score = snakes[player1_score]

    elif player1_score in ladders:
        print("🪜 Great! Ladder Found")
        player1_score = ladders[player1_score]

    print(f"{player1}'s Position: {player1_score}")

    if player1_score == WINNING_POINT:
        print(f"\n🏆 Congratulations {player1}!")
        print("You Won the Game!")
        break

    # ------------------------
    # Player 2 Turn
    # ------------------------

    print("\n----------------------------------")
    print(f"{player2}'s Turn")
    print("----------------------------------")

    choice = input("Press P to Play or Q to Quit: ").upper()

    if choice == "Q":
        print(f"\n🏆 {player1} Wins the Game!")
        break

    dice = roll_dice()

    print(f"🎲 Dice Value: {dice}")

    if player2_score + dice <= WINNING_POINT:
        player2_score += dice

    if player2_score in snakes:
        print("🐍 Oh No! Snake Bite")
        player2_score = snakes[player2_score]

    elif player2_score in ladders:
        print("🪜 Great! Ladder Found")
        player2_score = ladders[player2_score]

    print(f"{player2}'s Position: {player2_score}")

    if player2_score == WINNING_POINT:
        print(f"\n🏆 Congratulations {player2}!")
        print("You Won the Game!")
        break

# ----------------------------
# Final Scores
# ----------------------------

print("\n========== FINAL SCORES ==========")
print(f"{player1}: {player1_score}")
print(f"{player2}: {player2_score}")
print("==================================")
