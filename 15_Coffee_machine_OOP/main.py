from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_m = MoneyMachine() #Initialize Moneymachine-object            
coffee_m = CoffeeMaker() #Initialize CoffeeMaker-object
menu = Menu() #Initialize Menu-object

turn_on = True

while turn_on == True:
    options = menu.get_items()
    choice = input(f"What would you like {options}?")
    if choice == "off":
        turn_on = 0
    elif choice == "report":
        money_m.report()
        coffee_m.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_m.is_resource_sufficient(drink) and money_m.make_payment(drink.cost):
            coffee_m.make_coffee(drink)
