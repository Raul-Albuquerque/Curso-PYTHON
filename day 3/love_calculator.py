# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

true = 0
love = 0

var_t = lower_case_name1.count("t")
var_t2 = lower_case_name2.count("t")
var_r = lower_case_name1.count("r")
var_r2 = lower_case_name2.count("r")
var_u = lower_case_name1.count("u")
var_u2 = lower_case_name2.count("u")
var_e = lower_case_name1.count("e")
var_e2 = lower_case_name2.count("e")
var_l = lower_case_name1.count("l")
var_l2 = lower_case_name2.count("l")
var_o = lower_case_name1.count("o")
var_o2 = lower_case_name2.count("o")
var_v = lower_case_name1.count("v")
var_v2 = lower_case_name2.count("v")
var_e = lower_case_name1.count("e")
var_e2 = lower_case_name2.count("e")

true = str(var_t + var_r + var_u + var_e + var_t2 + var_r2 + var_u2 + var_e2)
love = str(var_l + var_o + var_v + var_e + var_l2 + var_o2 + var_v2 + var_e2)

result = true + love
result = int(result)

if result <= 10 or result >= 90:
    result = str(result)
    print(f"Your score is {result}, you go together like coke and mentos.")

elif result >= 40 and result <= 50:
    result = str(result)
    print(f"Your score is {result}, you are alright together.")

else:
    result = str(result)
    print(f"Your score is {result}")