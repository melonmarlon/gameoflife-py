from gameoflife import *

# PROJEKT: Feste Anzahl an lebenden Zellen; Zufällig verteilt; big data versuche

def main():
    for i in range(1, 10):
        print(f"##### Ratio {str(round(0.1 * i, 1))} #####")
        for j in range(1):
            grid = populate(initializeGrid(80, 60), (0.1 * i))
            alive_result = reduction(grid)
            change_result = change(grid)
            repetition_result = repetition(grid)

            with open(f"data/{str(10 * i)}.data", "a") as file:
                file.write("{" + f"'alive': {alive_result}, 'change': {change_result}, 'repetition': {repetition_result}" + "}\n")
        
            print(str(2 - j))

# Funktion zum Testen der Reduktion
def reduction(grid, generations=100):
    newGrid = copyGrid(grid)
    alive = []
    for gen in range(generations):
        living = 0
        for i in range(len(newGrid)):
            for j in range(len(newGrid[i])):
                if newGrid[i][j] == 1:
                    living += 1
        alive.append(living)
        newGrid = step(newGrid)
    return alive

# Fuktion zum Testen der Veränderung
def change(grid, generations=100):
    alive = reduction(grid, generations)
    change = []
    for i in range(len(alive)):
        if i == len(alive):
            pass
        change.append(alive[i] - alive[i - 1])
    return change

# Funktion zum Testen auf Wiederholungen
def repetition(grid):
    gridA = copyGrid(grid)
    gridB = copyGrid(grid)
    gridP = None
    while(gridP == None):
        gridA = step(gridA)
        gridB = step(step(gridB))
        if gridA == gridB:
            gridP = copyGrid(gridA)
    gridT = copyGrid(grid)
    stepsToStart = 0
    while(gridT != gridP):
        gridT = step(gridT)
        stepsToStart += 1
    stepsToEnd = 0
    while(True):
        gridT = step(gridT)
        if gridT == gridP:
            break
        stepsToEnd += 1
    return (stepsToStart, stepsToEnd)


if __name__ == "__main__":
    main()
