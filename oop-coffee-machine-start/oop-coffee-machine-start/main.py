from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
menu = Menu()
make_coffee = CoffeeMaker()
money_machine = MoneyMachine()

while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        make_coffee.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if make_coffee.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                make_coffee.make_coffee(drink)
    #print(drink.name)
 