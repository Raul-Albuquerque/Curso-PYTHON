from game_data import data
from art import logo
from art import vs
import random


#functions space
winner = ''
def compare(first_person, second_person, users_choice):
  if first_person['follower_count'] > second_person['follower_count']:
    winner = 'A'
    print(winner)
  else:
    winner = 'B'
    print(winner)
  if users_choice == winner:
    return 'you are right! Current score: '
  else:
    return "Sorry, that's wrong. Final score: "
    
game_over = False
score = ()
while not game_over:
  first_person = random.choice(data)
  second_person = random.choice(data)
  if first_person == second_person:
    first_person = random.choice(data)
  
  #SHOW THE LOGO
  print(logo)
  
  #return the name of first person to dictionary
  print(f"Compare A: {first_person['name']}, {first_person['description']}, from {first_person['country']}.")
  
  #print the 'VS'
  print(vs)
  
  #return the name of second person to dictionary
  print(f"Compare B: {second_person['name']}, {second_person['description']}, from {second_person['country']}.")
  
  #ask who has more followers
  users_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
  
  #function with two inputs named compare to return who has more followers
  print(compare(first_person, second_person, users_choice))
  print(users_choice)

