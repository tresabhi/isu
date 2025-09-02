import os
import random

ANTAGONISTS = ['🪨', '📃', '✂️']
PROTAGONISTS = [2, 0, 1]


def play():
  while True:
    os.system('cls')
    print("Let's play rock, paper, scissors! Type the corresponding number to your choice.\n\n  EXIT = 0\n  🪨    = 1\n  📃   = 2\n  ✂️    = 3\n")

    player_choice = int(input("Your choice: "))
    computer_choice = random.randint(1, 3)

    if (player_choice < 0 or player_choice > 3):
      print("Invalid input.")

    if (player_choice == 0):
      print("\nGracefully exiting...")
      return

    round_status = "It's a tie!"
    if (computer_choice != player_choice):
      if (PROTAGONISTS[player_choice - 1] == computer_choice):
        round_status = "You lose!"
      else:
        round_status = "You win!"

    print(
        f"\n\nYou:      {ANTAGONISTS[player_choice - 1]}\nComputer: {ANTAGONISTS[computer_choice - 1]}\n\n{round_status}")

    input("\nPress enter to continue...")


play()
