import turtle

def tree(branchLenth, tur):
    #This function draws a tree with turtle
    """
    :param branchLenth: the length of the starting branch
    :param tur:
    :return:
    """
    if branchLenth < 2:
        return
    else:
        tur.forward(branchLenth)
        tur.right(20)
        tree(branchLenth-20,t)
        tur.left(40)
        tree(branchLenth-20,t)
        tur.right(20)
        tur.backward(branchLenth)

#creates a window
myWin = turtle.Screen()
#creates a turtle
t = turtle.Turtle()
#draw one square
tree(100, t)
#close window with a click on the screen
myWin.exitonclick()
