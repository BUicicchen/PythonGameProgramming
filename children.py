import xo as ml
grid = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}


turn = {"x":"human", "o":"machine"}

# determine whether human or machine starts first
symbol = input("Who is starting? (H/M)")
if symbol is "H":
    turn = {"x":"human", "o":"machine"}
else:
    turn = {"x":"machine", "o":"human"}

# data structure for the game
gridStructure = {"grid":grid,
                 "score":None,
                 "turn":turn["x"],
                 "children": None}

# Number of children
cellsInGrid = grid.values()
numChildren = 0
for c in cellsInGrid:
    if c is " ":
        numChildren += 1
print(numChildren)


def generateChildren(gridStructure):
    '''This function creates the possible moves n the game
    :param gridStructure: dictionary grid, turn, score, children
    :return children: list of gridStructures
    '''
    children = []
    for key, value in gridStructure["grid"].items():
        # here we have the parent grid
        if value is " ":
            gridChild = grid.copy()
            gridChild[key] = gridStructure["turn"]
            nextTurn = "x" if gridStructure["turn"] is "o" else "o"


            ml.displayGrid(gridChild)

            gridStructureChild = {"grid":grid,
                                  "score":None,
                                  "turn":nextTurn,
                                  "children": None}
            children.append(gridStructureChild)
    return children

#test
children = generateChildren(gridStructure)
