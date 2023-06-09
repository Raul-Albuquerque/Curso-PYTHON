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

num_1 = int(input("What's the first number? "))


for symbol in operations:
  print(symbol)
operation = input("Pick an operation from line above: ")
num_2 = int(input("What's the second number? "))
calculation_function = operations[operation]
first_answer = calculation_function(num_1, num_2)

print(f"{num_1} {operation} {num_2} = {first_answer}")

operation = input("Pick another operation: ")
num_3 = int(input("What's the next number? "))
calculation_function = operations[operation]
second_answer = calculation_function(first_answer, num_3)

print(f"{first_answer} {operation} {num_3} = {second_answer}")