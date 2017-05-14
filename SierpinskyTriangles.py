import turtle

levelSierpinski = 3
sizeOfTriangle = 100

def drawTriangle(points,color,myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1])
    myTurtle.goto(points[2])
    myTurtle.goto(points[0])
    myTurtle.end_fill()

def getMidPoint(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def drawSierpinski(points,degree,brad):

    fillColor = 'white'
    if (degree == 0) :
        fillColor = 'green'

    drawTriangle(points,fillColor,brad)

    #draw 3 triangles with each corner and the midle of each side that contains them.
    if degree > 0:
        drawSierpinski([points[0],
                        getMidPoint(points[0], points[1]),
                        getMidPoint(points[0], points[2])],
                   degree-1, brad)
        drawSierpinski([points[1],
                        getMidPoint(points[0], points[1]),
                        getMidPoint(points[1], points[2])],
                   degree-1, brad)
        drawSierpinski([points[2],
                        getMidPoint(points[2], points[1]),
                        getMidPoint(points[0], points[2])],
                   degree-1, brad)
        
def configureTurtle(brad):
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.pencolor("black")
    brad.speed(40)
    return brad


brad = configureTurtle(turtle.Turtle)
window = turtle.Screen()
trianglePoints = [(-sizeOfTriangle,-sizeOfTriangle/2),
                 (0,sizeOfTriangle),
                 (sizeOfTriangle,-sizeOfTriangle/2)]
drawSierpinski(trianglePoints,levelSierpinski,brad)
brad.hideturtle()
window.exitonclick()

