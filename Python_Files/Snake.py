import turtle
import time
import random

delay = 0.1

# screen set up
wn = turtle.Screen()
wn.bgcolor("green")
wn.setup(width=650, height=650)
wn.tracer(0)

# head of snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake's food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []


# functions for movement
def go_up():
    head.direction = "up"


def go_down():
    head.direction = "down"


def go_right():
    head.direction = "right"


def go_left():
    head.direction = "left"


# function
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


# connect to keyboard
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_left, "a")

while True:
    wn.update()
    # check for the collision of the food
    if head.distance(food) < 20:
        # move the food through random
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        food.goto(x, y)
    # adding new segments
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("grey")
    new_segment.penup()
    segments.append(new_segment)

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

        # Move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)
    move()

    time.sleep(delay)
    wn.mainloop()
