# Write the football throw program, a 2D turtle graphics based game where the quarterback throws the football to the receiver using real-life physics.
# The quarterback and the receiver are depicted from the side view on the level football field using simple line drawings (stick figures).
# The quarterback and the receiver are set at random distances each time the game is played.
# The user is prompted for the angle and the velocity of the ball.
# The program will plot the trajectory of the ball and if it is within + or – 1 meter of the receiver then the program will consider the ball to be caught.  

# The program should begin by printing out the distance to the receiver in meters.

#Plot the arc of the ball using a while loop and the following equations for X and Y.
#Xi and Yi is the initial position of the ball.  You can set this to the location of the quarterback's hand in your graphics representation. 
#A and V are the angle (in degrees 0-90) and velocity in meters per second.  g is the gravitational constant which is 9.8 m/s²

#X = Xi + Vx * t
#Y = Yi + Vy * t - g * t² / 2

#Vx = V * sin(A)
#Vy = V * cos(A)

#g = 9.8 m/s²

#Make only plot the ball when Y is >= 0, as the ball can’t go into the ground, or before being ‘caught’ by the receiver. 

#Ask the user if they would like to play again, and restart the game if they answer ‘Y’, exit if ‘N’.

#For extra credit, do any or all of the following:
#1) Write the game in object oriented format
#2) Move a football shape on the screen
#3) Give the user 3 tries to throw the ball

import turtle, math, random

class FootBall:
    def __init__(self, x):
        self.x = x
        self.draw_player()
    def draw_player(self):
        # Set the player location
        turtle.penup()
        turtle.goto(self.x, 0)
        turtle.pendown()
        # Draw the main body
        turtle.right(90)
        turtle.forward(50)
        # Draw left leg
        turtle.right(45)
        turtle.forward(25)
        turtle.left(180)
        # Draw right leg
        turtle.forward(25)
        turtle.right(90)
        turtle.forward(25)
        turtle.left(180)
        # Go to top of player
        turtle.forward(25)
        turtle.left(-45)
        turtle.forward(50)
        # Draw left arm
        turtle.

if __name__ == "__main__":
    game = FootBall(random.randint(5, 20))
    