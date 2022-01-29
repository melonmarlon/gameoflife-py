from gameoflife import *
import json

GENERATIONS = 100

def main():
    for i in range(1, 20):
        print(f"Ratio: {5 * i / 100}")
        generations = 0
        while(generations < GENERATIONS):
            ratio = 5 * i / 100
            (seed, grid) = populate(initializeGrid(80, 60), ratio)
            alive_result = alive(grid)
            repetition_result = repetition(grid)

            with open(f"data/{5 * i}.data", "a") as file:
                file.write(json.dumps({"seed": seed, "ratio": ratio, "alive": alive_result, "repetition": repetition_result}) + "\n")
            
            generations += 1
            print(generations)

# Funktion zum Testen der Anzahl der lebenden Zellen
def alive(grid, generations=100):
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

# Funktion zum Testen auf Wiederholungen
def repetition(grid):
    gridA = copyGrid(grid)
    gridB = copyGrid(grid)
    while(True):
        gridA = step(gridA)
        gridB = step(step(gridB))
        if gridA == gridB:
            break
    gridT = copyGrid(grid)
    stepsToStart = 0
    while(gridT != gridA):
        gridT = step(gridT)
        stepsToStart += 1
    stepsToEnd = 0
    while(True):
        stepsToEnd += 1
        gridT = step(gridT)
        if gridT == gridA:
            break
    return (stepsToStart, stepsToEnd)


if __name__ == "__main__":
    main()
