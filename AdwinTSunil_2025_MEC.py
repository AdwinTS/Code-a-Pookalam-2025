import turtle
import math
import random

# Set up the turtle screen
turtle.speed(0)
turtle.home()
turtle.hideturtle()
turtle.penup()

def write_text(text_list, font_size=20, start_y=350):
    """
    Writes a list of strings on the screen, one below the other.
    The text is positioned on the top-left of the screen.
    """
    turtle.goto(-700, start_y) # Adjusted x-coordinate to move to the left-most position
    for line in text_list:
        turtle.color("#FF4500")
        turtle.write(line, align="left", font=("Inter", font_size, "bold"))
        start_y -= (font_size + 5)  # Adjust y position for the next line
        turtle.goto(-700, start_y) # Adjusted x-coordinate for subsequent lines

# Write the sentences
text_to_write = [
    "Happy Onam guys!",
    "By Adwin too!",
    "A Pookalam for the competition."
]
write_text(text_to_write)

# Reposition the turtle to start the drawing at the correct center
turtle.goto(0, 0)
turtle.pendown()

# small helper to set pen
def set_pen(color, size=1):
    turtle.pencolor(color)
    turtle.pensize(size)

def circ(cl, r):
    """Draws a filled circle with the given color (cl) and radius (r)."""
    # move to bottom of circle, draw filled circle centered at (0,0)
    turtle.penup()
    turtle.setheading(270)
    turtle.forward(r)
    turtle.setheading(0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(cl)
    set_pen(cl, 1)
    turtle.circle(r)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
    turtle.pendown()

def square(size):
    """Draws a square of a given size."""
    for i in range(4):
        turtle.fd(size)
        turtle.lt(90)

def big_flower(shade):
    """Draws a large, multi-petaled flower shape with a given shade."""
    for i in range(13):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.fillcolor(shade)
        set_pen(shade, 1)
        turtle.begin_fill()
        turtle.circle(305, 70)
        turtle.left(110)
        turtle.circle(305, 70)
        turtle.end_fill()
        turtle.right(1)

def draw_square(square_turtle, lll, cll):
    """Draws a two-segment shape with a given length (lll) and color (cll)."""
    for i in range(0, 2):
        square_turtle.begin_fill()
        square_turtle.fillcolor(cll)
        square_turtle.pencolor(cll)
        square_turtle.forward(lll)
        square_turtle.right(30)
        square_turtle.forward(lll)
        square_turtle.right(150)
        square_turtle.end_fill()

def draw_flower(coll, sizz):
    """Draws a flower pattern by repeating a square shape."""
    window = turtle.Screen()
    window.bgcolor("white")

    hello = turtle.Turtle()
    hello.speed(0)
    hello.shape("triangle")
    hello.color(coll)

    for i in range(0, 36):
        draw_square(hello, sizz, coll)
        hello.right(10)

def petal(t, r, angle):
    """Uses the Turtle (t) to draw a petal using two arcs."""
    for i in range(2):
        t.circle(r, angle)
        t.left(180 - angle)

def flower(t, n, r, angle):
    """Uses the Turtle (t) to draw a flower with (n) petals."""
    for i in range(n):
        petal(t, r, angle)
        t.left(360.0 / n)

# --- Start of Pookalam Drawing ---

# Outer ring of circles in a green-orange-yellow palette
set_pen("#008000", 1)  # Green
circ("#008000", 400)
set_pen("#FFA500", 1)  # Orange
circ("#FFA500", 390)
set_pen("#FFD700", 1)  # Gold
circ("#FFD700", 380)

# RingS of red square 
set_pen("#FF0000", 1)
for k in range(36):   # 36 * 10 = 360 -> FOR even coverage
    turtle.begin_fill()
    turtle.fillcolor("#FF0000")
    set_pen("#FF0000", 1)
    square(270)
    turtle.end_fill()
    turtle.rt(10)

# Additional circles
set_pen("#FFA500", 1)  # Orange
circ("#FFA500", 350)
set_pen("#006400", 1)  # Dark Green
big_flower("#006400")
turtle.right(60)
set_pen("#FF4500", 1)  # Orange-red
big_flower("#FF4500")
set_pen("#FFFF00", 1)  # Yellow
turtle.right(60)
big_flower("#FFFF00")
set_pen("#FF0000", 1)  # Red
circ("#FF0000", 280)

# More complex square and hexagon patterns
# Gold rotated squares 
set_pen("#FFD700", 1)
for k in range(12):
    turtle.begin_fill()
    turtle.fillcolor("#FFD700")
    set_pen("#FFD700", 1)
    square(197)
    turtle.end_fill()
    turtle.rt(30)

# Tomato hexagons - use separate turtle 't' that draws & fills each hexagon
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
for k in range(12):
    t.penup()
    t.goto(0, 0)
    t.setheading(k * (360/12))
    t.forward(0)  # keep center-based heading logic consistent
    t.pendown()
    t.begin_fill()
    t.fillcolor("#FF6347")
    t.pencolor("#FF6347")
    for i in range(6):
        t.forward(140)
        t.right(60)
    t.end_fill()

set_pen("#32CD32", 1)  # Lime green
circ("#32CD32", 250)
draw_flower("#FF4500", 129)  # Orange-red
set_pen("#FFD700", 1)  # Gold
circ("#FFD700", 220)
set_pen("#FF6347", 1)  # Tomato
circ("#FF6347", 210)

# Inner orange-red circle with patterns (fill each square individually)
set_pen("#FF4500", 1)
for k in range(36):
    turtle.begin_fill()
    turtle.fillcolor("#FF4500")
    set_pen("#FF4500", 1)
    square(148)
    turtle.end_fill()
    turtle.right(10)

turtle.speed(0)
set_pen("#32CD32", 1)  # Lime green
circ("#32CD32", 160)

# Crimson rotated hexagons (each hexagon filled individually)
th = turtle.Turtle()
th.hideturtle()
th.speed(0)
for k in range(9):
    th.penup()
    th.goto(0, 0)
    th.setheading(k * (360/9))
    th.pendown()
    th.begin_fill()
    th.fillcolor("#DC143C")
    th.pencolor("#DC143C")
    for i in range(6):
        th.forward(100)
        th.right(60)
    th.end_fill()

# Hexagon petal pattern
turtle.begin_fill()
turtle.fillcolor("#FF0000")  # Red
turtle.pen(pencolor="#FF0000", pensize=1)
flower(turtle, 9, 140.0, 60.0)
turtle.end_fill()
turtle.lt(30)
turtle.begin_fill()
turtle.fillcolor("#FFFF00")  # Yellow
turtle.pen(pencolor="#FFFF00", pensize=1)
flower(turtle, 9, 140.0, 60.0)
turtle.end_fill()
turtle.lt(30)
turtle.begin_fill()
turtle.fillcolor("#FFA500")  # Orange
turtle.pen(pencolor="#FFA500", pensize=1)
flower(turtle, 9, 140.0, 60.0)
turtle.end_fill()
turtle.lt(30)

# Small colored squares
turtle.pen(pencolor="#FF4500", pensize=1)  # Orange-red
for k in range(6):
    turtle.begin_fill()
    if k % 2 == 0:
        turtle.pen(pencolor="yellow", pensize=1)
        turtle.fillcolor("yellow")
    else:
        turtle.pen(pencolor="#FF4500", pensize=1)
        turtle.fillcolor("#FF4500")
    square(40)
    turtle.rt(60)
    turtle.end_fill()

# Keep the window open until clicked
turtle.exitonclick()
