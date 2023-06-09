print("Welcome to tip calculator!!")

total_bill = float(input ("What was the total bill? $"))
percentage = int(input ("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input ("How many people to split the bill? "))

percentage_calculator = 1 + (percentage / 100)

result = (total_bill * percentage_calculator) / people

result_conversion = round(result, 2)

print(f"Each person should pay: {result_conversion}")