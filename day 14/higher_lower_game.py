from art import logo
from art import vs
from game_data import data
import random
#from replit import clear

def compare(first_person, second_person, users_choice, score, game_over):
  winner = ''
  if first_person['follower_count'] > second_person['follower_count']:
    winner = 'A'
  else:
    winner = 'B'
  if winner == users_choice:
    return True
  else:
    return False

def game ():
  print(f"Compare A: {first_person['name']}, {first_person['follower_count']}, {first_person['description']}, from {first_person['country']}.")
  print(vs)
  print(f"Compare B: {second_person['name']}, {second_person['follower_count']}, {second_person['description']}, from {second_person['country']}.")

score = 0
game_over = False
print(logo)
while not game_over:
  first_person = random.choice(data)
  second_person = random.choice(data)

  if first_person == second_person:
    second_person = random.choice(data)
  game()
  users_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
  score += 1
  print (compare(first_person, second_person, users_choice, score, game_over))
  #clear()
  print(logo)
  if compare(first_person, second_person, users_choice, score, game_over) == True:
    print(f"You are right! Current score: {score}.")
  else:
    print(f"Sorry, That's wrong. Final score: {score}. ")
    game_over = True