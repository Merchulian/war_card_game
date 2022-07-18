import os
from Card import Card
from Game import Game

class View():
    def init(self):
        pass
        
        #==============================================           Methods           =========================================================

    def start_menu(self):
        os.system("clear")
        print("============================================================================================================")
        print("                                          WELCOME TO THIS GAME")
        print("============================================================================================================\n\n")
        opt = input("Press 1 to start game or 2 to see game rules: ")
        if opt != "1" and opt != "2":
            while(opt != "1" and opt != "2"):
                opt = input("press 1 to start or 2 to see game rules:")
        if opt == "2":
            self.display_rules()

    def status_view(self, game):
        if isinstance(game, Game):
            if len(game._player_one.prisoner_stack.cards) >= len(game._player_two.prisoner_stack.cards):
                max = len(game._player_one.prisoner_stack.cards)
                diff = len(game._player_one.prisoner_stack.cards) - len(game._player_two.prisoner_stack.cards)
                most = '1'
            else:
                max = len(game._player_two.prisoner_stack.cards)
                diff = len(game._player_two.prisoner_stack.cards) - len(game._player_one.prisoner_stack.cards)
                most = '2'
            
            print("=====================================================================================================")
            print("||                                          prisoner stacks                                         ||")
            print("=====================================================================================================")
            print("||                 player 1                      ||                    player 2                     ||")
            print("======================================================================================================")
            for index in range(max):
                if most == '1' :

                    print(f"{game._player_one._prisoner_stack.cards[index].show_card()}", "\t\t\t\t", f"||  {game._player_two._prisoner_stack.cards[index].show_card()}" if index <(max-diff) else "")
                    
                elif most == '2' :

                    print(f"{game._player_one._prisoner_stack.cards[index].show_card()}" if index <(max-diff) else "\t\t", "\t\t\t\t || ",f"{game._player_two._prisoner_stack.cards[index].show_card()}")
            print("=====================================================================================================")
            print("||                                          player 1 deck                                           ||")
            print("=====================================================================================================")
            index= 0
            for item in game._player_one._deck.cards:
                index += 1
                print(f"{index}) ",item.show_card()) 
            print("=====================================================================================================")
            print("||                                          player 2 deck                                           ||")
            print("=====================================================================================================")
            index = 0
            for item in game._player_two._deck.cards:
                index += 1
                print(f"{index}) ", item.show_card()) 
  

    def display_rules(self):
        os.system("clear")
        print("This is a two-player game. The objective of the game is to win every card in the game. At the beginning a 52 French deck is shuffled and then distributed evenly for the two opponents. To start the round (battle), every player draws the top card of his own stack (playable stack), and the winner is defined by value, as follows:")
        print("Card \t\t\t\t\t value")
        for item in range(2,11):
            print(f"{item} \t\t\t\t\t {item}")
        for key, value in Card.specials.items():
            print(f"{key} \t\t\t\t\t {value}")
        print("The winner takes both cards and put them into a his/her own prisoner stack. This is a different stack from the mentioned before, called the playable stack. Next, another round begins.\nIn the case of a tie, a war begins: the cards drawn before becomes part of the war loot and a next card is played, in the case of a winner, he/she not only receives the war loot but the other player’s complete prisoner stack. If there is another tie, the war continues, and both played cards are also considered part of the war loot.\nThe last round always triggers a war, and in case of tie, both players’ prisoner stacks are shuffled, and the top card of each player’s prisoner stack is played. This mechanic continues until there is a winner and the game finishes.\n\n")
        input("Press enter to continue: ")
        os.system("clear")
    
    def game_over(self, game):
        if isinstance(game, Game):
            os.system("clear")
            print("=====================================================================================================")
            print("||                                     GAME OVER                                                    ||")
            print("=====================================================================================================")
            print("\n\n\n\n\n")
            print(f"                               The winner is {game._winner.name}!!!!!!!!!")
            print("\n\n\n\n\n")
            input("press enter to continue")
        