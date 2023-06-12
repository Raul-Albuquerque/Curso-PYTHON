#Number Guessing Game Objectives:

# Include an ASCII art logo.
import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking in a number between 0 and 100.")

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
def check_answer(NUMBER, user_guess):
    # If they got the answer correct, show the actual answer to the player.
  if user_guess == NUMBER:
    return "You win."
  elif user_guess > NUMBER:
    return "Too high."
  elif user_guess < NUMBER:
    return "Too low."

NUMBER = random.randint(0, 100)
is_game_over = False
turns_remaining = 0
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
game_level = input("Choose a dificulty. Type 'easy' or 'hard': ")

if game_level == "easy":
  turns_remaining = 9
else:
  turns_remaining = 4

while not is_game_over:
  print(f"The correct answer is: {NUMBER}")
  # Allow the player to submit a guess for a number between 1 and 100.
  user_guess = int(input("Make a guess:"))
  print(check_answer(NUMBER, user_guess))
  if check_answer(NUMBER, user_guess) == "You win.":
    is_game_over = True
  elif turns_remaining == 0:
    # If they run out of turns, provide feedback to the player. 
    print(f"You lose. The correct answer is {NUMBER}.")
    is_game_over = True 
  else:
    if turns_remaining == 1:
      print(f"You have only {turns_remaining} turn ramaining.")
    else:
      print(f"You have {turns_remaining} turns ramaining.")
    turns_remaining -= 1