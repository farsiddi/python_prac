# from menu import Menu, MenuItem
# from coffee_maker import Coffee Maker
# from money_machine import MoneyMachine
# 1 - Print Report
# Check resources sufficient ?
# Process coins
# Check transaction successful ?
# Make Coffee
from MoneyMachine import MoneyMachine
from Menu import MenuItem, Menu
from CoffeeMaker import CoffeeMaker

money_machine1 = MoneyMachine()
coffe_maker1 = CoffeeMaker()
menu1 = Menu()
# money_machine1.report()
# coffe_maker1.report()

is_on = True

while is_on:
    options = menu1.get_items()
    choice = input(f"What would you like to have- {options} or no")
    if choice == "no":
        is_on = False
    elif choice == "report":
        coffe_maker1.report()
        money_machine1.report()
    else:
        drink1 = menu1.find_drink(choice)
        print(drink1)
        if coffe_maker1.is_resource_sufficient(drink1):
            if money_machine1.make_payment(drink1.cost):
                coffe_maker1.make_coffee(drink1)
