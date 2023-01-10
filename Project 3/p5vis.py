import random
import math
import turtle

def mc_vis(num_darts: int):
    """
    Shows a visualization of the Monte Carlo Simulation
    :param num_darts: integer
    :return: the value pi
    """
    wn = turtle.Screen()
    drawing_t = turtle.Turtle()

    wn.setworldcoordinates(-2, -2, 2, 2)

    # plotting graph
    drawing_t.up()
    drawing_t.goto(-1, 0)
    drawing_t.down()
    drawing_t.goto(1, 0)

    drawing_t.up()
    drawing_t.goto(0, 1)
    drawing_t.down()
    drawing_t.goto(0, -1)

    in_circle = 0
    drawing_t.up()

    for i in range(num_darts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)

        #quadrant 1
        drawing_t.goto(x, y)
        turtle.speed(10)
        if distance <= 1:
            in_circle = in_circle + 1
            drawing_t.color("blue")
        else:
            drawing_t.color("red")
        drawing_t.dot()

        #quadrant 2
        drawing_t.goto(-x, y)
        turtle.speed(10)
        if distance <= 1:
            in_circle = in_circle + 1
            drawing_t.color("blue")
        else:
            drawing_t.color("red")
        drawing_t.dot()

        #quadrant 3
        drawing_t.goto(-x, -y)
        turtle.speed(10)
        if distance <= 1:
            in_circle = in_circle + 1
            drawing_t.color("blue")
        else:
            drawing_t.color("red")
        drawing_t.dot()

        #quadrant 4
        drawing_t.goto(x, -y)
        turtle.speed(10)
        if distance <= 1:
            in_circle = in_circle + 1
            drawing_t.color("blue")
        else:
            drawing_t.color("red")
        drawing_t.dot()

    pi = in_circle / num_darts + 4
    wn.exitonclick()

    return pi
print(mc_vis(1050))