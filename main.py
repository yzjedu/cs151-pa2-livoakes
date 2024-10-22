# Liv Oakes
# Dr. Yalew
# CS151
# 10/23/2024
# PA2
# Purpose: A simple stick taking game where players, including a computer player, take turns removing 1-3 sticks from
#           a pile. The player to take the last stick loses.

import random
# Keep track of losses
total_losses = {"Player 1": 0, "Player 2": 0, "Computer": 0}

def initial_sticks():
    while True:
        sticks = int(input("Enter the number of sticks (10-100): "))
        if sticks >= 10 and sticks <= 100:
                return sticks
        else:
            print("Error: Number must be between 10 and 100.")


def player_turn():
    while True:
        sticks_taken = int(input("How many sticks do you want to take? (1-3): "))
        if sticks_taken >= 1 and sticks_taken <= 3:
                return sticks_taken
        else:
            print("Error: You must take 1, 2, or 3 sticks.")


def computer_turn():
    sticks_taken = random.randint(1, 3)
    print(f"The computer took {sticks_taken} stick(s).")
    return sticks_taken

# Main game loop
play_again = True
while play_again:
    sticks = initial_sticks()
    players = ["Player 1", "Player 2", "Computer"]
    current_player_index = 0
    game_losses = {player: 0 for player in players}

# Stick taking loop
    while sticks > 0:
        print(f"\nCurrent number of sticks: {sticks}")
        current_player = players[current_player_index]
        print(f"{current_player}'s turn.")

# Determine if it's the computer's turn or player's turn
        if current_player == "Computer":
            taken = computer_turn()
        else:
            sticks_taken = player_turn()

        sticks -= sticks_taken

        if sticks <= 0:
            print(f"\n{current_player} has lost!")
            game_losses[current_player] += 1
            total_losses[current_player] += 1

# Move to next player
        current_player_index = (current_player_index + 1) % len(players)

# Check if game is over
    continue_game = input("Would you like to play again? (yes/no): ").lower().strip()
    if continue_game == "yes":
            play_again = True
    elif continue_game == "no":
            play_again = False
    else:
        input("Invalid input. Please enter 'yes' or 'no'.")

# Display total losses for each player
print("\nTotal losses:")
for player, losses in total_losses.items():
    print(f"{player}: {losses}")