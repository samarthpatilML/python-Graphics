import turtle

# Screen setup
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Web-Inspired Turtle Graphics")
screen.bgcolor("white")

# Turtle setup
t = turtle.Turtle()
t.speed(3)
t.width(2)

# Draw Header
t.penup()
t.goto(-300, 250)
t.pendown()
t.color("lightblue")
t.begin_fill()
for _ in range(2):
    t.forward(600)
    t.right(90)
    t.forward(60)
    t.right(90)
t.end_fill()

# Draw Navigation Bar
t.penup()
t.goto(-300, 190)
t.pendown()
t.color("grey")
t.begin_fill()
for _ in range(2):
    t.forward(600)
    t.right(90)
    t.forward(40)
    t.right(90)
t.end_fill()

# Draw Nav Buttons
button_colors = ["lightgrey", "silver", "lightgrey", "silver"]
for i in range(4):
    t.penup()
    t.goto(-290 + i * 140, 195)
    t.pendown()
    t.color(button_colors[i])
    t.begin_fill()
    for _ in range(2):
        t.forward(130)
        t.right(90)
        t.forward(30)
        t.right(90)
    t.end_fill()

# Draw Content Sections
content_colors = ["lightblue", "lightgrey", "white", "lightgrey"]
for i in range(4):
    t.penup()
    t.goto(-300, 130 - i * 110)
    t.pendown()
    t.color(content_colors[i])
    t.begin_fill()
    for _ in range(2):
        t.forward(600)
        t.right(90)
        t.forward(100)
        t.right(90)
    t.end_fill()

# Hide the turtle and display
t.hideturtle()
screen.mainloop()
