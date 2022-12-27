# Card Game
This code creates, plays, and returns score of a card game.

## Game Rules
The goal of the game is to move all the Ace cards to the top of the four columns with the fewest remaining cards in the game area, in order to earn the highest score possible. 

The game begins by dealing one card to each of the four columns. If there are two or more cards with the same suit on the bottom row, the highest card is kept and the others are discarded. Once all the cards that can be discarded have been removed, four new cards are drawn from the deck and placed in each column. This process is repeated until there are no more cards left in the deck. 

If all the cards in a column are discarded, a card from another column is moved to the empty one. This is a key point where the player (code) can make the best move to maximize the score.

An example of a play is shown below.

![An example of a game play - part 1](https://user-images.githubusercontent.com/77254817/209414378-77bd7207-0121-41cc-a894-4f03a442cda8.png)

![an exmaple of a game play - part 2](https://user-images.githubusercontent.com/77254817/209414384-54b253ab-fb0b-42fb-bf07-9fa966945466.png)

## Score Calculation
The score is calculated when all the cards have been dealt and no more cards can be discarded. 
The score is determined according to the following rules:

- 25 points are awarded for each Ace at the top (first row)
- For all other remaining cards (including any Aces not in the first row), 1 point is subtracted.

## Modeling
Four classes have been used to model the card game:
- Card: A class to represent a playing card
- Deck: A class to represent a deck of cards
- Game: A class to represent the logics used in the game
- SimpleBacktrack: A subclass of Game representing a Game which uses *backtracking* to optimize the score

