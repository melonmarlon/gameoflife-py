def main():
    grid = initializeGrid(8, 6)
    printGrid(grid)

##############
# Game Logic #
##############

# Returns a 2D list with the given x and y dimensions and optional fill (defaults to 0)
def initializeGrid(x, y, fill=0):
    grid = []
    for i in range(y):
        horizontalLine = []
        for j in range(x):
            horizontalLine.append(fill)
        grid.append(horizontalLine)
    return grid

# Returns a new grid that is one step further than the given grid after the rules of conways game of life have been applied
def step(grid):
    newGrid = [[grid[i][j] for j in range(len(grid[0]))] for i in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            neighbors = 0 - grid[i][j]
            for y in range(-1, 2):
                for x in range(-1, 2):
                    neighbors += grid[(i + y) % len(grid)][(j + x) % len(grid[i])]
            if (grid[i][j] == 1 and (neighbors == 2 or neighbors == 3)) or (grid[i][j] == 0 and neighbors == 3):
                newGrid[i][j] = 1
            else:
                newGrid[i][j] = 0
    return newGrid

############
# File I/O #
############

# Python Module for Serialization
import pickle

# Writes the given grid to a given file in binary representation
def saveGrid(grid, fileName):
    with open(fileName, "wb") as file:
        pickle.dump(grid, file)

# Returns grid that has been read from a given file
def readGrid(fileName):
    with open(fileName, "rb") as file:
        return pickle.load(file)
    return None

##############
# Visual I/O #
##############

# Prints a given grid to the stdout in formatted representation
def printGrid(grid):
    for i in grid:
        print(i)

# PROJEKT: Zufällige Startkonfiguration (mit verschiedenen Anteilen an lebenden Zellen); Schritte bis zum regelmäßigen (periodischen) Verhalten

if __name__ == "__main__":
    main()