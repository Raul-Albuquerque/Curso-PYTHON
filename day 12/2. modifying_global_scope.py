############ MODIFYING GLOBAL SCOPE ################

enemies = 1
#essa maneira não é indicada
def increase_enemies():
  global enemies
  enemies += 1
  print(f"Enemies inside the function: {enemies}")

increase_enemies()
print(f"Enemies outside de function: {enemies}")

def increase_enemies():
  print(f"Enemies inside the function: {enemies}")
  return enemies + 1
  
enemies = increase_enemies()
print(f"Enemies outside de function: {enemies}") 