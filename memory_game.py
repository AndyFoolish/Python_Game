# card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global cards_deck, exposed, state, turns, pair
    cards_deck = range(8) + range(8)
    random.shuffle(cards_deck)
    exposed = [False] * 16
    state = 0  
    turns = 0
    pair = []
# define event handlers
def mouseclick(pos):
    i = pos[0] // 50   
    
    # add game state logic here
    # state 0 corresponds to the start of the game
    # state 1 corresponds to a single exposed unpaired card
    # state 2 corresponds to the end of a turn
    global state, card1, card2, turns, card, pair
    
    if state == 0:
        card1 = i
        exposed[i] = True
        state = 1
    elif state == 1:
        card2 = i
        if (card1 != card2) and (card2 not in pair):
            exposed[i] = True
            state = 2
            
            turns += 1
            text = "Turns = " + str(turns)
            label.set_text(text)
        print "state1"
        print "card1:",card1
        print "card2:",card2
    else:
        print "state2"
        print "card1:",card1
        print "card2:",card2
        card = i
        if (card1 != card2) and (card1 != card) and (card2 != card) and (card not in pair):
            if cards_deck[card1] != cards_deck[card2]:
                exposed[card1] = False
                exposed[card2] = False
            else:
                pair.append(card1)
                pair.append(card2)
            card1 = i
            print "update"
            print "card1:",card1
            print "card2:",card2
            exposed[i] = True
            state = 1
            
# cards are logically 50x100 pixels in size
# draw the card deck in draw_handler
def draw(canvas):
    for index, value in enumerate(cards_deck):
        if exposed[index]:
            canvas.draw_text(str(value), [50 * index + 15, 63], 40, 'White')
        else:
            canvas.draw_polygon([[50 * index, 0], [50 * (index + 1), 0], [50 * (index + 1), 100], [50 * index, 100]], 1, 'Red', 'Green')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()










# other student's code

# implementation of card game - Memory

import simplegui
import random

width = 800
height = 100
n = 8
list1 = range(1, n + 1)
list2 = list1
card_list = list1 + list2
random.shuffle(card_list)
exposed = ['False' for i in range(2 * n)]
turns = 0

# helper function to initialize globals
def new_game():
    global state, turns, exposed
    exposed = ['False' for i in range(2 * n)]
    state = 0
    turns = 0
    label.set_text('Turns = ' + str(turns))    
    random.shuffle(card_list)
     
# define event handlers
def mouseclick(pos):
    global state, card1, card2, turns
    card_number = pos[0] // (width / (2 * n))
    if exposed[card_number] == 'False':
        exposed[card_number] = 'True'
        if state == 0:
            card1 = [card_number, card_list[card_number]]
            state = 1
        elif state == 1:
            card2 = [card_number, card_list[card_number]]
            state = 2
            turns += 1
            label.set_text('Turns = ' + str(turns))
        else:
            if card1[1] != card2[1]:
                exposed[card1[0]] = 'False'
                exposed[card2[0]] = 'False'
            card1 = [card_number, card_list[card_number]]
            state = 1
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    x = 0
    y = 0
    for i in range(n * 2):
        canvas.draw_polygon([(x, y), (x + 50, y), (x + 50, y + 100), (x, y + 100)], 4, "#3C6785", "#F2D4AE")
        canvas.draw_text(str(card_list[i]), (x + 10, y + 65), 50, "#3C6785", 'sans-serif')
        if exposed[i] == 'False':
            canvas.draw_polygon([(x, y), (x + 50, y), (x + 50, y + 100), (x, y + 100)], 4, "#3C6785", "#858C4A")
        x += 50

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", width, height)
frame.add_button("Reset", new_game)
label = frame.add_label('Turns = ' + str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
