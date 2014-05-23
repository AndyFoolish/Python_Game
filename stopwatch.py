#
import simplegui
import random

#global state
position = [0, 0]
width = 100
height = 100
interval = 500

"""
def draw_handler(canvas):
#	canvas.draw_text("A", [120, 20], 12, "Red")
#	canvas.draw_line([0, 0], [200, 300], 10, "Green")
	canvas.draw_circle([90, 200], 20, 10, "White")
	canvas.draw_circle([210, 200], 20, 10, "White")
	canvas.draw_line([50, 180], [250, 180], 40, "Red")
	canvas.draw_line([55, 170], [90, 120], 5, "Red")
	canvas.draw_line([90, 120], [130, 120], 5, "Red")
	canvas.draw_line([180, 108], [180, 160], 140, "Red")
"""
#define an input filed handler
def input_handler(text):
	pass

#define timer handler
def timer_handler():
	pass

#degine draw handler
def draw_handler(canvas):
	canvas.draw_text("A", [120, 20], 12, "Red")

#create frame
frame = simplegui.create_frame("test", 300, 300)
frame.set_draw_handler(draw_handler)
frame.add_input("Enter a value:", input_handler, 200)
timer = simplegui.create_timer(500, timer_handler)
#start the frame animation
frame.start()
timer.start()

# "Stopwatch: The Game"
import simplegui
# define global variables
current_time = 0
running = False
x = 0
y = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
	A = t // 600
    B = ((t // 10) % 60) // 10
    C = ((t // 10) % 60) % 10
    D = t % 10
    return str(A) + ":" + str(B) + str(C) + "." + str(D)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
	global running
	timer.start()
	running = True

def stop():
	global running, x, y
	timer.stop()
	if running == True:
		y += 1
		if current_time % 10 == 0:
			x += 1
	running = False

def reset():
	global current_time, running, x, y
	timer.stop()
	current_time = 0
	running = False
	x = 0
	y = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
	global current_time
	current_time += 1

# define draw handler
def draw_handler(canvas):
	if current_time < 6000:
		canvas.draw_text(format(current_time), [70, 80], 20, "White")
		canvas.draw_text(str(x) + "/" + str(y), [160, 20], 20, "White")

    else:
    	canvas.draw_text("10:00.0", [65, 80], 20, "White")
    	canvas.draw_text("The stopwatch need a rest!", [10, 100], 14, "Yellow")

# create frame
frame = simplegui.create_frame("stopwatch", 200, 150)

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

frame.set_draw_handler(draw_handler)

timer = simplegui.create_timer(100, timer_handler)

# start frame
frame.start()









