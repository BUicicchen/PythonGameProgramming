import turtle

def triangle(triangleLength, tur):
    if triangleLength < 10:
        return
    else:
        #draw a triangle
        for i in range(3):
            tur.forward(triangleLength)
            tur.left(120)
            triangle(triangleLength/2, tur)

#creates a window
myWin = turtle.Screen()
#creates a turtle
t = turtle.Turtle()
#draw one square
triangle(100, t)
#close window with a click on the screen
myWin.exitonclick()

'''
import turtle

def triangle(triangleLength, tur):
    if triangleLength < 5:
        return
    else:
        #draw a triangle
        for i in range(3):
            tur.forward(triangleLength)
            tur.left(120)
            triangle(triangleLength/2, tur)

#creates a window
myWin = turtle.Screen()
#creates a turtle
t = turtle.Turtle()
#draw one square
triangle(100, t)
#close window with a click on the screen
myWin.exitonclick()
'''
