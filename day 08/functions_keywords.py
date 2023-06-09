#function with more than 1 input:
"""
def greet_with(name, location):
  print(f"Hello, {name}")
  print(f"How is it like in {location}")
greet_with("Raul", "Recife")
"""
#function with keywords arguments:
def greet_with(name, location):
  print(f"Hello, {name}")
  print(f"How is it like in {location}?")
greet_with(location = "Recife", name = "Raul")