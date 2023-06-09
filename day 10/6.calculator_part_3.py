#Calculator

#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calculator():
  num_1 = int(input("What's the first number? "))
  for symbol in operations:
    print(symbol)
  
  should_continue = True
  
  while should_continue:
    operation = input("Pick an operation: ")
    num_2 = int(input("What's the next number? "))
    calculation_function = operations[operation]
    answer = calculation_function(num_1, num_2)
    
    print(f"{num_1} {operation} {num_2} = {answer}")
  
    if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ") == "y":
      num_1 = answer
    else:
      should_continue = False
      calculator()
calculator()