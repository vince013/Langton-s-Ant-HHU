import turtle
def langton():
    window = turtle.Screen()
    window.bgcolor('white')
    window.screensize(2500, 2500)
    window.tracer(0,0)

    ant = turtle.Turtle()
    ant.shape('square')
    ant.shapesize(0.5)
    ant.speed(0)

    def coordinate(ant):
        return (round(ant.xcor()), round(ant.ycor()))

    def invert(field, ant, color):
        field[coordinate(ant)] = color

    #counterMax anpassen für mehr/weniger Schritte
    rule = "RRLLLRLLLRRR"
    colors = ["white", "cornflower blue", "white smoke","dark cyan","mint cream","beige","light green","moccasin","bisque","rosy brown","firebrick","salmon"]
    fields, pos, step = {}, coordinate(ant), 10
    degree, counter, counterMax = 90, 0, 25000
    
    while counter != counterMax:
        if pos not in fields:
            current_color = "white"
        else:
            current_color = fields[pos]
        
        color_index = colors.index(current_color)
        
        new_color = colors[(color_index + 1) % len(colors)]
        turn_direction = rule[color_index]
        
        ant.fillcolor(new_color)
        invert(fields, ant, new_color)
        ant.stamp()
        
        if turn_direction == "R":
            ant.right(degree)
        else:
            ant.left(degree)
        
        ant.forward(step)
        pos = coordinate(ant)
        counter += 1
        
        if counter % 1000 == 0:
            window.update()   
            
    window.update()
    window.mainloop()

langton()