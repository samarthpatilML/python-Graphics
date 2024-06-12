import turtle
import random

# Create a turtle object
t = turtle.Turtle()

# Set speed to fastest (adjust as needed)
t.speed(0)

# Set background color (optional)
t.screen.bgcolor("lightblue")

# Hide the turtle (optional)
t.hideturtle()

# Move turtle to starting position (adjust as needed)
t.penup()
t.goto(-200, -100)
t.pendown()

# Set pen color for ground
t.pencolor("brown")

# Draw a long rectangle for the ground
t.forward(400)
t.left(90)
t.forward(200)
t.left(90)
t.forward(400)
t.left(90)
t.forward(200)


# Move turtle to starting position for the sky
t.penup()
t.goto(-200, 100)
t.pendown()

# Use a loop to fill the sky with different shades of blue
for _ in range(100):
  # Generate random blue shades
  red = 0
  green = 0
  blue = random.randint(0, 255)
  t.pencolor(red, green, blue)

  # Draw small horizontal lines to create a textured sky
  t.forward(2)
  t.left(random.randint(1, 3))  # Randomly adjust angle for variety

# Move turtle below the sky for further drawing
t.penup()
t.goto(-100, -50)
t.pendown()

# Define a function to draw a hill with random variations
def draw_hill(t):
  # Set pen color for hills
  t.pencolor("green")

  # Start of the hill
  t.begin_fill()

  # Randomly determine hill shape (rounded or pointy)
  if random.randint(0, 1) == 0:
    t.circle(50, 180)  # Rounded hill
  else:
    t.right(90)  # Start of pointy hill
    t.forward(30)
    t.left(120)
    t.forward(50)
    t.left(120)
    t.forward(30)
    t.right(90)

  # End of the hill and fill
  t.end_fill()

  # Move turtle to the right for the next hill
  t.forward(50)

# Draw multiple hills with the defined function
for _ in range(5):
  draw_hill(t.clone())  # Clone the turtle to avoid affecting previous drawings
