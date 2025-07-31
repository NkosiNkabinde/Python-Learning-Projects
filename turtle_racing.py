import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ["red", "green", "blue", "orange", "purple", "yellow", "black", "pink", "brown", "gray"]

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers  (2-10) or 'q' to quit: ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Invalid input. Please enter a valid number")
            continue

        if 2 <= racers <= 10:
            return racers
        elif racers == 'q':
            quit()
        else:
            print("Invalid input. Please enter a number between 2 and 10.")

def race(colors):
    turtles = create_turtle(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)
            
            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


def create_turtle(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)                # +1 to include the starting point
    for i , color in enumerate(colors):                  
        racer = turtle.Turtle()                          # create a new turtle
        racer.color(color)                                   # set the color of the turtle
        racer.shape("turtle")                # set the shape of the turtle
        racer.left(90)                       # turn the turtle left by 90 degrees
        racer.penup()                       # lift the pen up
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT // 2 + 20 )                       # set the position of the turtle
        racer.pendown()  # set the position of the turtle
        turtles.append(racer)

    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")


racers = get_number_of_racers() 
init_turtle()      # we need to call this function to set up the screen

random.shuffle(COLORS)  
colors = COLORS[:racers]  

winner = race(colors)    # Start the race and get the winner
print(f"The winner is: {winner}")
time.sleep(5)

