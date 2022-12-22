import random

class Card:
  """
  Creates a Card object with the given suit and value

  Attributes:
  ----------
  suit: str
    suit of the card
  val: int
    value of the card
  """

  def __init__(self, s=None, v=None):
    """
    Contructs all necessary attributes for a Card object

    Parameters:
    ----------
      suit: str
            suit of the card
      val: int
            value of the card
    """

    self.suit = s
    self.val = v

  def __repr__(self):
    """
    Returns a Card object's representation in string format
    """

    return f"{self.val} of {self.suit}"

class Deck:
  """
  Creates a Deck object with 52 Cards

  Attributes:
  ----------
  cards: list
    card deck / list of Card objects

  Methods:
  --------
  def clone():
    Returns a copy of a Deck object
  
  def shuffle():
    Shuffles the deck

  def draw_card():
    Draws a card from the deck
  """

  def __init__(self):
    """Creates all necessary attributes for a Deck object"""

    self.cards = []
    for suit in ['h', 'd', 's', 'c']:
      for i in range(1, 15):
        self.cards.append(Card(suit, i))

  def clone(self):
    """Returns a copy of a Deck object"""

    d = Deck()
    d.cards = [card for card in self.cards]

    return d

  def shuffle(self):
    """Shuffles the Deck object"""

    random.shuffle(self.cards)

  def draw_card(self):
    """
    Draws a card form the Deck

    Returns:
    --------
    Card object:
      card drawn from the deck
    """

    if len(self.cards) == 0:
      return None
      
    return self.cards.pop()

class Game:
  """
  A class to represent a game, game logics, and methods of play

  Attributes:
  ----------
  cols: list
    The game area which consists of 4 columns

  deck: Deck
    A deck of cards

  Methods:
  --------
  def clone():
    Returns a copy of a Game object
  
  def play():
    Plays the game by calling appropriate functions until no more move is remaining.
    Returns the game score.
  
  def deal():
    Deals 4 cards

  def discard():
    Discard cards per the game rules

  def select_col_to_move_card_from():
    Returns the indices of the columns to move card from and to

  def move_card_up():
    Moves a card from one column to the empty column

  def score():
    Returns the game score
  
  def output():
    Prints games score and output message
  """

  def __init__(self, _deck):
    """
    Creates all attributes necessary to create a Game object

    Parameters:
    ----------
    _deck: Deck
      A deck of cards (shuffled)
    """

    self.cols = [[] for _ in range(4)]
    self.deck = _deck
  
  def clone(self):
    """Returns a copy of a Game object"""

    clone = Game(self.deck.clone())
    clone.cols = [col.copy() for col in self.cols]

    return clone

  def play(self):
    """
    Plays the game by calling appropriate functions until no more move is remaining.
    
    Returns:
    -------
    score: int
      Game score
    """

    while not self.discard():
      if not self.deal(): 
        return self.score()
      
    c_from, c_to = self.select_col_to_move_card_from()
    self.move_card_up(c_from, c_to)

    return self.play()
  
  def deal(self):
    """
    Deals 4 cards

    Returns:
    -------
    True if 4 cards are dealt.
    False if there are no cards in the Deck to deal
    """

    if not self.deck.cards:
      return False
    
    for col in self.cols:
      col.append(self.deck.draw_card())

    return True

  def discard(self):
    """
    Discard cards per the game rules

    Compares top row cards and discards cards until no more card can be discarded.
    
    Returns:
    -------
    True if, after discarding all possible cards, there is one or more columns with no cards and
    there are columns from which a card can be moved to the empty column(s) 
    (i.e. column has 2 or more cards). 

    False if above is not met
    """

    top_card = {'s':-1,'d':-1,'h':-1,'c':-1}
    poped = True
    
    while poped:
      poped = False

      for col in self.cols:
        if col:
          top_card[col[-1].suit] = max(top_card[col[-1].suit], col[-1].val)
      
      for col in self.cols:
        if col and top_card[col[-1].suit]>col[-1].val:
          col.pop()
          poped = True

    return any(len(col) == 0 for col in self.cols) and any(len(col)>1 for col in self.cols)

  def select_col_to_move_card_from(self):
    """ 
    Returns the indices of the columns to move card from and to

    Finds an empty column and selects which column to move card from based on following rules:

    1. if the last card of a column is an Ace card, move Ace up
    2. Otherwise, if the card on the 2nd row of a column has the same suit as 
       one or more cards on the top row, move card from this column
    3. If none of the above are met, the function returns the first adjecent column w/ 2 or more cards

    Returns:
    --------
    (col_from, col_to): tuple 
      index of the column which is available to move card from
      index of the column to move the card to (empty column).

      Returns (-1, -1), if no columns found w/ sufficeint card to move card from
    """

    # finds an empty column
    for i, col in enumerate(self.cols):
      if not col:
        c = i
        break

    # 1. if the last card of a column is an Ace card, move Ace up
    for i, col in enumerate(self.cols):
      if len(col) > 1 and col[-1].val == 14:
        return (i, c)

    # if the card on the 2nd row of a column has the same suit as 
    # one or more cards on the top row, move card from this column
    top_row_suits = {col[-1].suit for col in self.cols if col}

    for i, col in enumerate(self.cols):
      if len(col) > 1 and col[-2].suit in top_row_suits:
        return (i, c)
    
    # If none of prev is met, find the first adjecent column w/ 2 or more cards 
    c_from = (c+1)%4
    while len(self.cols[c_from]) < 2 and c_from != c:
      c_from = (c_from+1)%4
    
    if c_from != c:
      return (c_from, c)

    return (-1, -1)

  def move_card_up(self, c_from, c_to):
    """
    Moves a card from one column to the empty column

    Parameters:
    ----------
    c_from: int
      index of column to move card from

    c_to: int
      index of column to move card to
    
    Returns:
    -------
    True if card is moved up
    False if there are no card is moved (less than 2 cards in c_from)
    """

    if c_from>=0 and len(self.cols[c_from])>1:
      self.cols[c_to].append(self.cols[c_from].pop())
      return True
    
    return False

  def score(self):
    """ 
    Returns the game score per following:
    - Each Ace card on first row is +25
    - All other cards are -1

    Returns:
    -------
    score: int
      Game score
    """

    score = 0
    for col in self.cols:
      score -= len(col)
      if col and col[0].val == 14:
        score += 26

    return score
  
  def output(self, score):
    """Prints games score and output message"""

    if score <= 5:
      print("wow... that hurts! ", score, "%")
    elif score < 40:
      print("Maybe you need a new plan... ", score, "%")
    elif score < 60:
      print("Could happen or could not happen... no body knows! ", score, "%")
    elif score < 80:
      print("Getting closer! ", score, "%")
    elif score < 99:
      print("You've got the luck on your side! ", score, "%")
    elif score >= 99:
      print("This is all on you! If this doesn't happen, you've messed up big time! ", score, "%")

    return

