# war card game
_A gambling two player card game_. 

Welcome to this project documentation. In the next sections you will find detailed information about the project itself, classes used, and methods defined to execute a complete game.

## Introduction:
This project was written in Python v3.10 using object-oriented programming, using also certain python modules as random, and os. This means _it should run without problems in any python 3.10.x version_ or higher. Nevertheless, if necessary, a [**requirements.txt**](https://github.com/Merchulian/war_card_game/blob/main/requirements.txt) is attached in order to create the very virtual environment using in its development.
The virtual environment can be created by downloading the [**requirements.txt**](https://github.com/Merchulian/war_card_game/blob/main/requirements.txt) file in your computer and running this command on a terminal:

pip install requirements.txt

## Game rules:
This is a two-player game. The objective of the game is to win every card in the game. At the beginning a 52 French deck is shuffled and then distributed evenly for the two opponents. To start the round (_battle_), every player draws the top card of his own stack (<span style="color:orange">playable stack</span>), and the winner is defined by value, as follows:

<center>

| Card description	| Card value    |
|:-----------------:|:-------------:|
| 2 - 10	        |Its own value  |
| “Jack”	        |      11       |
| “Queen”	        |      12       |
| “King”	        |      13       |
| “Ace”	            |      14       |

</center>

The winner takes both cards and put them into a his/her own <span style="color:coral">prisoner stack </span>. This is a different stack from the mentioned before, called the <span style="color:orange">playable deck </span>.<br>
In the case of a tie, a war begins: the cards drawn before becomes part of the <span style="color:MediumTurquoise">war loot</span> and a next card is played, in the case of a winner, he/she not only receives the war loot but the other player’s complete <span style="color:coral">prisoner stack </span>. If there is another tie, the war continues, and both played cards are also considered part of the <span style="color:MediumTurquoise">war loot</span>. <br>

The last round always triggers a war, and in case of tie, both players’ <span style="color:coral">prisoner stack </span> are shuffled, and the top card of each is played. This mechanic continues until there is a winner and the game finishes.
## Classes:
Main classes used to develop this game are:
### Card class:
Used to generate an object that stores the information of every card in a 52 cards French deck. The information of each element is the card value (2 to 14) and the suit (_Hearts_, _Diamonds_, _Clubs_ and _Spades_). This general card info is stored in a class attribute called _specials_ .
The card class also has a **show_card()** method to display the information, during the game. The suit attribute is defined using a **Suit** class which use a class attribute to store the suit info and description. This Suit class is a lesser class with the information needed to create a complete deck and display a card information.

### Deck class:
A Deck object is simply a list of card objects (deck._cards). Has no other attribute than that, but several methods to make a dynamic game.  
* **build()**:
The local build() method is used to generate the main game Deck, containing all 52 cards. This method is thought to be called while instancing a Deck object, and has a Boolean argument _autobuild_ in the constructor. In this case, to generate a complete deck, deck.autobuild need to be True. As the Deck class is also used to store player’s cards (the <span style="color:orange">playable stack</span> and the <span style="color:coral">prisoner stack </span>), the _autobuild = False_ is used to create an empty deck. The build() method creates in order 52 cards and assigning the corresponding values, following always the same order.
* **shuffle()**: this method is used to randomize the order of the game's main deck. 
* **add()** and **draw()**: these methods are mostly used for player’s deck. **draw()** removes a card on the top of the player’s Deck (last element of the Deck._cards list) and **add()**, adds the card in the bottom of player’s deck (first element of Deck._cards list). The **draw()** method is also used to make a play, first removing the card from their deck, then showing it, and then deciding who is the winner. Finally, **draw()** and **add()** are used to distribute cards to players, adding a card to the players' deck and drawing them fromthe main deck, at the beginning of the game.

### Player class:
Every player has a name, which can be entered by keyboard in case of a human player or can be chosen from a default list, for computer players. This name list is a class attribute called "_computer_names_". Every player has 4 attributes: 
1) name (_string object_) 
2) A Deck object with playable cards (_player.deck_) 
3) A prisoner stack (Deck object) to store previously won cards (_player.prisoner_stack_) 
4) The boolean _is_computer_ attribute, to define if the player is human or not.

