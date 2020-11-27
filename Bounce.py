from tkinter import *
from tkinter import messagebox
import random
import time


window = Tk()
window.title("Bounce")
window.resizable(0, 0)      # Prevents player from resizing the window


# Initiated a canvas as it is easier to do animation on a canvas
canvas = Canvas(window, width=700, height=700, bd=0, highlightthickness=0, bg="#264653")
canvas.pack()
window.update()


# Defining class ball which will contain all the functions with the ball
class Ball:
    def __init__(self, canvas):
        # So that these can be changed later
        self.x = random.randint(-5, 5)  # Makes the game more unpredictable
        self.y = -3
        self.canvas = canvas
        self.game_still_going = True

        # Creating the ball
        self.identity = self.canvas.create_oval(10, 10, 25, 25, fill="#e76f51")
        self.canvas.move(self.identity, 350, 150)   # Moving the ball to the center of the screen

    # Defining a function to move the ball down
    def action(self):
        self.canvas.move(self.identity, self.x, self.y)

        # Keeps track of the current position of the ball and stores in the variable position so we can create an if loop
        position = self.canvas.coords(self.identity)    # returns (x1, y1, x2, y2)

        # position[1] and [3] are the y coordinate of the ball; if the ball reaches the top it starts to come back down and if it reaches the bottom it comes back up
        if position[1] <= 1 or position[3] > 700:
            self.y = -self.y
        if position[3] >= 700:
            self.game_still_going = False
        # Checking the ball is hitting the paddle and  if it does the ball moves in the other direction
        if position[2] >= rectangle.position[0] and position[0] <= rectangle.position[2]:
            if position[3] >= rectangle.position[1] and position[3] <= rectangle.position[3]:
                self.y = -self.y

        # position [0] & [2] are x coordinates; creating a while loop to prevent the ball from going out of the screen
        if position[0] <= 0 or position[2] > 700:
            self.x = -self.x


# Exactly the same as when defining the ball
class Rectangle:
    def __init__(self, canvas):
        self.canvas = canvas
        self.identity = self.canvas.create_rectangle(0, 0, 130, 30, fill='#ddbea9')
        self.canvas.move(self.identity, 300, 650)
        self.x = 0  # We don't need the y value here
        # Making position an attribute so it can be accessed inside the ball class
        self.position = (0, 0, 0, 0)

    # When the user presses the left key the rectangles moves left as well
    def move_left(self, event):
        self.x = -3

    # When the user presses the right key the rectangles moves right as well
    def move_right(self, event):
        self.x = 3

    def decision(self):
        # These are th key bindings
        window.bind('<Left>', self.move_left)
        window.bind('<Right>', self.move_right)
        self.canvas.move(self.identity, self.x, 0)
        self.position = self.canvas.coords(self.identity)
        if self.position[0] <= 5 or self.position[2] >= 695:
            self.x = 0  # Stops the paddle from moving out of the screen


ball = Ball(canvas)
rectangle = Rectangle(canvas)

# Initiating a while loop so thw window keeps updating and sleep is there so animations are smooth
while True:
    if ball.game_still_going:
        ball.action()
        rectangle.decision()
        window.update()
        time.sleep(0.01)  # Allow for the animation to take place otherwise it would go very quick
    else:
        # incase they enter lowercase
        answer = messagebox.askquestion("Take the L", "Do you want to keep playing?")
        if answer == "yes":
            ball.game_still_going = True
            continue
        else:
            print("Thanks for playing")
            break