class SimpleBacktrack(Game):
  """
  A child class of Game, representing a game which uses backtracking to play
  to optimize the game and score
  
  Attributes:
  ----------
  All Game attributes

  max_depth: int
    maximum depth of backtracking

  Methods:
  --------
  def clone():
    Returns a copy of a SimpleBacktrack object
  
  def backtrack(depth):
    Plays the game using backtracking
  """

  def __init__(self,_deck,_max_depth):
    """Creats all necessary attributes for a SimpleBacktack object."""

    super().__init__(_deck)   #calling parent __init__ function
    self.max_depth = _max_depth
  
  def clone(self):
    """Returns a copy of a SimpleBacktrack object"""

    clone = SimpleBacktrack(self.deck.clone(), self.max_depth)
    clone.cols = [col.copy() for col in self.cols]

    return clone

  def backtrack(self, depth):
    """ 
    Plays the game using backtacking.
    
    When a decision point is reached (i.e. a column has become empty and the game needs to decide form 
    which column a card should be moved up to the empty column), backtracking function plays all possible outcomes. 
    And returns the highest score possible.

    The depth of backtracking is limited by max_depth variable to limit the run time where there are many decision points. 
    After the max depth is reached, the game is played using parent (i.e. Game) Play() function which uses heuristic rules.

    Paremeters:
    ----------
    depth: int
      current depth of backtrack

    Returns:
    -------
    score: int
      Game score
    """

    while not self.discard():
      if not self.deal():
        return self.score()
    
    candidates = []
    for i, col in enumerate(self.cols):
      if not col:
        for j in range(4):
          if j != i:
            clone = self.clone()
            if clone.move_card_up(j, i):
              candidates.append(clone)
    
    return max(clone.backtrack(depth + 1) if depth<self.max_depth else clone.play() for clone in candidates)

# test
h = []
sbt = []
for i in range(100):
  d = Deck()
  d.shuffle()
  g = Game(d.clone())
  h += g.play(),
  sbt += SimpleBacktrack(d.clone(), 10).backtrack(0),

  # check - all scores from SimpleBacktrack should be equal or higher than heuristic approch
  if sbt[-1] < h[-1]:
    print('Problem!', 'sbt:', sbt[-1], 'h:', h[-1])

print('h =', h)
print('Heuristic Appraoch Average:', sum(h)/len(h))
print('\nsbt =', sbt)
print('Backtrack Average:', sum(sbt)/len(sbt))

