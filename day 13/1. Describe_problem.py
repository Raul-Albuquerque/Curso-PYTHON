############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# o loop acima está se repetindo somente 19 vezes. Para resolver, basta colocar 21 no lugar do vinte:

def my_function():
  for i in range(1, 21):
    if i == 20:
       print("You got it.")
my_function()