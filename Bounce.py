from tkinter import *
import random
import time


window = Tk()
window.title("Bounce")
window.resizable(0, 0)      # Prevents player from resizing the window


# Initiated a canvas as it is easier to do animation on a canvas
canvas = Canvas(window, width=700, height=700)
canvas.pack()
window.update()


# Defining class ball which will contain all the functions with the ball
class Ball:
    def __init__(self, canvas):
        # So that these can be changed later
        self.x = 0
        self.y = -1
        self.canvas = canvas

        # Creating the ball
        self.identity = self.canvas.create_oval(10, 10, 25, 25, fill="red")
        self.canvas.move(self.identity, 350, 150)   # Moving the ball to the center of the screen

    # Defining a function to move the ball down
    def action(self):
        self.canvas.move(self.identity, self.x, self.y)

        # Keeps track of the current position of the ball and stores in the variable position so we can create an if loop
        position = self.canvas.coords(self.identity)

        # position[1] and [3] are the y coordinate of the ball; if the ball reaches the top it starts to come back down and if it reaches the bottom it comes back up
        if position[1] <= 1:
            self.y = 1
        if position[3] > 688:   # 688 as it looked better
            self.y = -1


ball = Ball(canvas)


# Initiating a while loop so thw window keeps updating and sleep is there so animations are smooth
while True:
    ball.action()
    window.update()
    time.sleep(0.0000001)  # Allow for the animation to take place otherwise it would go very quick
