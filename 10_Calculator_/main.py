# Calculator

x = 0  # Initialize variable for first number
op = ""  # Initialize variable for operator

# Drawing of the calculator interface
draw0 = ("""
 _____________________
|  _________________  |
               0.00
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
""")

while x == 0:
    print(draw0)  # Print initial calculator interface
    x = float(input("Submit the first number: "))  # Prompt user for the first number
    print(f"""
 _____________________
|  _________________  |
              {x}
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
""")

    while x != 0:
        op = input("""Select the operator

    +
    -
    *
    /
    c

    """)  # Prompt user to select an operator

        if op == "c":
            x = 0  # If 'c' is chosen, reset x to 0 and restart the calculator

        else:
            y = float(input("Submit the next number: "))  # Prompt user for the next number

            if op == "+":
                x = x + y  # Addition operation
            elif op == "-":
                x = x - y  # Subtraction operation
            elif op == "*":
                x = x * y  # Multiplication operation
            elif op == "/":
                x = x / y  # Division operation

            # Print updated calculator interface with current result
            print(f"""
 _____________________
|  _________________  |
              {x}
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
""")

