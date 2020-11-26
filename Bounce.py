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
    # Init is run everytime we reference Ball and pass in attributes
    def __init__(self, canvas):
        self.canvas = canvas
        # Creating the ball
        self.identity = self.canvas.create_oval(10, 10, 25, 25, fill="red")
        self.canvas.move(self.identity, 350, 150)   # Moving the ball to the center of the screen

    # Defining a function to move the ball down
    def draw(self):
        self.canvas.move(self.identity, 0, 1)


ball = Ball(canvas)


# Initiating a while loop so thw window keeps updating and sleep is there so animations are smooth
while True:
    ball.draw()
    window.update()
    time.sleep(0.1)  # Allow for the animation to take place otherwise it would go very quick
