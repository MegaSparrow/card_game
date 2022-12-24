# Card Game
This code creates, plays, and returns score of a card game.

## Game Rules
The game is played with one deck of cards, with four columns as the game area.
The aim of the game is to achieve the highest score possible by moving all Ace cards to the top of the columns and minimizing the number of cards remaining in the game area. 

The game starts with dealing four cards (one for each column). 
If there are two or more cards with the same suit on the last last row the highest card is kept and the rest are discarded.
Once there are no more cards to discard, four cards are drawn from the deck and place on each column. 
This is repeated until more cards are left in the deck.

In an event when all cards in a column are discarded, a card is moved from another column to the one with no cards. 
This is considered a decision point where the player (code) can maximize the score by selecting the best possible move.

An example is shown below.

![An example of a game play - part 1](https://user-images.githubusercontent.com/77254817/209414378-77bd7207-0121-41cc-a894-4f03a442cda8.png)

![an exmaple of a game play - part 2](https://user-images.githubusercontent.com/77254817/209414384-54b253ab-fb0b-42fb-bf07-9fa966945466.png)

## Score Calculation
The score is calculated once all the cards are dealt and no more card can be discarded. 
The score is calculated per the following:
- 25 scores are awared for ech ace at the top (first row)
- For all other cards remaining (including any aces not on the first row), 1 score is deducted

## Model
Four classes have been used to model the card game:
- Card: A class to represent a card
- Deck: A class to represent a deck of cards
- Game: A class to represent the logics used in the game
- SimpleBacktrack: A subclass of Game representing a Game which uses *backtracking* to optimize the score

