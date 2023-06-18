MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" : 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

current_resources = {}
def count_resources(machine_comand):
    """Funtion that count the resources"""
    coffee_water = MENU[machine_comand]["ingredients"]['water']
    coffee_milk = MENU[machine_comand]["ingredients"]['milk']
    coffee = MENU[machine_comand]["ingredients"]['coffee']

    machine_water = resources["water"]
    machine_milk = resources["milk"]
    machine_coffee = resources["coffee"]

    if machine_comand != "report":
        current_resources = {
            "water": machine_water - coffee_water,
            "milk": machine_milk - coffee_milk,
            "coffee": machine_coffee - coffee,
        }
    else:
        current_resources = resources
    return current_resources


def machine_comands(command):
    """Function that return the command of the user"""
    if command == "report":
        return "report"
    elif command == "espresso":
        return "espresso"
    elif command == "latte":
        return "latte"
    elif command == "cappuccino":
        return "cappuccino"


def count_coins(MENU, machine_comand):
    """Function that process the payment"""
    quarters = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickles = float(input("How many nickles? "))
    pennies = float(input("How many pennies? "))

    total_quarters = quarters * 0.25, 2
    total_dimes = dimes * 0.10
    total_nickles = nickles * 0.05
    total_pennies = pennies * 0.01

    total_inserted = total_quarters + total_dimes + total_nickles + total_pennies, 2
    coffee_price = MENU[machine_comand]['cost'], 2
    payment = total_inserted - coffee_price, 2

    if payment == 0:
        return f"Here is your {machine_comand} ☕. Enjoy!"
    elif payment > 0:
        return f"Here is ${payment} in change."
    elif payment < 0:
        return f"Sorry that's not enough money. Money refunded."


#ASK THE USER 

############### LOGIC ###########################

#perguntar o usuário qual vai ser a escolha dele
machine_is_on = True
while machine_is_on:
    users_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    machine_comand = machine_comands(users_choice)
    if users_choice == "report":
        print(count_resources(machine_comand))
    print(count_coins(MENU, machine_comand))
    print(count_resources(machine_comand))


