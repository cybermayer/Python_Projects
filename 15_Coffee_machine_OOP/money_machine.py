class MoneyMachine:

    """<DOC

        Models a money machine that handles payments and profits.

            METHODS:    
                        -__init__ -> None
                        -report -> None
                        -process_coins -> float
                        -make_payment -> bool

    DOC?>"""

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self) -> None:

        """<DOC

            Initialize a MoneyMachine object.

        DOC?>"""

        #region CODE

        self.profit = 0
        self.money_received = 0

        #endregion CODE

    def report(self) -> None:

        """<DOC

            Prints the current profit

        DOC?>"""

        #region CODE

        print(f"Money: {self.CURRENCY}{self.profit}")

        #endregion CODE

    def process_coins(self) -> float:

        """<DOC

            Returns the total calculated from coins inserted.

                    RETURNS:    The total amount of money received from inserted coins

        DOC?>"""

        #region CODE

        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(
                input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

        #endregion CODE

    def make_payment(self, cost) -> bool:

        """<DOC

            Returns True when payment is accepted, or False if insufficient.

                    ARGS:    cost: The cost of the item being purchased

                    RETURNS:    True if payment is successful, False otherwise

        DOC?>"""

        #region CODE

        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False

        #endregion CODE
