
# This script helps you calculate the amount each person needs to pay, including the tip, when splitting a bill.

# Prompt the user to input the total amount of the bill
fltBill = float(input("What's the total amount of the bill? $"))

# Prompt the user to input the percentage tip they would like to give and convert it to a multiplier
fltTip = float(1 + (0.01 * float(input("What percentage tip would you like to give?"))))

# Prompt the user to input the number of people to split the bill
fltPpl = float(input("How many people to split the bill?"))

# Calculate the total amount each person needs to pay
fltTotal = (fltBill * fltTip) / fltPpl

# Print the amount each person needs to pay, rounded to 2 decimal places
print(round(fltTotal, 2))