By default, name is an empty string, giving the possibility to change to the user’s choice at the beginning of the game. The default value is also a way to define if the player is human or computer: an empty name is interpreted as a computer player, giving also the chance to watch 2 computer players battle.
There are several methods in this class, which are described below:
* **has_empty_deck()** <span style="color:Red">(_deprecated_)</span>: this method checks if a player has no card in his/her deck, this is mainly used to determine the winning condition and the winner/looser. The one with an empty deck loose
* **draw_card()** and **add_card()** <span style="color:Red">(_deprecated_)</span>: these are the methods for a player to draw the top card of his/her deck, or to add a card to his deck.These call the Card class  draw() and add() methods described before.

### Game class:
This class is intended to instantiate a new game. It has several attributes:
1) A main deck (_game.deck_)
2) Two player objects (_game.player_one_ and _game.player_two_).
3) A boolean attribute to determine the victory (_game.has_finished_).
4) A loot (Deck object), to store contested cards during a war(_game.loot_).
5) Another Player object to set te winner (_game.winner_)

It has several methods:

* **start_game()**: Uses the constructor to instantiate the Game object itself, and the data entry needed to define the two players and whether there’s a human player or two computers playing against. It also construct a complete deck for the game, shuffles it and distribute evenly into each player, <span style="color:orange">playable deck </span>.<br>

* **play_card()**: Implements the main mechanic of the game: the first card of each players’ deck is drawn, are removed from respective playable decks and to determine the winner their values are compared using the **game.compare_cards()** method described below. A monitor parameter is used to determine the last round: the boolean is_final which takes by default the value _False_. This monitor only changes its value to True when there is only one card on players’ decks. As can be observed in the code attached, this value is passed through further methods, in order to trigger the **game.last_round()** method. There is also another boolean called "_use_prisoners_", that takes the value _True_ when in the last round there is a tie. In this case, the **game.use_prisoners()** method is called.<br>
* **compare_cards()**: receives both played cards and defined by their value if there is a winner or there’s a tie. In case of a winner the method **set_winner()** is called and the loot is added to winner's <span style="color:orange">playable deck </span>. In case of a tie, the method **game.lets_war()** is invoked. <br>
* **set_winner()**: Having determined which card wins, this method adds the cards to the prisoner stack of the winner, removing both cards from the <span style="color:orange">playable deck </span>. Also, in the last round compares number of prisoners and set the _game.winner_ .<br>
* **lets_war()**: In case of a tie during **game.compare_cards()** method, **lets_war()** is called, it receives the played cards as an entry argument to set the war loot as a card list (to do so, **game.create_war_loot()** is used). To define the next round the  **game.play_card()** method is called again and in case of another tie, **game.lets_war()** method is called recursively adding the played cards to the _game.loot_ until there is a winner.<br>
* **Create_war_loot()**: In case of a war the two cards that triggered the war are stored in the _game.loot_ attribute and removed from both playable decks. The **game.play_card()** method is called again, and in case of another tie, the new pair of cards are appended to _game.loot_. <br>
* **Final_round()**: When there is only one card in both playable decks, those cards are compared and the winner is defined. But in case of a tie, the _game.use_prisoners()_ is called. <br>
* **Use_prisoners()**: in case of a tie in the last round this method is called, as there is no more playable cards, both each _player.prisoner_stack_ is shuffled and the first card in those list are played and compared. 

### main class
this main class (war.py) has only a few lines and is intended to call methods to instanciate Game, Player and other objects to start a new game. Using a while loop starts anew round until the game has finished, displaying on each round played cards, the winner and both players prisoners stacks. 
### View class
This class is used to generate a more user-friendly interface. it allows the user to see game rules, entry user's name and display basic information each round and game over screen. It is intended to be eliminated in a future version, in which a real user interface is pretended to be implemented. 


**Note: In this first version there are some tools created to control game flux, as print statements which will be removed in other game versions**."