# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
random_name = random.randint(0, len(names))
who_pays = names[random_name]
print(f"{who_pays} is going to buy the meal today!")