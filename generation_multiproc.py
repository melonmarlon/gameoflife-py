from gameoflife import *
import random
import json
from multiprocessing import Process
import time

GENERATIONS = 100
N = 4

def main():
    for i in range(1, 20):
        ratio = 5 * i / 100
        print(f"Ratio: {ratio}")

        processes = [Process(target=compute, args=(ratio, i, n)) for n in range(N)]
        for process in processes:
            process.start()
        for process in processes:
            process.join()

def compute(ratio, i, procnum):
    generations = 0
    while(generations < GENERATIONS // N):
        generations += 1
        print(f"Process {procnum} is at Generation {generations}")

        (seed, grid) = populate(initializeGrid(24, 18), ratio)
        alive_result = alive(grid)
        repetition_result = repetition(grid)

        with open(f"data/{5 * i}.data", "a") as file:
            file.write(json.dumps({"seed": seed, "ratio": ratio, "alive": alive_result, "repetition": repetition_result}) + "\n")
    print(f"Process {procnum} is finished!")

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
