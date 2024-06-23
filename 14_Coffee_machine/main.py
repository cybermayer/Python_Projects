#Coffe machine control code

import math
import os

def clear() -> int:                                                            #Function to clear the console screen.
                        
                                                                                return os.system("cls")
    
def check_resource(ingredient, need, in_maschine, capacity) -> bool:           # function to check the avalaibe resources
    
                                                                                if need > in_maschine:
                                                                                    print(
                                                                                        f"The {ingredient} has run out. Please fill the {ingredient}container.")
                                                                                    result = False
                                                                                elif in_maschine < capacity*0.2:
                                                                                    print(
                                                                                        f"The {ingredient} will run out soon. Please fill the {ingredient}container.")
                                                                                    result = True
                                                                                else:
                                                                                    result = True
                                                                                    
                                                                                    return result

# Capacity of the machine for various ingredients
capacity = {

    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}

# Recipes and costs of the drinks available in the MENU
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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


# Initial quantities for coins and ingredients
profit = 0
penny_am = 50
nickel_am = 50
dime_am = 50
quarter_am = 50
water_am = capacity["water"]
milk_am = capacity["milk"]
coffee_am = capacity["coffee"]

# Flags to control different modes of operation
report_mode = False
in_change_mode = False
in_service = False
standby_mode = True
prompt = ""

