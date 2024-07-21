import turtle

def langton():
    window = turtle.Screen()
    window.bgcolor('white')
    window.screensize(2500, 2500)
    window.tracer(0, 0)
    window.setworldcoordinates(-1250, -1250, 1250, 1250)

    n = 5
    start_positions = [(0, 0), (500, 500), (-500, -500), (500, -500), (-300, 500)]
    ants = []
    rules = ["RL", "LR", "RL", "LR", "LR"]
    colors = ["white", "black"]

    for i in range(n):
        ant = turtle.Turtle()
        ant.shape('square')
        ant.shapesize(0.5)
        ant.speed(0)
        ant.penup()
        ant.goto(start_positions[i])
        ant.pendown()
        ants.append(ant)
        if i % 2 == 0:
            ant.degree = -90
        else:
            ant.degree = 90

    def coordinate(ant):
        return (round(ant.xcor()), round(ant.ycor()))

    def invert(field, ant, color):
        field[coordinate(ant)] = color

    fields, step = {}, 10
    counter, counterMax = 0, 25000

    while counter != counterMax:
        for i, ant in enumerate(ants):
            pos = coordinate(ant)
            if pos not in fields:
                current_color = "white"
            else:
                current_color = fields[pos]

            color_index = colors.index(current_color)
            new_color = colors[(color_index + 1) % len(colors)]
            turn_direction = rules[i][color_index % len(rules[i])]

            ant.fillcolor(new_color)
            invert(fields, ant, new_color)
            ant.stamp()

            if turn_direction == "R":
                ant.right(ant.degree)
            else:
                ant.left(ant.degree)

            ant.forward(step)

        counter += 1

        if counter % 10000 == 0:
            window.update()

    window.update()
    window.mainloop()

langton()