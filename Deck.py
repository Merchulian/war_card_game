from Card import Card
from Suit import Suit
import random
class Deck():
    
    def __init__(self, autobuild=False):
        #for game's full deck autobuild = True
        if autobuild:
            self._cards = self.build()
        # to instantiate player's own deck autobuild = False
        else:
            self._cards = []

    #Getter
    @property
    def cards(self):
        return self._cards
    @cards.setter
    def cards(self, cards):
        monitor = True
        if isinstance(cards, list):
            for i in range(len(cards)):
                if not isinstance(cards[i], Card):
                    monitor = False
                if monitor:
                    self._cards = cards
    
    #Methods:
    def build(self):
        #An empty deck
        my_cards= []
        # I use the suit dictionary to instance Suit class objects, to create the cards
        for key, value in Suit.suits.items():
            suit = Suit(key, value)
            # for every suit,there is assigned a value ( from 1 to 14) 
            for value in range(2,15):
                new_card = Card(suit, value)
                #the new cards is appended to the list
                my_cards.append(new_card)
        return my_cards

    def show(self):
        for item in self._cards:
            if isinstance(item, Card):
                print(item.show_card())

    def shuffle(self):
        self.cards = random.shuffle(self.cards)
    
    # These methods should help to modify players decks 
    def draw(self):
        self._cards.remove(self._cards[len(self._cards)-1])
        print("card removed from top")
    
    def add(self, card):
        if isinstance(card, Card):
            self._cards.insert(0, card) 
