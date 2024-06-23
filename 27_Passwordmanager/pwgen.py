#region IMPORT

import random 

#endregion

#region INIT

letters = "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z"
numbers = "0, 1, 2, 3, 4, 5, 6, 7, 8, 9"
specials = "~ ` ! @ # $ % ^ & * ( ) _ - + = { [ } ] | \ : ; ' < , > . ? /"

#endregion 

class Password:

    """<DOC

        Represents a password generator.

            ATTRIBUTES:
                        - specials_list: List of special characters.
                        - numbers_list: List of number characters.
                        - letters_list: List of letter characters.

            METHODS:
                        - __init__ -> None
                        - generate -> str

    DOC?>"""

    def __init__(self):

        """<DOC

            Initialize the Password object with lists of characters.

        DOC?>"""

        self.specials_list = specials.split(" ")
        self.numbers_list = numbers.split(", ")
        self.letters_list = letters.split(", ")

    def generate(self, letter, number, special) -> str:

        """<DOC

            Generate a random password.

                PARAMS:
                        - letter: Number of letters in the password.
                        - number: Number of numbers in the password.
                        - special: Number of special characters in the password.

                RETURNS:
                        - str: Generated password.

        DOC?>"""

        pw = ""
        let = int(letter)
        num = int(number)   
        spec = int(special)

        for i in range(let):
            x = random.randint(0, len(self.letters_list)-1)
            pw = pw + self.letters_list[x]
        
        for i in range(num):
            z = random.randint(0, len(self.numbers_list)-1)
            npart = self.numbers_list[z]
            y = random.randint(0, len(pw))
            pw = pw[:y] + npart + pw[y:]
        
        for i in range(spec):
            k = random.randint(0, len(self.specials_list)-1)
            spart = self.specials_list[k]
            y = random.randint(0, len(pw))
            pw = pw[:y] + spart + pw[y:]

        return pw

