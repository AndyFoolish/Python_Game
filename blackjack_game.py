# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
deck = []
dealer = []
player = []
# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        string = "Hand contains "
        for card in self.hand:
            string += str(card) + " "
        return string  

    def add_card(self, card):
        self.hand.append(card)
        return self.hand

    def get_value(self):
        self.value = 0
        self.aces = 0
        for card in self.hand:
            self.value += VALUES.get(card.get_rank())
            if card.get_rank() == 'A':
                self.aces += 1
        if self.aces == 0:
            return self.value
        else:
            if self.value + 10 <= 21:
                return self.value + 10
            else:
                return self.value    
            
    def draw(self, canvas, pos):
        for card in self.hand:
            card.draw(canvas, pos)
            pos[0] += 100
        if in_play:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [136.5, 229], CARD_BACK_SIZE)
 
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit,rank))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        self.deal = self.deck.pop()
        return self.deal

    def __str__(self):
        string = "Deck contains "
        for card in self.deck:
            string = string + str(card) + " "
        return string

#define event handlers for buttons
def deal():
    global outcome, in_play, deck, dealer, player, score 
    if in_play:
        score -= 1
        outcome = "You didn't finish your last game. New deal now. Hit or Stand?"
    else:
        outcome = "New deal. Hit or Stand?"
    deck = Deck()
    dealer = Hand()
    player = Hand()
    dealer.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    in_play = True

def hit():
    global in_play, outcome, score
    if in_play:
        outcome = "Hit or Stand?"
        player.add_card(deck.deal_card())
        if player.get_value() > 21:
            outcome = "You went bust and lose. New deal?"
            in_play = False
            score -= 1
    else:
        outcome = "This hand is already over. Please do the new deal."
       
def stand():
    global in_play, outcome, score
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        if dealer.get_value() > 21:
            outcome = "The dealer busted. You win. New deal?"
            in_play = False
            score += 1
        elif dealer.get_value() < player.get_value():
            outcome = "You win. New deal?"
            in_play = False
            score += 1    
        elif dealer.get_value() >= player.get_value():
            outcome = "You lose. New deal?"
            in_play = False
            score -= 1    
    else:
        outcome = "This hand is already over. Please do the new deal."

# draw handler    
def draw(canvas):
    canvas.draw_text('Blackjack', [60, 80], 50, 'Yellow')
    canvas.draw_text('Dealer', [100, 160], 36, 'Black')
    canvas.draw_text('Player', [100, 380], 36, 'Black')
    canvas.draw_text('Score ' + str(score), [500, 100], 40, 'Black')
    canvas.draw_text(outcome, [40, 330], 24, 'Black')
    dealer.draw(canvas, [100, 180])
    player.draw(canvas, [100, 400])

# initialization frame
frame = simplegui.create_frame("Blackjack", 800, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()
















#other students' code
# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (128, 180)
CARD_CENTER = (CARD_SIZE[0]/2, CARD_SIZE[1]/2)
card_images = simplegui.load_image("https://dl.dropboxusercontent.com/u/3082546/py/blackjack/abcg.gif")

CARD_BACK_SIZE = (127, 180)
CARD_BACK_CENTER = (CARD_BACK_SIZE[0]/2, CARD_BACK_SIZE[1]/2)
card_back = simplegui.load_image("https://dl.dropboxusercontent.com/u/3082546/py/blackjack/card_back.gif")

# Some extras ;)
title = simplegui.load_image("https://dl.dropboxusercontent.com/u/3082546/py/blackjack/title.gif")
dealer_t = simplegui.load_image("https://dl.dropboxusercontent.com/u/3082546/py/blackjack/dealer.gif")
player_t = simplegui.load_image("https://dl.dropboxusercontent.com/u/3082546/py/blackjack/player.gif")
WIN = simplegui.load_image("https://dl.dropboxusercontent.com/u/3082546/py/blackjack/win.gif")
LOOSE = simplegui.load_image("https://dl.dropboxusercontent.com/u/3082546/py/blackjack/loose.gif")
status = None


CARD_OFFSET = 2
CANVAS_W = 7*CARD_SIZE[0]
CANVAS_H = 3*CARD_SIZE[1]

# initialize some useful global variables
in_play = False
dealed = False
outcome = ""
score = 0
deck = None
dealer = None
player = None
timer = None

# define globals for cards
SUITS = ('D', 'S', 'H', 'C')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)


        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []

        
    def __str__(self):
        ret = "Hand contains"
        
        for c in self.hand:
            ret += " " + str(c)
        return ret

    
    def add_card(self, card):
        self.hand.append(card)

        
    def get_value(self):
        aces = False
        value = 0
        
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        for c in self.hand:
            if not aces and c.get_rank() == 'A':
                aces = True
            
            value += VALUES[c.get_rank()]
        
        if aces and (value+10 <= 21):
            value += 10
        
        return value
    
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        i=0
        while i < len(self.hand):
            self.hand[i].draw(canvas, (pos[0]+i*CARD_SIZE[0], pos[1]) )
            i+=1
 

    
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        
        for s in SUITS:
            for r in RANKS:
                self.deck.append(Card(s,r))
        

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop()
    
    def __str__(self):
        # return a string representing the deck
        ret = "Deck contains"
        for c in self.deck:
            ret += " " + str(c)

            
