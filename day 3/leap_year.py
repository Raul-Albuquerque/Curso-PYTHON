# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

check_one = year % 4
check_two = year % 100
check_three = year % 400

if check_one == 0:
    if check_two != 0:
        print("Leap year.")
    else:
        if check_three == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
elif check_three == 0:
    print("Leap year.")
else:
    print("Not leap year.")