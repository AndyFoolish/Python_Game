#"Guess the number" mini-project
import simplegui
import math
import random

# initialize global variables
low = 0
high = 100

# helper function to start and restart the game
def new_game():
    global secret_number, time
    range_width = high - low
    secret_number = int(random.random()*range_width + low)
    time = int(math.ceil(math.log(high - low + 1, 2)))
    print "\nNew game. Range is from", low, "to", high
    print "Number of remaining guesses is", time

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global low, high
    low = 0
    high = 100
    new_game()
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global low, high
    low = 0
    high = 1000
    new_game()

def input_guess(guess):
    # main game logic goes here
    global input_number,time,secret_number
    input_number = int(guess)
    print "\nGuess was", guess
    time = time-1
    print "Number of remaining guesses is", time
    if input_number > secret_number:
        print "Lower!"
    elif input_number < secret_number:
        print "Higher!"
    else:
        print "Correct!"
        print "\nAwesome! Let's do it again!"
        new_game()
    if time == 0 and input_number != secret_number:
        print "\nSorry, you did't make it.But you can try again!"
        new_game()

# create frame		
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
frame.add_button("Range: 0 - 100", range100, 200)
frame.add_button("Range: 0 - 1000", range1000, 200)
frame.add_input("Enter a guess:", input_guess, 200)

# call new_game and start frame
new_game()
frame.start()	   
