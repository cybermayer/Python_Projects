class MenuItem:
  
    """#DOC

        Models each Menu Item.

            METHODS:     
                        -__init__

    DOC#"""
    
    def __init__(self, name, water, milk, coffee, cost):
        
        """<DOC

            Initialize a MenuItem object.

                    ARGS:     
                                name: The name of the menu item
                                water: The amount of water required for the item
                                milk: The amount of milk required for the item
                                coffee: The amount of coffee required for the item
                                cost: The cost of the item

        DOC?>"""

        #region CODE

        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

        #endregion CODE


class Menu:
    
    """#DOC

        Models the Menu with drinks.

            METHODS:     
                        -__init__
                        -get_items
                        -find_drink

    DOC#"""

    def __init__(self):
        
        """<DOC

            Initialize a Menu object.

        DOC?>"""

        #region CODE

        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

        #endregion CODE

    def get_items(self):
        
        """<DOC

            Returns all the names of the available menu items.

                    RETURNS:    A string containing names of menu items separated by '/'

        DOC?>"""

        #region CODE

        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options.rstrip('/')

        #endregion CODE

    def find_drink(self, order_name):
        
        """<DOC

            Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None.

                    ARGS:    order_name: The name of the drink to search for

                    RETURNS:    The MenuItem object if found, None otherwise

        DOC?>"""

        #region CODE

        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")

        #endregion CODE
