import random

cards_enum = "A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K"                   #Enumerating all possible cards in a deck
cards = cards_enum.split(", ")

cards_values = {                                                        #Dictionary mapping card values
    "A": 11,  # Ace can be 11 or 1 (handled later)
    "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9,
    "10": 10, "J": 10, "Q": 10, "K": 10,
}

def draw_a_card():                                                      #Function to draw a random card
    
                                                                            selected_card = random.choice(cards)
                                                                            return selected_card


def calc_cardvalue(actual_card):                                        # Function to calculate the value of a card
    
                                                                            card_value = cards_values[actual_card]
                                                                            return card_value

want_to_play = input("Do you want to play BLACKJACK? yes(y) or no(n)")

# Welcome screen
print("""
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\.
                       _/ |                
                      |__/ 

""")

while want_to_play == "y":
    # Initialize player's and dealer's hands
    your_hand = []
    your_hand_value = 0
    your_ace_count = 0

    dealer_hand = []
    dealer_hand_value = 0
    dealer_ace_count = 0

    actual_card = ""
    actual_value = 0

    # Initial deal: Player gets two cards
    for i in range(2):
        actual_card = draw_a_card()
        actual_value = calc_cardvalue(actual_card)
        your_hand.append(actual_card)
        your_hand_value += actual_value
        if actual_card == "A":
            your_ace_count += 1
    print(f"Your hand is: {your_hand}. The value is {your_hand_value}")

    # Dealer gets one visible card
    actual_card = draw_a_card()
    actual_value = calc_cardvalue(actual_card)
    dealer_hand.append(actual_card)
    dealer_hand_value += actual_value
    if actual_card == "A":
        dealer_ace_count += 1
    print(f"Your dealer's hand is: {dealer_hand}. The value is {dealer_hand_value}")

    # Check if player has a natural blackjack (21)
    if your_hand_value == 21:
        print("Congratulations you win!")
    else:
        # Player's turn to choose hit or stand
        while your_hand_value <= 21:
            go_on = input("Take your choice: hit(h) or stand(s)")

            if go_on == "h":
                actual_card = draw_a_card()
                actual_value = calc_cardvalue(actual_card)
                your_hand.append(actual_card)
                your_hand_value += actual_value

                # Handling Aces when player's total exceeds 21
                if your_hand_value > 21 and your_ace_count > 0:
                    your_ace_count -= 1
                    your_hand_value -= 10

                print(f"Your hand is: {your_hand}. Your hand's value is {your_hand_value}")

                # Check if player wins by reaching exactly 21
                if your_hand_value == 21:
                    print("Congratulations you win!")
                    break

                # Check if player busts (exceeds 21)
                elif your_hand_value > 21:
                    print(f"Your hand's value is {your_hand_value}. The dealer wins!")
                    break

            elif go_on == "s":
                break

    # If player hasn't busted, it's now dealer's turn
    if your_hand_value < 21:
        while dealer_hand_value < your_hand_value:
            actual_card = draw_a_card()
            actual_value = calc_cardvalue(actual_card)
            dealer_hand.append(actual_card)
            dealer_hand_value += actual_value

            # Check if dealer busts and adjust for Aces
            if dealer_hand_value > 16 and dealer_hand_value == your_hand_value:
                print("It's a draw!")
                break

            if dealer_hand_value == 21:
                print("The dealer wins!")
                break

            elif dealer_hand_value > 21:
                if dealer_ace_count > 0:
                    dealer_ace_count -= 1
                    dealer_hand_value -= 10
                print(f"The dealer's hand: {dealer_hand}. The dealer's hand's value is {dealer_hand_value}")

            if dealer_hand_value > 21:
                print(f"The dealer's hand's value is {dealer_hand_value}. Congratulations you win!")
                break

        print(f"The dealer's hand's value is {dealer_hand_value}. The dealer wins!")

    # If player busts in the first deal
    elif your_hand_value > 21:
        print(f"Your hand's value is {your_hand_value}. The dealer wins!")

    want_to_play = input("Do you want to play one more game? yes(y) or no(n)")

    # Goodbye message
    print("""
            _____
           |\ ~ /|
           |||:|||
           |||:|||  _____
           |||:||| |Joker|
           |/_~_\| |==%, |
                   | \/>\|
      ejm98        | _>^^|           _____
         _____     |/_\/_|    _____ |6    |
        |2    | _____        |5    || ^ ^ |
        |  ^  ||3    | _____ | ^ ^ || ^ ^ | _____
        |     || ^ ^ ||4    ||  ^  || ^ ^ ||7    |
        |  ^  ||     || ^ ^ || ^ ^ ||____9|| ^ ^ | _____
        |____Z||  ^  ||     ||____S|       |^ ^ ^||8    | _____
               |____E|| ^ ^ |              | ^ ^ ||^ ^ ^||9    |
                      |____h|              |____L|| ^ ^ ||^ ^ ^|
                                  _____           |^ ^ ^||^ ^ ^|
                          _____  |K  WW|          |____8||^ ^ ^|
                  _____  |Q  ww| | ^ {)|                 |____6|
           _____ |J  ww| | ^ {(| |(.)||| _____
          |10 ^ || ^ {)| |(.)||| | |||%||A .  |
          |^ ^ ^||(.)% | | |||%| |_||%>|| /.\ |
          |^ ^ ^|| | % | |_||%O|        |(_._)|
          |^ ^ ^||__||[|                |  |  |
          |___0I|                       |____V|
                                     _____
         _____                _____ |6    |
        |2    | _____        |5    || & & |
        |  &  ||3    | _____ | & & || & & | _____
        |     || & & ||4    ||  &  || & & ||7    |
        |  &  ||     || & & || & & ||____9|| & & | _____
        |____Z||  &  ||     ||____S|       |& & &||8    | _____
               |____E|| & & |              | & & ||& & &||9    |
                      |____h|              |____L|| & & ||& & &|
                                  _____           |& & &||& & &|
                          _____  |K  WW|          |____8||& & &|
                  _____  |Q  ww| | o {)|                 |____6|
           _____ |J  ww| | o {(| |o o||| _____
          |10 & || o {)| |o o||| | |||%||A _  |
          |& & &||o o% | | |||%| |_ww%>|| ( ) |
          |& & &|| | % | |_||%O|        |(_'_)|
          |& & &||__||[|                |  |  |
          |___0I|                       |____V|
                                     _____
         _____                _____ |6    |
        |2    | _____        |5    || v v |
        |  v  ||3    | _____ | v v || v v | _____
        |     || v v ||4    ||  v  || v v ||7    |
        |  v  ||     || v v || v v ||____9|| v v | _____
        |____Z||  v  ||     ||____S|       |v v v||8    | _____
               |____E|| v v |              | v v ||v v v||9    |
                      |____h|              |____L|| v v ||v v v|
                                  _____           |v v v||v v v|
                          _____  |K  WW|          |____8||v v v|
                  _____  |Q  ww| |   {)|                 |____6|
           _____ |J  ww| |   {(| |(v)||| _____
          |10 v ||   {)| |(v)||| | v||%||A_ _ |
          |v v v||(v)% | | v||%| |_||%>||( v )|
          |v v v|| v % | |_||%O|        | \ / |
          |v v v||__||[|                |  .  |
          |___0I|                       |____V|
                                     _____
         _____                _____ |6    |
        |2    | _____        |5    || o o |
        |  o  ||3    | _____ | o o || o o | _____
        |     || o o ||4    ||  o  || o o ||7    |
        |  o  ||     || o o || o o ||____9|| o o | _____
        |____Z||  o  ||     ||____S|       |o o o||8    | _____
               |____E|| o o |              | o o ||o o o||9    |
                      |____h|              |____L|| o o ||o o o|
                                  _____           |o o o||o o o|
                          _____  |K  WW|          |____8||o o o|
                  _____  |Q  ww| | /\{)|                 |____6|
           _____ |J  ww| | /\{(| | \/||| _____
          |10 o || /\{)| | \/||| |  ||%||A ^  |
          |o o o|| \/% | |  ||%| |_||%>|| / \ |
          |o o o||   % | |_||%O|        | \ / |
          |o o o||__||[|                |  .  |
          |___0I|                       |____V|
ejm

""")


print("I hope you come back soon!")
