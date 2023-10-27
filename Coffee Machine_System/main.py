import coffee_maker
import money_machine
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
money = MoneyMachine()
item = Menu()

coffee.report()
money.report()
works = True

while works:
    options = item.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        works = False
    elif choice == "report":
        coffee.report()
        money.report()
    else:
        drink = item.find_drink(choice)
        if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
                coffee.make_coffee(drink)
