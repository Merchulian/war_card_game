import random
from Deck import Deck
class Player():
    #list of computer opponents
    computer_names = ["Verónica", "Martín", "Alvaro", "Gómez", "Alicia", "Letitia", "Juan Alberto", "Olivia", "Miguel"]
    #contructor
    def __init__(self, name="" , deck=Deck() , is_computer=True):
        self._deck = Deck()
        self._prisoner_stack = Deck()    
        if name =="":
            name  = random.sample(Player.computer_names, 1)[0]
            self.name = name
        else:
            self.name = name
            self._is_computer = False

    #Getters and Setters
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
            self._name = name
    @property
    def deck(self):
        return self._deck

    @deck.setter
    def deck(self, deck):
        if isinstance(deck, Deck):
            self._deck = deck
    
    @property
    def prisoner_stack(self):
        return self._prisoner_stack
    @prisoner_stack.setter
    def prisoner_stack(self, deck):
        if isinstance(deck, Deck):
            self._deck = deck


    #Methods
    def has_empty_deck(self):
        answer = False
        if self._deck == None:
            answer = True
        return answer
    
    def draw_card(self):
        if not self.has_empty_deck():
            card = self.deck.cards[len(self.deck.cards-1)]
            self.deck.draw()
            return card
    
    def add_card(self, card):
        self.deck.add(card)