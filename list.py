# Project 4 In Python Quarter 3

# Rock , Paper , Scissors Game #

import random 

# Game Choices #

choices = ["rock" , "paper" , "scissors"]

# Player Choice #
player_choice = input("Enter rock , paper , or scissors: ").lower()

# Computer Choice #

computer_choice = random.choice(choices)

# Winner Desicion #
if player_choice == computer_choice:
 print(f"same choice as {player_choice} Its a Tie!")
elif player_choice == "rock" and computer_choice == "scissors":
  print(f"Player wins! {player_choice} beats {computer_choice}.")
  
  
elif player_choice =="paper" and computer_choice == "rock":
  print(f"Player wins! {player_choice} beats {computer_choice}.")

elif player_choice =="scissors" and computer_choice == "paper":
  print(f"Player wins! {player_choice} beats {computer_choice}.")

else:
  print(f"Computer Wins! {computer_choice} beats {player_choice}")
