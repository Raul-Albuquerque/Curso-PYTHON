# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names = name1 + name2
names_to_lower = names.lower()

var_t = names_to_lower.count("t")
var_r = names_to_lower.count("r")
var_u = names_to_lower.count("u")
var_e = names_to_lower.count("e")

true = str(var_t + var_r + var_u + var_e)

var_l = names_to_lower.count("l") 
var_o = names_to_lower.count("o") 
var_v = names_to_lower.count("v") 
var_e = names_to_lower.count("e") 

love = str(var_l + var_o + var_v + var_e)
true_love = int(true + love)

if true_love < 10 or true_love > 90:
  print(f"Your score is {true_love}, you go together like coke and mentos.")

elif true_love > 40 and true_love < 50:
  print(f"Your score is {true_love}, you are alright together.")

else:
  print(f"Your score is {true_love}")