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
    def __init__(self):
        # Set constant
        self.g = 9.8
        # Sets up the player positions and field
        turtle.speed(0)
        turtle.hideturtle()
        self.draw_field()
        rand_distance = self.rand_dis()
        self.quarter_back = self.draw_player(rand_distance[0])
        self.reciever = self.draw_player(rand_distance[1])
        self.distance_between = rand_distance[2]

        # Getter for the hand positions
    def get_pos(self):
        players = [self.quarter_back[0], self.quarter_back[1], self.reciever[0], self.reciever[1]]
        # Returns a list of tuples
        return players

    def rand_dis(self):
        # Generates two random numbers
        x_one = random.randint(-300, 0)
        x_two = random.randint(0, 300)
        # If the numbers are equal regenerate them or if they're too close to zero
        if x_one == x_two or (x_one < 0 and x_one > 25) or (x_two > 0 and x_two < 25) :
            self.rand_dis()
        else:
            # Return a tuple
            return x_one, x_two, x_two - x_one

    def throw_football(self, V, A):
        # Get the positions of each players hands
        positions = self.get_pos()
        quarter_back = [int(positions[0]), int(positions[1])]
        reciever = [int(positions[2]), int(positions[3])]
        Xr = reciever[0]
        Yr = reciever[1]
        # Set up the throwing equation
        Xi = quarter_back[0]
        Yi = quarter_back[1]
        Vx = V * math.sin(math.radians(A))
        Vy = V * math.cos(math.radians(A))
        X = Xi
        Y = Yi
        t = 0  
        # Draw the throw arc
        turtle.penup()
        while True:
            X = Xi + Vx * t
            Y = Yi + Vy * t - self.g * (math.pow(t, 2) / 2)
            # Check if ball is above ground
            if Y >= 0:
                # Prevents the line from jumping straight to reciever
                if t != 0:
                    turtle.pendown()
                # Draws the arc
                turtle.goto(int(X), int(Y))
                # Checks if the ball is inside the hitbox
                if (Xr - int(turtle.xcor())) < 40 and (Yr - int(turtle.ycor())) < 75:
                    print("Congrats!")
                    break
            else:
                # Print the distance the player missed. Assuming 1 meter = 25 pixles
                print("You missed by " + str(abs(int(self.distance_between - turtle.xcor()) // 25)) + " meters.")
                break
            t += 1
 
        turtle.penup()

    def draw_field(self):
        # Draws the field
        turtle.penup()
        turtle.goto(-500, 0)
        turtle.pendown()
        turtle.forward(1000)

    def draw_player(self, x):
        # Set the player location
        turtle.penup()
        turtle.goto(x, 70)
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
        turtle.left(135)
        turtle.forward(25)
        turtle.left(180)
        turtle.forward(25)
        # Draw throwing arm (right arm)
        turtle.right(35)
        turtle.forward(25)
        # The the cordinates of the end of the right arm
        X_pos = turtle.xcor()
        Y_pos = turtle.ycor()
        turtle.right(180)
        turtle.forward(25)
        # Draw head
        turtle.right(180)
        turtle.circle(10)
        turtle.penup()
        turtle.right(10)
        # Return the position
        return X_pos, Y_pos

if __name__ == "__main__":
    # Set important variables
    game = FootBall()
    end_game = False
    tries = 0
    # Print distance between players
    print("Distance between Quarterback and Reciever:", game.distance_between)
    # Game Loop
    while not end_game and tries < 3:
        # Velocity and Angle input and handles potential Value Errors
        try:
            V = float(input("Enter Velocity: "))
            A = int(input("Enter Angle: "))
        except ValueError:
            print("Invalid input detected please try again.")
            continue
        # Draw Throw arc
        game.throw_football(V, A)
        # Ask if player wants to continue
        check = input("Tries:" + str(3 - tries) + " Enter Y if you want to retry or N if you want to quit: ").capitalize()
        if check == "Y":
            tries += 1
            # Print Number of tries left
            print("Tries left:", 3 - tries)
        elif check == "N":
            end_game = True
        else:
            # Assume Y if something other than y or n is entered
            tries += 1
            print("Tries left:", 3 - tries)
            continue
    
    