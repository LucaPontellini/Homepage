import random

print ("Welcome to the seven-and-a-half!")
answer = input ("Do you want to play? '")

if answer == "Yes":

    answer_1 = str (input ("Enter your name: '"))
    print (f"Hello {answer_1}, let's start the game!")

    deck = {"seed": None,
            "value": None
            } #stampa il contenuto presente nel deck

    def create_a_deck (seeds: list, values: list) -> list [dict]:

        """This function creates a deck of 40 cards, each one with a seed and a value"""


        while len (deck) < 40:

            values = [1,2,3,4,5,6,7,8,9,10,0.5]
            seeds = ["Monies" , "Cups" , "Sticks" , "Swords"]
    
            for seed in seeds:
                for value in values:

                    card = {"seed": None,
                            "value": None
                            }

                    card.update ({"seed" : random.choice (seeds), "value" : random.choice (values)})
                    deck ["seed"] = card ["seed"]
                    deck ["value"] = card ["value"]

                    print (f"This is the deck: {deck}")

            return deck

    def deck_shuffle (deck: list [dict]):
        
        """This function shuffles the deck of cards""" 

        for _ in range (random.randint (5,10)):
            random.shuffle (deck)

            deck = create_a_deck
            deck_shuffle (deck)

        return deck_shuffle (deck)
    
    print (f"This is the shuffled deck: {deck}")

    answer_2 = str (input ("Enter the number of money you want to bet: '"))
    print (f"You bet {answer_2} money")

    answer_3 = str (input ("Do you want to extract a card? '"))

    if answer_3 == "Yes":

        def card_extraction (deck: list [dict]) -> dict:

            """This function extracts a card from the deck"""

            card = random.choice (deck)
            print (f"This is the card you extracted: {card}")

            return card
    
    elif answer_3 == "No":
        print ("Ok, maybe another time")
    
    else: "Error. Please, type 'Yes' or 'No'"

    def player_s_turnRound (deck: list [dict]) -> float:

        """This function represents the player's turn round""" 

        player_s_turnRound = 0
        player_s_turnRound += card_extraction (deck)

        return player_s_turnRound

elif answer == "No":
    print ("Ok, maybe another time")

else: "Error. Please, type 'Yes' or 'No'"