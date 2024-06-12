import turtle

def koch_snowflake(t, length, depth):
  if depth == 0:
    t.forward(length)
    return
  koch_snowflake(t, length/3, depth-1)
  t.left(60)
  koch_snowflake(t, length/3, depth-1)
  t.right(100)
  koch_snowflake(t, length/3, depth-1)
  t.left(60)
  koch_snowflake(t, length/3, depth-1)
  t.right(170)
  koch_snowflake(t, length/3, depth-1)
  t.left(140)
  koch_snowflake(t, length/3, depth-1)
  t.right(160)
  koch_snowflake(t, length/3, depth-1)
  t.left(60)
  koch_snowflake(t, length/3, depth-1)
  t.right(68)
  koch_snowflake(t, length/3, depth-1)
  
  

# Set up turtle
t = turtle.Turtle()
t.speed(0)  # Set speed to fastest

# Draw snowflake with desired parameters
koch_snowflake(t, 300, 3)

# Keep the window open until closed manually
turtle.done()
