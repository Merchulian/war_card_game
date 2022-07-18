import os
from View import View
from Deck import Deck
from Game import Game
# =========================================================================================================================
# ==============================================     MAIN CLASS    ========================================================
# =========================================================================================================================


def run():
    os.system("clear")
    view = View()
    view.start_menu()
    os.system("clear")

    name = input("please enter your name: ")
    #intantiate objects to create a new game
    full_deck = Deck(True)
    new_game = Game(name)
    new_game._deck = full_deck
    print("game created!!")
    print("let's start this game")
    new_game.start_game()
    input("press enter to continue")

 # ========================================================================================================================
 #                                                     GAME 
 # ========================================================================================================================
    
    index = 0
    while(not new_game._has_finished):
        os.system("clear")
        index += 1
        print("A new round beggins!!")
        print(f"Round {index}")
        if len(new_game._player_one._deck.cards) > 1 and len(new_game._player_two._deck.cards) > 1:
            new_game.play_card()

            view.status_view(new_game)
            
            input("press enter to continue")
        elif len(new_game._player_one._deck.cards) == 1 or len(new_game._player_two._deck.cards) == 1:
            print("FINAL ROUND")
            new_game.final_round()

    # when the game finishes:
    view.game_over(new_game)


if __name__ == "__main__":
    run()


