
# This script generates a random password based on user inputs for the number of letters, numbers, and symbols.

import random

# Define the possible characters for the password
letters = "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z"
numbers = "0, 1, 2, 3, 4, 5, 6, 7, 8, 9"
specials = "~ ` ! @ # $ % ^ & * ( ) _ - + = { [ } ] | \ : ; ' < , > . ? /"

# Split the character strings into lists
arySpcls = specials.split(" ")
aryNmbrs = numbers.split(", ")
aryLttrs = letters.split(", ")

# Prompt the user for the number of letters, numbers, and symbols in the password
pwl = int(input("How many letters would you like? "))
pwn = int(input("How many numbers would you like? "))
pws = int(input("How many symbols would you like? "))

# Initialize the password variable
pw = ""

# Add the specified number of letters to the password
for n in range(pwl):
    x = random.randint(0, len(aryLttrs) - 1)
    pw += aryLttrs[x]

# Add the specified number of numbers to the password at random positions
for n in range(pwn):
    x = random.randint(0, len(aryNmbrs) - 1)
    NPart = aryNmbrs[x]
    y = random.randint(0, len(pw))
    pw = pw[:y] + NPart + pw[y:]

# Add the specified number of symbols to the password at random positions
for n in range(pws):
    x = random.randint(0, len(arySpcls) - 1)
    SPart = arySpcls[x]
    y = random.randint(0, len(pw))
    pw = pw[:y] + SPart + pw[y:]

# Print the generated password
print(pw)
