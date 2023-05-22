height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

height_float = float(height)
weight_float = float(weight)

bmi = int(weight_float/(height_float ** 2))
print(bmi)

#refactoring -> cleaning the code
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = int ( float ( weight ) / float (height) ** 2)
print(bmi)
