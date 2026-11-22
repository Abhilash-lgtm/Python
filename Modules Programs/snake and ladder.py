import tkinter as tk
from tkinter import messagebox
import random

# Snakes and Ladders

snakes = {
    29:15,
    35:21,
    42:12,
    56:22,
    74:39,
    87:3,
    92:64,
    99:44
}

ladders = {
    5:17,
    19:43,
    36:67,
    45:93,
    51:77,
    61:85,
    83:95
}

player1_pos = 0
player2_pos = 0

turn = 1

# --------------------------
# Roll Dice
# --------------------------

def roll_dice():

    global player1_pos
    global player2_pos
    global turn

    dice = random.randint(1,6)

    dice_label.config(
        text=f"🎲 Dice: {dice}"
    )

    if turn == 1:

        if player1_pos + dice <= 100:
            player1_pos += dice

        if player1_pos in snakes:
            messagebox.showinfo(
                "Snake",
                f"Player 1 bitten by snake!\nMoved to {snakes[player1_pos]}"
            )
            player1_pos = snakes[player1_pos]

        elif player1_pos in ladders:
            messagebox.showinfo(
                "Ladder",
                f"Player 1 climbed ladder!\nMoved to {ladders[player1_pos]}"
            )
            player1_pos = ladders[player1_pos]

        p1_label.config(
            text=f"Player 1 : {player1_pos}"
        )

        if player1_pos == 100:
            messagebox.showinfo(
                "Winner",
                "🏆 Player 1 Wins!"
            )
            return

        turn = 2
        turn_label.config(
            text="Turn : Player 2"
        )

    else:

        if player2_pos + dice <= 100:
            player2_pos += dice

        if player2_pos in snakes:
            messagebox.showinfo(
                "Snake",
                f"Player 2 bitten by snake!\nMoved to {snakes[player2_pos]}"
            )
            player2_pos = snakes[player2_pos]

        elif player2_pos in ladders:
            messagebox.showinfo(
                "Ladder",
                f"Player 2 climbed ladder!\nMoved to {ladders[player2_pos]}"
            )
            player2_pos = ladders[player2_pos]

        p2_label.config(
            text=f"Player 2 : {player2_pos}"
        )

        if player2_pos == 100:
            messagebox.showinfo(
                "Winner",
                "🏆 Player 2 Wins!"
            )
            return

        turn = 1

        turn_label.config(
            text="Turn : Player 1"
        )

# --------------------------
# Restart Game
# --------------------------

def restart():

    global player1_pos
    global player2_pos
    global turn

    player1_pos = 0
    player2_pos = 0
    turn = 1

    p1_label.config(
        text="Player 1 : 0"
    )

    p2_label.config(
        text="Player 2 : 0"
    )

    dice_label.config(
        text="🎲 Dice : -"
    )

    turn_label.config(
        text="Turn : Player 1"
    )

# --------------------------
# UI
# --------------------------

root = tk.Tk()

root.title(
    "Snake and Ladder Game"
)

root.geometry(
    "500x500"
)

root.configure(
    bg="#1e1e2f"
)

title = tk.Label(
    root,
    text="🐍 Snake & Ladder 🪜",
    font=("Arial",22,"bold"),
    bg="#1e1e2f",
    fg="white"
)

title.pack(
    pady=20
)

turn_label = tk.Label(
    root,
    text="Turn : Player 1",
    font=("Arial",14),
    bg="#1e1e2f",
    fg="yellow"
)

turn_label.pack()

dice_label = tk.Label(
    root,
    text="🎲 Dice : -",
    font=("Arial",20),
    bg="#1e1e2f",
    fg="white"
)

dice_label.pack(
    pady=20
)

p1_label = tk.Label(
    root,
    text="Player 1 : 0",
    font=("Arial",16),
    bg="#1e1e2f",
    fg="lightgreen"
)

p1_label.pack(
    pady=10
)

p2_label = tk.Label(
    root,
    text="Player 2 : 0",
    font=("Arial",16),
    bg="#1e1e2f",
    fg="lightblue"
)

p2_label.pack(
    pady=10
)

roll_btn = tk.Button(
    root,
    text="🎲 Roll Dice",
    font=("Arial",16,"bold"),
    bg="green",
    fg="white",
    width=15,
    command=roll_dice
)

roll_btn.pack(
    pady=20
)

restart_btn = tk.Button(
    root,
    text="🔄 Restart",
    font=("Arial",16,"bold"),
    bg="orange",
    fg="white",
    width=15,
    command=restart
)

restart_btn.pack()

root.mainloop()
