import xo as ml
'''Tic tac toe game, in which an user wins by having a line in the grid of 9'''

grid = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}

ml.displayGrid(grid)

turn = 'x'
print("x's turn")

continueG = ml.checkLine(grid)

while continueG:
    grid = ml.checkUser(grid, turn)
    ml.displayGrid(grid)
    if turn == 'x':
        turn = 'o'
        print("o's turn")
    else:
        turn = 'x'
        print("x's turn")
    continueG = ml.checkLine(grid)
