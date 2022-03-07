"""A heart with a pink and red background and two stars - Something fun is that the little stars appear in random places (they are supposed to resemble sparkles from the heart)!"""


__author__ = 730238845

from turtle import Turtle, colormode, done
t: Turtle = Turtle()
t.speed(0)


def rectangle(t: Turtle, x: float, y: float) -> None:
    """Function 1 - Creating a pink rectangle for the background."""
    t.penup()
    t.goto(-400, 0)
    t.pendown()
    t.color("pink")
    t.forward(800)
    t.left(90)
    t.fillcolor("pink")
    t.begin_fill()
    t.forward(400)
    t.left(90)
    t.forward(800)
    t.left(90)
    t.forward(400)
    t.left(90)
    t.end_fill()


def rectangle2(t: Turtle, x: float, y: float) -> None:
    """Function 1 - Creating a red rectangle for the background."""
    t.penup()
    t.goto(-400, -400)
    t.pendown()
    t.color("red")
    t.forward(800)
    t.left(90)
    t.fillcolor("red")
    t.begin_fill()
    t.forward(400)
    t.left(90)
    t.forward(800)
    t.left(90)
    t.forward(400)
    t.left(90)
    t.end_fill()
    

def triangle(t: Turtle, x: float, y: float) -> None:
    """Function 2 - Creating upside-down triangle."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    colormode(255)
    t.color(204, 153, 255)
    t.fillcolor(204, 153, 255)
    t.begin_fill()
    i: int = 0
    while (i < 3):
        t.right(120)
        t.forward(300)
        i += 1
    t.end_fill()
    

def circle(t: Turtle, r: float, x: float, y: float) -> None:
    """Function 3 - Creating circles for the top of the heart."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    colormode(255)
    t.color(204, 153, 255)
    t.fillcolor(204, 153, 255)
    t.begin_fill()
    t.circle(r)
    t.end_fill()


def star(t: Turtle, x: float, y: float) -> None:
    """Funtion 4 - Drawing stars!"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("white")
    i: int = 0
    while i < 5:
        t.forward(50)
        t.right(144)
        i += 1


def star2(t: Turtle, x: float, y: float) -> None:
    """Funtion 4 - Drawing stars!"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("white")
    i: int = 0
    while i < 5:
        t.forward(30)
        t.right(144)
        i += 1


def star3(t: Turtle, x: float, y: float) -> None:
    """Function 4 - Drawing stars!"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("white")
    i: int = 0
    while i < 5:
        t.forward(40)
        t.right(144)
        i += 1


def main() -> None:
    """The entrypoint of my scene."""
    rectangle(t, -400.0, 0.0)
    rectangle2(t, -400.0, -400.0)
    triangle(t, 150.0, 0.0)
    circle(t, 90.0, 70.0, -50.0)
    circle(t, 90.0, -70.0, -50.0)
    import random
    star(t, random.randint(-200, 200), random.randint(-200, 200))
    star2(t, random.randint(-200, 200), random.randint(-200, 200))
    star3(t, random.randint(-200, 200), random.randint(-200, 200))
   

if __name__ == "__main__":
    main()


done()