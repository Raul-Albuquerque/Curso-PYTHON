#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

age = input("What is your current age? ")

yearsLeft = 90 - int(age)

days = yearsLeft * 365
weeks = yearsLeft * 52
mounths = yearsLeft * 12

print(f"you have {days} days, {weeks} weeks, and {mounths} mounths left.")