def timer_handler():
    global timer, in_play, dealed
    timer.stop()
    in_play = True
    dealed = False

#define event handlers for buttons
def deal():
    global outcome, in_play, deck, dealer, player
    global timer, status, dealed, score
    
    if in_play:
        in_play = False
        dealed = True
        status = LOOSE
        timer = simplegui.create_timer(2000, timer_handler)
        timer.start()
        score -= 1
    else:
        in_play = True
        dealed = False

    # your code goes here
    deck = Deck()
    dealer = Hand()
    player = Hand()
    
    deck.shuffle()    
    i=0
    while i<2:
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        i+=1
        
    #print "Player " + str(player)
    #print "Dealer " + str(dealer)
    
    outcome = "Hit or Stand?"

    
def hit():
    global in_play, outcome, score, status
 
    # if the hand is in play, hit the player
    if in_play and player.get_value() <= 21:
        player.add_card(deck.deal_card())
        #print "Player" + str(player) + "(value=" + str(player.get_value()) + ")"
   
    # if busted, assign a message to outcome, update in_play and score
    if player.get_value() > 21:
        outcome = "You have busted!"
        in_play = False
        status = LOOSE
        score -= 1
        

        
def stand():
    global outcome, in_play, score, status
    # replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play and player.get_value() <= 21:
        in_play = False
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        
        if dealer.get_value() > 21:
            outcome = "Dealer Busted!"
        
        if dealer.get_value() > 21 or player.get_value() > dealer.get_value():
            outcome = "Player wins!"
            status = WIN
            score += 1
        else:
            outcome = "Dealer wins"
            status = LOOSE
            score -= 1
    else:
        outcome = "You are busted!"
        
    outcome += " New deal?"

    # assign a message to outcome, update in_play and score


def draw_titles(canvas):
    t_siz = (400, 57)
    subt_siz = (128,39)
    
    canvas.draw_image(title, 
                      (t_siz[0]/2, t_siz[1]/2), 
                      t_siz, 
                      (CANVAS_W/2, 50), 
                      t_siz)
    
    canvas.draw_image(dealer_t, 
                      (subt_siz[0]/2, subt_siz[1]/2), 
                      subt_siz, 
                      (CANVAS_W*1/10, CANVAS_H*2/5), 
                      subt_siz)
    
    canvas.draw_image(player_t, 
                      (subt_siz[0]/2, subt_siz[1]/2), 
                      subt_siz, 
                      (CANVAS_W*1/10, CANVAS_H*4/5), 
                      subt_siz)


def draw_back(canvas):
    canvas.draw_image(card_back, 
                      CARD_BACK_CENTER,
                      CARD_BACK_SIZE, 
                      (CANVAS_W*1/6+CARD_BACK_CENTER[0], CANVAS_H*1/5+CARD_BACK_CENTER[1]), 
                      CARD_BACK_SIZE)

    
def draw_status(canvas):
    canvas.draw_image(status, 
                      (590/2,125/2),
                      (590,125), 
                      (CANVAS_W/2, CANVAS_H/2), 
                      (590,125))
    
    

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    draw_titles(canvas)
    
    dealer.draw(canvas, (CANVAS_W*1/6, CANVAS_H*1/5))
    player.draw(canvas, (CANVAS_W*1/6, CANVAS_H*3/5))
    
    if in_play:
        draw_back(canvas)
    else:
        if dealed:
            draw_back(canvas)
        draw_status(canvas)
    
    canvas.draw_text(outcome,
                     (CANVAS_W*4/6, CANVAS_H*29/30), 
                     28, "White", "sans-serif")
    
    # I really dont know how play blackjack, so use the
    # same scoring as the example on class
    canvas.draw_text("Score: "+str(score),
                     (CANVAS_W*7/8, CANVAS_H*1/8), 
                     20, "White", "sans-serif")
    


# initialization frame
frame = simplegui.create_frame("Blackjack", CANVAS_W, CANVAS_H)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
