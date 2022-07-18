from Suit import Suit
class Card():
    #class attribute:

    specials ={"Jack": 11,
                "Queen": 12,
                "King": 13, 
                "Ace ": 14}

    #constructor
    def __init__(self, suit, value):
        if isinstance(suit, Suit) and value in range(1,15):
            self._suit = suit
            self._value = value
    #Getters and Setters
    @property
    def suit(self):
        return self._suit
    @suit.setter
    def suit(self, suit):
        if isinstance(suit, Suit):
            self._suit = suit

    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        self._value = value


    #Methods:
    def show_card(self):
        if (self.value <= 10):
            answer = f"{self.value} of {self.suit.description}.    "

        elif (11 <= self.value <= 14):
            for key, value in Card.specials.items():
                if self.value == value:
                    answer = f"{key} of {self.suit.description}. "
        return answer
                
    
    def is_special(self):
        if self._value <=10:
            answer = False
        else:
            answer = True
        return answer

