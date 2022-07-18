from Player import Player 
from Deck import Deck
class Game():

    def __init__(self, player_one_name ):

        self._player_one = Player(player_one_name)
        self._player_two = Player("")
        self._has_finished = False
        self._deck = Deck()
        self._loot = []
        self.winner = Player

    #Getters y Setters
    @property
    def deck(self):
        return Deck
    @deck.setter
    def deck(self, deck):
        if isinstance(deck, Deck):
            self._deck = deck
    @property
    def loot(self):
        return self._loot
    @loot.setter
    def loot(self, loot):
        if isinstance(loot, list):
            self._loot= loot
    @property
    def winner(self):
        return self.winner
    @property
    def has_finished(self):
        return self._has_finished
    @has_finished.setter
    def has_finished(self, has_finished):
        if isinstance(has_finished, bool):
            self._has_finished = has_finished
    @winner.setter
    def winner(self, winner):
        if isinstance(winner, Player):
            self._winner = winner

    # ======================================================================================================================
    # ============================================       METHODS       =====================================================
    # ======================================================================================================================   
    def start_game(self):
        self._deck.shuffle()
        print("deck shuffled")
        #Distribute!!! one to player 1 the other for player 2 and so on
        print("distributing cards")
        step = 1
        while(len(self._deck.cards) != 0):
            # take first card of the full deck and give it to player 1 (add to player_one.deck), then remove it from full_deck
            print(f"step: {step}")
            card = self._deck.cards[0]
            print(f"{card.show_card()} to player one")
            self._player_one.add_card(card)
            self._deck.cards.remove(self._deck.cards[0])
            print("card removed")
            # take first card of the full_deck and give it to player 2 (add to player_one.deck), then remove it from full_deck
            card = self._deck.cards[0]
            print(f"{card.show_card()} to player two")
            self._player_two.add_card(card)
            self._deck.cards.remove(self._deck.cards[0])
            print("card removed \n\n")
            step += 1
        print("Done!!!")

    #battle mechanic:
    def play_card(self):
        card_one = self._player_one._deck.cards[0]
        print("Player 1 has played:")
        print(card_one.show_card())
        card_two= self._player_two._deck.cards[0]
        print("Player 2 has played:")
        print(card_two.show_card())
        #define the loot    
        self.loot.append(card_one)
        self.loot.append(card_two)
        self._player_one._deck._cards.pop(0)
        self._player_two._deck._cards.pop(0)

        self.compare_cards(card_one, card_two, self.loot)



    def compare_cards(self, card_1, card_2, loot, is_final=False, use_prisoners=False):    
        if card_1.value > card_2.value:
            print(f"Player {self._player_one.name} has won this round!")
            self.set_winner(self._player_one, loot, is_final, use_prisoners)
        elif card_1.value < card_2.value:
            print(f"Player {self._player_two.name} has won this round!")
            self.set_winner(self._player_two, loot, is_final, use_prisoners)
        elif card_1.value == card_2.value:
            if len(self._player_one._deck._cards) > 1 and len(self._player_one._deck._cards) > 1:
                self.lets_war(loot)
            elif len(self._player_one._deck._cards) == 1 and len(self._player_one._deck._cards) == 1:
                self.final_round(loot)
            

    def set_winner(self, player, loot=[], is_final=False,use_prisoners=False):
        #both cards goes to the winner's prisoners_stack
        if isinstance(player, Player):
            for card in loot:
                player.prisoner_stack.cards.append(card)
            self.loot.clear()
            if is_final:
                if use_prisoners:
                    self.winner = player                    
                else:
                    if len(self._player_one.prisoner_stack.cards) > len(self._player_two.prisoner_stack.cards):
                        self.winner = self._player_one
                    elif len(self._player_one.prisoner_stack.cards) < len(self._player_two.prisoner_stack.cards):
                        self.winner = self._player_two
                    elif len(self._player_one.prisoner_stack.cards) == len(self._player_two.prisoner_stack.cards):
                        self.use_prisoners()
                    else:
                        pass
                self._has_finished = True


    def lets_war(self, loot):
            #we choose the top cards of players decks
            print("Let\'s war: ")
            card_one = self._player_one._deck.cards[0]
            print("Player 1 has played:")
            print(card_one.show_card())
            card_two= self._player_two._deck.cards[0]
            print("Player 2 has played:")
            print(card_two.show_card())
            #append two new cards on the loot
            loot.append(card_one)
            loot.append(card_two)
            
            self._player_one._deck.cards.pop(0)
            self._player_two._deck.cards.pop(0)
            
            #put all the prisoners as a part of the loot
            loot = self.create_war_loot(loot)
            #compares card values
            self._player_one._prisoner_stack.cards.clear()
            self._player_two._prisoner_stack.cards.clear()
            self.compare_cards(card_one , card_two, loot)
                        
    
    def create_war_loot(self, loot):
        for card in self._player_one.prisoner_stack.cards:
            loot.append(card)
        for card in self._player_two._prisoner_stack.cards:
            loot.append(card)

        return loot

    def final_round(self, loot=[]):
        card_1 = self._player_one.deck.cards[0]
        
        print(f"player one has played: {card_1.show_card()}")
        
        card_2 = self._player_two.deck.cards[0]
        
        print(f"player one has played: {card_2.show_card()}")
        
        self._player_one.prisoner_stack.cards.append(card_1)
        self._player_two.prisoner_stack.cards.append(card_2)
        
        input("Press enter to continue:")
        self.compare_cards(card_1, card_2, loot, True)
        
    def use_prisoners(self):
        print("using prisoners to define the game!!!")
        self._player_one._prisoner_stack.shuffle()
        self._player_two._prisoner_stack.shuffle()

        prisoner_1 = self._player_one._prisoner_stack.cards[0]
        prisoner_2 = self._player_two._prisoner_stack.cards[0]
        
        print(f"Player 1 has played {prisoner_1.show_card()}")
        print(f"Player 2 has played {prisoner_2.show_card()}")
        

        self.compare_cards(prisoner_1 , prisoner_2, True, True)


