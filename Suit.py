class Suit():
    #class attributes: 

    suits = {"Clubs ":"♧", 
            "Diamonds": "♢",
            "Spades": "♤",
            "Hearts": "♡"}
    #Constructor
    def __init__(self, description, symbol):
        self._description = description
        self._symbol = symbol
    #Getters and Setters
    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, description):
        if description in Suit.suits.keys():
            self._description = description

    @property
    def symbol(self):
        return self._symbol
    @symbol.setter
    def symbol(self, symbol):
        if symbol in Suit.suits.values():
            self._symbol = symbol