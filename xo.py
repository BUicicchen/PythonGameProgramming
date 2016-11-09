
def displayGrid(grid):
    '''This function prints out the grid'''

    print(" " + grid[1] + " | " + grid[2] + " | " + grid[3] + " ")
    print("___|___|___")
    print(" " + grid[4] + " | " + grid[5] + " | " + grid[6] + " ")
    print("___|___|___")
    print(" " + grid[7] + " | " + grid[8] + " | " + grid[9] + " ")
    print("   |   |   ")



def checkUser(grid, turn):
    place = input("Please select a number from 1 ~ 9: ")
    while grid[place] == 'o' or grid[place] == 'x':
        print("Please choose another place")
        place = input("Please select a number from 1 ~ 9: ")

    while place < 1 and place > 9:
        print("Please choose another place: ")
        place = input("Please select a number from 1 ~ 9: ")
    grid[place] = turn
    return grid


def checkLine(grid):
    continueGame = False
    if grid[1] == grid[2] == grid[3] != " ":
        print(grid[1] + " wins")
    elif grid[4] == grid[5] == grid[6] != " ":
        print(grid[4] + " wins")
    elif grid[7] == grid[8] == grid[9] != " ":
        print(grid[7] + " wins")
    elif grid[1] == grid[4] == grid[7] != " ":
        print(grid[1] + " wins")
    elif grid[2] == grid[5] == grid[8] != " ":
        print(grid[2] + " wins")
    elif grid[3] == grid[6] == grid[9] != " ":
        print(grid[3] + " wins")
    elif grid[1] == grid[5] == grid[9] != " ":
        print(grid[1] + " wins")
    elif grid[3] == grid[5] == grid[7] != " ":
        print(grid[3] + " wins")
    else:
        print("No winner yet")
        continueGame = True
    return continueGame

'''
def children(grid):
    children = 0
    if grid.getvalue == " ":
        children + 1
    print(children)
'''
'''
def MINIMAX_AI(grid):
    data = {grid:{1:}}
    score = 0
    'o' = -10
'''
