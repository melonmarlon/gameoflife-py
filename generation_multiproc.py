from gameoflife import *
import json
from multiprocessing import Process
import time

# Anzahl der zu überprüfenden Generationen pro Ratio 
GENERATIONS = 100
# Anzahl der auszuführenden Prozesse. Sollte GENERATIONS restlos teilen. (Anzahl der zu überprüfenden Ergebnisse = round(GENERATIONS / N) * N)
N = 5

def main():
    for i in range(1, 20):                                                          # For-loop um Ratios von 0.05 bis 0.95 (i * 5) zu erreichen
        ratio = 5 * i / 100                                                         # Momentanes Ratio wird berechnet
        print(f"Ratio: {ratio}")                                                    # Ausgabe des momentanen Ratios

        processes = [Process(target=compute, args=(ratio, i, n)) for n in range(N)] # Liste mit Prozessen, welche die Funktion compute() ausführen, wird erstellt
        for process in processes:                                                   # For-loop um die Prozesse in der Liste processes
            process.start()                                                         # Der Prozess wird gestartet
        for process in processes:                                                   # For-loop um die Prozesse in der Liste processes
            process.join()                                                          # Es wird gewartet bis der Prozess abgeschlossen wurde

# Funktion zum Generieren und Auswerten von mehreren Grids von einem Ratio (Auslagerung der main()-Funktion von generation.py in eine extra Funktion)
def compute(ratio, i, procnum):
    generations = 0                                                                                                                 # Anzahl der durchgelaufenen Generationen wird auf 0 gesetut
    while(generations < round(GENERATIONS / N)):                                                                                    # While-loop solange die Anzahl der bisher durchgelaufenen Generationen geringer als die Anzahl der zu durchlaufenden Generationen ist
        print(f"Process {procnum} is at Generation {generations}")                                                                  # Ausgabe des Prozessnamen und der momentanen Generation wrid ausgegeben

        (seed, grid) = populate(initializeGrid(80, 60), ratio)                                                                      # Ein grid mit dem berechneten Ratio wird zufällig generiert
        alive_result = alive(grid)                                                                                                  # Generiertes Grid wird auf die Anzahl der lebenden Zellen überprüft
        repetition_result = repetition(grid)                                                                                        # Generiertes Grid wird auf Wiederholungen überprüft

        with open(f"data/{5 * i}.data", "a") as file:                                                                               # Datei zum Abspeichern der Ergebnisse wird temporär im "append"-Modus geöffnet
            file.write(json.dumps({"seed": seed, "ratio": ratio, "alive": alive_result, "repetition": repetition_result}) + "\n")   # Ergebnisse der Überprüfung des Grids wird mit seed und ratio in der Datei im JSON-Format angehängt

        generations += 1                                                                                                            # Anzahl der durchgelaufenen Generationen wird um 1 erhöht

    print(f"Process {procnum} is finished!")                                                                                        # Beendigung des Prozesses wird angekündigt

# Funktion zum Testen der Anzahl der lebenden Zellen (siehe generation.py für Dokumentation)
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

# Funktion zum Testen auf Wiederholungen (siehe generation.py für Dokumentation)
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


if __name__ == "__main__":  # Abfrage ob die Datei ausgeführt wurde
    main()                  # Ausführung der main()-Funktion
