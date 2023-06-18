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

#se ele escolher algum dos 3 cafés, fazer os cafés.
        # função para checar se tem recursos suficientes
            #se tem recursos suficientes para o café.

            #se não tiver recursos suficientes, retornar para o usuário o que está faltando.
def check_resources(users_choice):
    """Function that checks the machine resources"""
    water_machine = resources["water"]
    milk_machine = resources["milk"]
    coffee_machine = resources["coffee"]

    water_coffee = MENU[users_choice]['ingredients']["water"]
    milk_coffee = MENU[users_choice]['ingredients']["milk"]
    coffee = MENU[users_choice]['ingredients']["coffee"]

    if water_machine >= water_coffee and milk_machine >= milk_coffee and coffee_machine >= coffee:
        return True
    elif water_machine < water_coffee:
        return "Sorry, there is not enough water."
    elif milk_machine < milk_coffee:
        return "Sorry, there is not enough milk."
    elif coffee_machine < coffee:
        return "Sorry, there is not enough coffee."
    

# funcao para checar se o valor pago é suficiente para pagar o café.
            #se ele pagar o valor exato do café, retornar o café pronto.

            #se ele pagar um valor menor do que o preço do café, reportar que o valor pago é insuficiente.

            #se ele pagar um valor acima, devolver o troco.    
def check_payment(users_choice):
    "Function that checks the payment"
    quarters = float(input("How many quarters?: ")) * 0.25
    dimes = float(input("How many dimes?: ")) * 0.10
    nickles = float(input("How many nickles?: ")) * 0.05
    pennies = float(input("How many pennies?: ")) * 0.01

    coffee_cost = MENU[users_choice]["cost"]
    users_pay = quarters + dimes + nickles + pennies

    process_payment = round(users_pay - coffee_cost, 3)

    if process_payment == 0:
        return True
    elif process_payment > 0:
        print(f"Here is ${process_payment} in change.")
        return True
    elif process_payment < 0:
        return f"Sorry that's not enough money. Money refunded."

# função para preparar o café
            #se o valor for suficiente para pagar o café e tive os ingredientes, fazer o café.
#def make_coffee(users_choice):
def make_coffee(users_choice):
    return f"Here is your {users_choice} ☕. Enjoy!"

#receber a escolha do usuário
machine_is_on = True

while machine_is_on:
    users_choice = input("What would you like? (espresso, latte, cappuccino): ")
    #se ele escolher off, desligar a máquina.
    if users_choice == "off":
        machine_is_on = False
    #se ele escolher report, apresentar os recursos atuais.
    elif users_choice == "report":
        print(resources)
    else:
        check_1 = check_resources(users_choice)
        check_2 = check_payment(users_choice)
        if check_1 == True:
            if check_2 == True:
                print(make_coffee(users_choice))
            else:
                print(check_2)
        else:
            print(check_1)

        

        

    

    

