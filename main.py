from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# Set up the screen
screen.bgcolor("lightblue")
screen.title("Turtle Movement Game")
screen.setup(width=800, height=600)

# Set up the turtle
tim.shape("turtle")
tim.color("green")
tim.speed(0)  # Fastest drawing speed

# Display instructions on the screen
instructions = Turtle()
instructions.hideturtle()
instructions.penup()
instructions.color("black")
instructions.goto(0, 250)
instructions.write("Use 'F' to move forward, 'D' to move backward, 'L' to turn left, 'R' to turn right, 'C' to clear.", align="center", font=("Arial", 16, "bold"))

# Function to move the turtle forward
def move_forwards():
    tim.forward(10)

# Function to move the turtle backward
def move_backwards():
    tim.backward(10)

# Function to turn the turtle left
def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

# Function to turn the turtle right
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

# Function to clear the screen and reset the turtle's position
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# Function to change the turtle's color randomly
def change_color():
    import random
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    tim.color(random.choice(colors))

# Function to change the turtle's shape
def change_shape():
    shapes = ["turtle", "square", "triangle", "circle"]
    tim.shape(random.choice(shapes))

# Function to increase turtle's speed
def speed_up():
    current_speed = tim.speed()
    if current_speed < 10:
        tim.speed(current_speed + 1)

# Function to decrease turtle's speed
def slow_down():
    current_speed = tim.speed()
    if current_speed > 1:
        tim.speed(current_speed - 1)

# Listen to key presses
screen.listen()

# Assign key presses to functions
screen.onkey(move_forwards, "f")
screen.onkey(move_backwards, "d")
screen.onkey(turn_left, "l")
screen.onkey(turn_right, "r")
screen.onkey(clear, "c")
screen.onkey(change_color, "p")  # Press 'P' to change color
screen.onkey(change_shape, "s")  # Press 'S' to change shape
screen.onkey(speed_up, "w")      # Press 'W' to speed up
screen.onkey(slow_down, "x")     # Press 'X' to slow down

# Keep the window open until clicked
screen.exitonclick()
