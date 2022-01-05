from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Menu = Menu()
MoneyMachine = MoneyMachine()
CoffeeMaker = CoffeeMaker()

is_on = True



while is_on:
    print("Welcome to the Coffee Machine. What would you like?")

    choice = input(Menu.get_items() + "\n")

    if choice == "off":
        is_on = False
    elif choice == "report":
        CoffeeMaker.report()
        MoneyMachine.report()
    else:
        drink = Menu.find_drink(choice)
        if CoffeeMaker.is_resource_sufficient(drink) and MoneyMachine.make_payment(drink.cost):
            CoffeeMaker.make_coffee(drink)


