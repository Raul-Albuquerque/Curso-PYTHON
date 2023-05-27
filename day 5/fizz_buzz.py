#Write your code below this row 👇
for number in range(1, 101):
    fizz = number % 3
    buzz = number % 5
    if fizz == 0 and buzz == 0:
        number = "FizzBuzz"
    elif fizz == 0:
        number = "Fizz"
    elif buzz == 0:
        number = "Buzz"
    print(number)