import turtle

# Create a Turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a Turtle object
spiral_turtle = turtle.Turtle()
spiral_turtle.shape("turtle")
spiral_turtle.speed(1)  # Set the drawing speed (1 is the slowest)


# Function to draw a spiral with thickness and color
def draw_spiral(num_turns, initial_length, angle_increment):
    length = initial_length
    angle = 0

    # Define a list of colors for the spiral
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    for _ in range(num_turns):
        # Set the color of the turtle's pen
        spiral_turtle.pencolor(colors[_ % len(colors)])

        # Increase the pen thickness
        spiral_turtle.pensize(3 + _ // 10)

        spiral_turtle.forward(length)
        spiral_turtle.right(90)  # Turn the turtle right by 90 degrees
        angle += angle_increment
        length += 5  # Increase the length for each turn


# Set the parameters for the spiral
num_turns = 40  # Number of turns in the spiral
initial_length = 10  # Length of the first segment
angle_increment = 5  # Angle increment for each turn

# Draw the spiral
draw_spiral(num_turns, initial_length, angle_increment)

# Close the Turtle graphics window when clicked
screen.exitonclick()
