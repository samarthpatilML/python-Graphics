import turtle

# Initialize turtle and set pen properties
t = turtle.Turtle()
t.speed(0)  # Set speed to fastest
t.pensize(2)

# Define colors
base_color = "lightgray"
sugar_phosphate_color = "red"
adenine_color = "blue"
thymine_color = "orange"
guanine_color = "green"
cytosine_color = "purple"

# Function to draw a nucleotide base pair
def draw_base_pair(y_pos, base_color, pair_color):
  t.penup()
  t.goto(-30, y_pos)
  t.pendown()
  t.fillcolor(base_color)
  t.begin_fill()
  t.circle(20)
  t.end_fill()

  t.penup()
  t.goto(30, y_pos)
  t.pendown()
  t.fillcolor(pair_color)
  t.begin_fill()
  t.circle(20)
  t.end_fill()

  # Connect bases with a short line
  t.penup()
  t.goto(-10, y_pos + 5)
  t.pendown()
  t.pencolor(base_color)
  t.goto(10, y_pos + 5)

# Draw the sugar-phosphate backbone
t.pencolor(sugar_phosphate_color)
for y in range(100, -100, -20):
  t.penup()
  t.goto(-50, y)
  t.pendown()
  t.goto(50, y)

# Draw Adenine-Thymine base pairs
for y in range(100, -80, -20):
  draw_base_pair(y, adenine_color, thymine_color)

# Draw Guanine-Cytosine base pairs
for y in range(-60, -120, -20):
  draw_base_pair(y, guanine_color, cytosine_color)

# Hide turtle and keep window open
t.hideturtle()
turtle.done()