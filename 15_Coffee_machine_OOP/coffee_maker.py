class CoffeeMaker:
  
    """#DOC

        Models the machine that makes the coffee.

            METHODS:     
                        -report
                        -is_resource_sufficient
                        -make_coffee
    DOC#"""                                                                          
     
    def __init__(self):                                        

        """<DOC

            Initialize the CoffeMaker-object

        DOC?>"""

        #region CODE

        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

        #endregion CODE

    def report(self) -> None:                                  
        
        """<DOC

            Prints a report of all resources.
        
        DOC?>"""

        #region CODE

        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

        #endregion

    def is_resource_sufficient(self, drink) -> bool:          
                                                                
        """<DOC
        
            Examines whether available resources is sufficient.

                    ARGS:     drink: The coffee type you want to drink 
                                    -ESPRESSO
                                    -LATTE
                                    -CAPUCHINO
                                        
                    RETRUN:    bool depending on sufficiency of resources      
            
        DOC?>"""                                                        

        #region CODE

        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
            
        return can_make

        #endregion
    
    def make_coffee(self, order) -> None:                                   
        
        """<DOC 

            Deducts the required ingredients from the resources.

                 ARGS:    order: The coffee type you want to order

        DOC?>"""                                                            

         #region CODE

        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")

         #endregion
