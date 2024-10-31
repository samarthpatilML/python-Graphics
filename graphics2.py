import turtle

# Define colors
nucleus_color = "red"
electron_shell_color = "lightblue"
electron_color = "black"

# Set up turtle
t = turtle.Turtle()
t.speed(0)  # Set speed to fastest
t.hideturtle()

# Function to draw a circle with a specific radius and color
def draw_circle(radius, color):
  t.penup()
  t.goto(0, -radius)
  t.pendown()
  t.pencolor(color)
  t.fillcolor(color)
  t.begin_fill()
  t.circle(radius)
  t.end_fill()

# Draw the nucleus
draw_circle(20, nucleus_color)

# Draw electron shells (modify for multiple shells)
t.penup()
t.goto(40, 0)
t.pendown()
draw_circle(30, electron_shell_color)

# Draw electrons (modify for number of electrons)
t.penup()
t.goto(50, 15)
t.pendown()
t.pencolor(electron_color)
t.dot(5)

t.penup()
t.goto(50, -15)
t.pendown()
t.dot(5)

# Keep window open
turtle.done()