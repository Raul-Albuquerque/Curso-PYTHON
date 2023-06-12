################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"Enemies inside de function: {enemies}")

increase_enemies()
print(f"Enemies outside de function: {enemies}")

############## LOCAL SCOPE ###################

def drink_potion():
  potion_strength = 2
  print(potion_strength)
drink_potion()

############# GLOBAL SCOPE ####################

player_health = 10

def drink_potion():
  potion_strength = 2
  print(player_health)
drink_potion()

print(player_health)