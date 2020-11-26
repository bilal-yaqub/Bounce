from tkinter import *
import random
import time

window = Tk()
window.title("Bounce")

# Initiating a canvas as it is easier to do animation on a canvas
canvas = Canvas(window, width=700, height=700).pack()


class Ball:
    # Init is run everytime we reference Ball and pass in attributes
    def __init__(self, canvas):
        self.canvas = canvas
        # Creating the ball
        self.identity = canvas.create_oval(15, 15, 25, 25, fill="red")
        self.canvas.move(self.identity, 350, 150)   # Moving the ball to the center


window.mainloop()
