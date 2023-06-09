print("Welcome to the rollercoaster!")

height = int(input("What is your heigh in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!!")
    age = int(input("How old are you?"))
    if age < 12:
      print("please pay $5.")
    elif age <= 18:
      print("Please pay $7")
    else:
      print("please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")
