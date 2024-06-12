import turtle
import math

def spirograph(t, radius1, radius2, ratio, color="black", num_loops=36):
  """
  Draws a spirograph using the turtle graphics library.

  Args:
      t (turtle.Turtle): The turtle object to use for drawing.
      radius1 (float): The radius of the inner circle.
      radius2 (float): The radius of the outer circle.
      ratio (float): The rotation ratio between the inner and outer circles.
      color (str, optional): The color of the spirograph (defaults to "black").
      num_loops (int, optional): The number of loops to draw (defaults to 36).
  """

  x = 0
  y = 0
  t.color(color)  # Set pen color

  for _ in range(num_loops):
    theta = t.heading()
    x += radius1 * math.cos(theta)
    y += radius1 * math.sin(theta)
    t.goto(x, y)
    t.pendown()
    t.setheading(theta + ratio)
    t.penup()

# Set up turtle
t = turtle.Turtle()
t.speed(0)  # Set drawing speed to fastest

# Draw spirograph with desired parameters
spirograph(t, 100, 50, 1.3, "blue", 72)  # Adjust parameters as needed

# Keep the window open until closed manually
turtle.done()


