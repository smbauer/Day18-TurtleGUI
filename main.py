import turtle as t
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_shape(turtle, shape, side_length=100):
    shapes = {'triangle': 3, 'square': 4, 'pentagon': 5, 'hexagon': 6, 'heptagon': 7, 'octagon': 8,
              'nonagon': 9, 'decagon': 10}
    sides = shapes[shape]
    angle = 360 / sides

    for _ in range(sides):
        turtle.forward(side_length)
        turtle.right(angle)


def draw_all_shapes(turtle):
    shapes = ['triangle', 'square', 'pentagon', 'hexagon', 'heptagon', 'octagon', 'nonagon', 'decagon']

    for shape in shapes:
        color = random_color()
        turtle.pencolor(color)
        draw_shape(turtle=turtle, shape=shape)


def draw_dashed_line(turtle, line_length=100, seg_length=10):
    if line_length >= seg_length:
        segments = line_length // (seg_length * 2)

        for _ in range(segments):
            turtle.forward(seg_length)
            turtle.penup()
            turtle.forward(seg_length)
            turtle.pendown()
    else:
        print("Can't draw dashed line. Segments are too big.")
        turtle.forward(line_length)


def random_walk(turtle, step_size=20, num_steps=100):
    # change line width
    turtle.pensize(10)

    # colors = ['cyan', 'lime', 'medium slate blue', 'magenta', 'green', 'dark orange', 'red', 'dodger blue']
    headings = [0, 90, 180, 270]

    for _ in range(num_steps):
        # choose a random color
        pen_color = random_color()
        turtle.pencolor(pen_color)

        # choose a random direction
        heading = random.choice(headings)
        turtle.setheading(heading)

        # walk '1 step'
        turtle.forward(step_size)


def draw_spirograph(turtle, num_circles=36):
    angle = 360 / num_circles

    for i in range(num_circles):
        turtle.pencolor(random_color())
        turtle.circle(100)
        turtle.left(angle)


# initialize turtle object
tim = t.Turtle()
tim.speed('fastest')

# initialize screen
screen = t.Screen()
screen.colormode(255)

# draw_square(turtle=tim, side_length=100)
# draw_dashed_line(turtle=tim, line_length=200, seg_length=5)
# draw_all_shapes(tim)
# random_walk(turtle=tim, num_steps=500)
draw_spirograph(turtle=tim, num_circles=72)

# exit
screen.exitonclick()
