import turtle

# Screen setup
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("GitHub Icon")
screen.bgcolor("white")

# Turtle setup
t = turtle.Turtle()
t.speed(5)
t.width(2)

# Draw the face (circular head of the Octocat)
t.penup()
t.goto(0, -100)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(100)
t.end_fill()

# Draw the ears
def draw_ear(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(30)
    t.end_fill()

# Left ear
draw_ear(-70, 70)

# Right ear
draw_ear(70, 70)

# Draw the eyes
def draw_eye(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.penup()
    t.goto(x + 5, y - 5)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.circle(5)
    t.end_fill()

# Left eye
draw_eye(-40, 0)

# Right eye
draw_eye(40, 0)

# Draw the mouth
t.penup()
t.goto(-30, -40)
t.pendown()
t.setheading(-30)
t.circle(30, 60)

# Hide the turtle and display the window
t.hideturtle()
screen.mainloop()