# In standby mode, the machine is turned off but connected to electricity
while standby_mode == True:
    turn_in = input("Press the 'ON' button to turn maschine on")
    if turn_in == "on":
        clear()
        in_service = True
        print("Welcome!")

        # In service mode, the machine is turned on and ready for operations
        while in_service == True:

            # Cash inventory of the machine
            in_change = {

                "penny": [penny_am, 0.01,],
                "nickel": [nickel_am, 0.5],
                "dime": [dime_am, 0.10],
                "quarter": [quarter_am, 0.25],

            }

            # Ingredients inventory of the machine
            resources = {

                "water": water_am,
                "milk": milk_am,
                "coffee": coffee_am,
                "total": (in_change["penny"][0] * in_change["penny"][1]) + (in_change["nickel"][0] * in_change["nickel"][1]) + (in_change["dime"][0] * in_change["dime"][1]) + (in_change["quarter"][0] * in_change["quarter"][1])

            }

            #Prompting user to choose a drink or turn off the machine, enter report mode, or refill mode
        
                       
                       
            prompt = input("What would you like? Espresso(E), Latte(L), Cappuccino(C)?")

            # ESPRESSO
            if prompt == "E":

                resource_condition = False
                coin_condition = False
                execution_condition = False

                # Checking resources required for Espresso
                water_check = check_resource(
                    "water", MENU["espresso"]["ingredients"]["water"], resources["water"], capacity["water"])
                milk_check = True
                coffee_check = check_resource(
                    "coffee", MENU["espresso"]["ingredients"]["coffee"], resources["coffee"], capacity["coffee"])

                if water_check == True and milk_check == True and coffee_check == True:
                    resource_condition = True
                    inserted_money = 0
                                   
                    # Collecting money from user for Espresso
                    while inserted_money < (MENU['espresso']['cost']):
                        actual_coin = input(
                            f"Please insert {(MENU['espresso']['cost'])-inserted_money}$")
                        
                        # Updating cash inventory based on inserted coins
                        if actual_coin == "penny":
                            inserted_money += 0.01
                            penny_am += 1
                        elif actual_coin == "nickel":
                            inserted_money += 0.05
                            nickel_am += 1
                        elif actual_coin == "dime":
                            inserted_money += 0.10
                            dime_am += 1
                        elif actual_coin == "quarter":
                            inserted_money += 0.25
                            quarter_am += 1

                    if inserted_money == MENU['espresso']['cost']:
                        coin_condition = True

                    elif inserted_money > MENU['espresso']['cost']:
                        coin_back = inserted_money-(MENU['espresso']['cost'])
                        
                        # Returning extra money to user
                        print(f"Your money back: {coin_back}$")
                        
                        # Calculating and returning change in coins
                        qs_back = math.floor(coin_back / 0.25)
                        coin_back = coin_back % 0.25
                        ds_back = math.floor(coin_back / 0.10)
                        coin_back = coin_back % 0.10
                        ns_back = math.floor(coin_back / 0.05)
                        coin_back = coin_back % 0.05
                        ps_back = coin_back / 0.01
                        coin_back = 0

                        # Updating coin inventory based on returned change
                        while quarter_am > 0 and qs_back > 0:
                            quarter_am -= 1
                            qs_back -= 1

                        while dime_am > 0 and ds_back > 0:
                            dime_am -= 1
                            ds_back -= 1
                            if qs_back > 0:
                                dime_am -= math.floor((qs_back * 0.25)/0.10)
                                ns_back += ((qs_back*0.25) % 0.10) / 0.05

                        while nickel_am > 0 and ns_back > 0:
                            nickel_am -= 1
                            ns_back -= 1
                            if ds_back > 0:
                                nickel_am -= ds_back/2

                        while penny_am > 0 and ps_back > 0:
                            penny_am -= 1
                            ps_back -= 1
                            if ns_back > 0:
                                penny_am -= ns_back/5

                        coin_condition = True
                        
                # If resources and coins are sufficient, prepare and serve Espresso
                if resource_condition == True and coin_condition == True:

                    water_am -= (MENU["espresso"]["ingredients"]["water"])
                    milk_am = milk_am
                    coffee_am -= (MENU["espresso"]["ingredients"]["coffee"])
                    profit += MENU["espresso"]["cost"]

                    print("Your ESPRESSO is ready to take. Enjoy it!")

            # LATTE
            elif prompt == "L":

                resource_condition = False
                coin_condition = False
                execution_condition = False

                water_check = check_resource(
                    "water", MENU["latte"]["ingredients"]["water"], resources["water"], capacity["water"])
                milk_check = check_resource(
                    "water", MENU["latte"]["ingredients"]["milk"], resources["milk"], capacity["milk"])
                coffee_check = check_resource(
                    "coffee", MENU["latte"]["ingredients"]["coffee"], resources["coffee"], capacity["coffee"])

                if water_check == True and milk_check == True and coffee_check == True:
                    resource_condition = True
                    inserted_money = 0
                    
                    # Collecting money from user for Latte
                    while inserted_money < (MENU['latte']['cost']):
                        actual_coin = input(
                            f"Please insert {(MENU['latte']['cost'])-inserted_money}$")

                        # Updating cash inventory based on inserted coins
                        if actual_coin == "penny":
                            inserted_money += 0.01
                            penny_am += 1
                        elif actual_coin == "nickel":
                            inserted_money += 0.05
                            nickel_am += 1
                        elif actual_coin == "dime":
                            inserted_money += 0.10
                            dime_am += 1
                        elif actual_coin == "quarter":
                            inserted_money += 0.25
                            quarter_am += 1

                    if inserted_money == MENU['latte']['cost']:
                        coin_condition = True

                    elif inserted_money > MENU['latte']['cost']:
                        coin_back = inserted_money-(MENU['latte']['cost'])
                        
                        # Returning extra money to user
                        print(f"Your money back: {coin_back}$")

                        qs_back = math.floor(coin_back / 0.25)
                        coin_back = coin_back % 0.25
                        ds_back = math.floor(coin_back / 0.10)
                        coin_back = coin_back % 0.10
                        ns_back = math.floor(coin_back / 0.05)
                        coin_back = coin_back % 0.05
                        ps_back = coin_back / 0.01
                        coin_back = 0

                        while quarter_am > 0 and qs_back > 0:
                            quarter_am -= 1
                            qs_back -= 1

                        while dime_am > 0 and ds_back > 0:
                            dime_am -= 1
                            ds_back -= 1
                            if qs_back > 0:
                                dime_am -= math.floor((qs_back * 0.25)/0.10)
                                ns_back += ((qs_back*0.25) % 0.10) / 0.05

                        while nickel_am > 0 and ns_back > 0:
                            nickel_am -= 1
                            ns_back -= 1
                            if ds_back > 0:
                                nickel_am -= ds_back/2

                        while penny_am > 0 and ps_back > 0:
                            penny_am -= 1
                            ps_back -= 1
                            if ns_back > 0:
                                penny_am -= ns_back/5

                        coin_condition = True

                if resource_condition == True and coin_condition == True:

                    water_am -= (MENU["latte"]["ingredients"]["water"])
                    milk_am = milk_am
                    coffee_am -= (MENU["latte"]["ingredients"]["coffee"])
                    profit += MENU["latte"]["cost"]

                    print("Your LATTE is ready to take. Enjoy it!")

            # CAPPUCCINO
            elif prompt == "C":

                resource_condition = False
                coin_condition = False
                execution_condition = False

                water_check = check_resource(
                    "water", MENU["cappuccino"]["ingredients"]["water"], resources["water"], capacity["water"])
                milk_check = check_resource(
                    "water", MENU["cappuccino"]["ingredients"]["milk"], resources["milk"], capacity["milk"])
                coffee_check = check_resource(
                    "coffee", MENU["cappuccino"]["ingredients"]["coffee"], resources["coffee"], capacity["coffee"])

                if water_check == True and milk_check == True and coffee_check == True:
                    resource_condition = True
                    inserted_money = 0

                    while inserted_money < (MENU['cappuccino']['cost']):
                        actual_coin = input(
                            f"Please insert {(MENU['cappuccino']['cost'])-inserted_money}$")

                        if actual_coin == "penny":
                            inserted_money += 0.01
                            penny_am += 1
                        elif actual_coin == "nickel":
                            inserted_money += 0.05
                            nickel_am += 1
                        elif actual_coin == "dime":
                            inserted_money += 0.10
                            dime_am += 1
                        elif actual_coin == "quarter":
                            inserted_money += 0.25
                            quarter_am += 1

                    if inserted_money == MENU['cappuccino']['cost']:
                        coin_condition = True

                    elif inserted_money > MENU['cappuccino']['cost']:
                        coin_back = inserted_money-(MENU['cappuccino']['cost'])

                        print(f"Your money back: {coin_back}$")

                        qs_back = math.floor(coin_back / 0.25)
                        coin_back = coin_back % 0.25
                        ds_back = math.floor(coin_back / 0.10)
                        coin_back = coin_back % 0.10
                        ns_back = math.floor(coin_back / 0.05)
                        coin_back = coin_back % 0.05
                        ps_back = coin_back / 0.01
                        coin_back = 0

                        while quarter_am > 0 and qs_back > 0:
                            quarter_am -= 1
                            qs_back -= 1

                        while dime_am > 0 and ds_back > 0:
                            dime_am -= 1
                            ds_back -= 1
                            if qs_back > 0:
                                dime_am -= math.floor((qs_back * 0.25)/0.10)
                                ns_back += ((qs_back*0.25) % 0.10) / 0.05

                        while nickel_am > 0 and ns_back > 0:
                            nickel_am -= 1
                            ns_back -= 1
                            if ds_back > 0:
                                nickel_am -= ds_back/2

                        while penny_am > 0 and ps_back > 0:
                            penny_am -= 1
                            ps_back -= 1
                            if ns_back > 0:
                                penny_am -= ns_back/5

                        coin_condition = True

                if resource_condition == True and coin_condition == True:

                    water_am -= (MENU["cappuccino"]["ingredients"]["water"])
                    milk_am = milk_am
                    coffee_am -= (MENU["cappuccino"]["ingredients"]["coffee"])
                    profit += MENU["cappuccino"]["cost"]

                    print("Your CAPPUCCINO is ready to take. Enjoy it!")
                    
            # Turn off the maschine - enter the stand-by mode
            elif prompt == "off":
                in_service = False
                turn_in = ""
                print("Good Bye!")

            # Enter the reportmode
            elif prompt == "report":
                report_mode = True
                while report_mode == True:
                    #Command for in_change details: "detail" for step out report mode: "back"
                    print(f"The profit is: {profit} $")
                    repchoice = input(f"{resources}")

                    if repchoice == "detail":
                        in_change_mode = True
                        while in_change_mode == True:
                            #Command for step out into change mode: "back"
                            inchoice = input(
                                f"0.01$: {in_change['penny'][0]}   0,05$: {in_change['nickel'][0]}   0,10$: {in_change['dime'][0]}   0,25$: {in_change['quarter'][0]}")
                            if inchoice == "back":
                                in_change_mode = False
                                inchoice = ""
                                clear()
                    elif repchoice == "back":
                        repchoice = ""
                        prompt = ""
                        report_mode = False
                        clear()
            
            # Refill resources
            elif prompt == "refill":
                in_service = False
                standby_mode = False
