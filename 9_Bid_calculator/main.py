# Hidden bid auction

import os
from draw import gavel  #import a gavel-draw to print 


def clear() -> int:                                         #Function to clear the console (Windows)
    
                                                                return os.system('cls') 


def place_bid() -> None:                                    #Funtion the place a bid
    
                                                                name = str(input("What's your name?"))  
                                                                bid = float(input("What's the bid?$"))  
                                                                bids[name] = bid  

                                              
bids = {}                                                   #Dictionary to store bids
winnerbid = 0                                               #Initialize the variable to track the highest bid

clear()                                                   
print(gavel)  
place_bid()  
furtherbids = input("Is there any further bids? yes('y') or no('n')") 

while furtherbids == "y":
    clear()  
    place_bid()  
    furtherbids = input("Is there any further bids? yes('y') or no('n')")  
    clear()  

# Determine the winner
for bidder in bids:
    if winnerbid < bids[bidder]:
        winnerbid = bids[bidder]  
        winnername = bidder  

# Print the winner's information
print(f"The highest bid amount of ${winnerbid} was placed by {winnername}")

