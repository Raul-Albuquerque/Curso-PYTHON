from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
while is_on:
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if drink == "off":
        is_on = False
    elif drink == "report":
        report = CoffeeMaker().report()
        print(report)
    else:
        enough_resources = CoffeeMaker().is_resource_sufficient(drink)
        print(enough_resources)