# war card game
_A gambling two player card game_. 

Welcome to this project documentation. In the next sections you will find detailed information about the project itself, classes used, and methods defined to execute a complete game.

Introduction:
This project was written in Python v3.10 using object-oriented programming, using also certain python modules as random, and os. This means _it should run without problems in any python 3.10.x version_ or higher. Nevertheless, if necessary, a **requirements.txt** is attached in order to create the very virtual environment using in its development.
The virtual environment can be created by downloading the **requirements.txt** file in your computer and running this command on a terminal (in the downloaded file directory):


Game rules:
This is a two-player game. The objective of the game is to win every card in the game. At the beginning a 52 French deck is shuffled and then distributed evenly for the two opponents. To start the round (battle), every player draws the top card of his own stack (playable stack), and the winner is defined by value, as follows:
Card description	Card value
2 - 10	Its own value
“Jack”	11
“Queen”	12
“King”	13
“Ace”	14

The winner takes both cards and put them into a his/her own prisoner stack. This is a different stack from the mentioned before, called the playable stack. Next, another round begins.
In the case of a tie, a war begins: the cards drawn before becomes part of the war loot and a next card is played, in the case of a winner, he/she not only receives the war loot but the other player’s complete prisoner stack. If there is another tie, the war continues, and both played cards are also considered part of the war loot.
The last round always triggers a war, and in case of tie, both players’ prisoner stacks are shuffled, and the top card of each player’s prisoner stack is played. This mechanic continues until there is a winner and the game finishes.
Classes:
Main classes used to develop this game are:
Card class:
Used to generate an object that stores the information of every card in a 52 cards French deck. The information of each element is the card value (2 to 14) and the suit (hearts, diamonds, clubs and spades). This general card info is stored in a class attribute called “specials”.
The card class also has a show() method to display the information, during the game. The suit attribute is defined using a Suit class which use a class attribute to store the suit info and description.

Deck class:
A Deck object is simply a list of card objects (self._cards). Has no other attribute than that, but several methods to make a dynamic game.  
build():
The local build() method is used to generate the main game Deck, containing all 52 cards. This method is thought to be called while instancing a Deck object, if the Boolean argument autobuild in the constructor is True. As the Deck class is also used to store player’s cards, the autobuild = False is used to create an empty deck.
The build() method creates in order 52 cards and assigning the corresponding values, following always the same order.
shuffle(): this method is used to randomize the order of the game deck. 
add() and draw(): these methods are mostly used for player’s Deck: draw() removes a card on the top of the player’s Deck (last element of the Deck._cards list) and add(), adds the card in the bottom of player’s deck (first element of Deck._cards list). The draw() method is used to make a play, first removing the card from their deck, then showing it, and then deciding who is the winner. The draw() method is also used to distribute cards to players, from the main deck at the beginning of the game.

Player class:
Every player has a name, which can be entered by keyboard in case of a human player or can be chosen from a default list, for computer players. This name list is a class attribute called computer_names. Every player has 4 attributes: name (string), a Deck with playable cards and a prisoner_stack (Deck objects) and finally the is_computer Boolean attribute, to define if the player is human or not.
By default, name is an empty string, giving the possibility to change to the user’s choice at the beginning of the game. The default value is also a way to define if the player is human or computer: an empty name is interpreted as a computer player, giving also the chance to watch 2 computer players battle.
There are several methods in this class, which are described below:
has_empty_deck(): this method checks if a player has no card in his/her deck, this is mainly used to determine the winning condition and the winner/looser. The one with an empty deck loose
draw_card() and add_card(): these are the methods for a player to draw the top card of his/her deck, or to add a card to his deck.These call the Card class  draw() and add() methods described before.

Game class:
This class is intended to instantiate a new game,  has several attributes:
•	A main deck
•	Two players (human/ computer or computer/computer).
•	A boolean attribute to determine the victory (game.has_finished).
It has several methods:
•	Start_game():
Uses the constructor to instantiate the Game object itself, and the data entry needed to define the two players and whether there’s a human player or two computers playing against. It also construct a complete deck for the game, shuffles it and distribute evenly into each player, playable deck. 
•	Play_card(): 
implements the main mechanic of the game: the first card of each players’ deck is drawn, are removed from respective playable decks and to determine the winner their values are compared using the game.compare_cards() method. A monitor parameter is used to determine the last round: the boolean is_final which takes by default the value False. This monitor only changes its value to True when there is only one card on players’ decks. As can be observed in the code attached, this value is passed through further methods, triggering the game.last_round() method.
•	Compare_cards():
Calls the player methods to draw a card and, by their value define the winner or if there’s a tie. In case of a tie, the method game.lets_war() is invoked.
•	Set_winner():
Having determined which card wins, this method adds the cards to the prisoner stack of the winner, removing both cards from the playable decks.
•	Lets_war():
In case of a tie in the game.compare_cards() method, this method is called, it receives the played cards as an entry argument to set the war loot as a list (for this another method game.create_war_loot() is used). To define the next round the  game.play_card() method is called again and in case of another tie, game.lets_war() method is called recursively adding the played cards to the war loot until there is a winner.
•	Create_war_loot():
In case of a war the two cards that triggered the war are stored in the game.loot attribute and removed from both playable decks. The game.play_card() method is called again, and in case of another tie, the new pair of cards are appended to game.loot. 
•	Final_round():
When there is only one card in both playable decks, those cards are compared and the winner is defined. But in case of a tie, the game.use_prisoners() is called. 
•	Use_prisoners(): in case of a tie in the last round this method is called, as there is no playable cards both each player.prisoner_stack is shuffled and the first card in those list are played and compared. 

