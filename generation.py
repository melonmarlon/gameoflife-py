from gameoflife import *
import json

# Anzahl der zu überprüfenden Generationen pro Ratio
GENERATIONS = 100

def main():
    for i in range(1, 20):                                                                                                              # For-loop um Ratios von 0.05 bis 0.95 (i * 5) zu erreichen
        ratio = 5 * i / 100                                                                                                             # Momentanes Ratio wird berechnet
        print(f"Ratio: {ratio}")                                                                                                        # Ausgabe des momentanen Ratios
        generations = 0                                                                                                                 # Anzahl der durchgelaufenen Generationen wird auf 0 gesetzt
        while(generations < GENERATIONS):                                                                                               # While-loop solange die Anzahl der bisher durchgelaufenen Generationen geringer als die Anzahl der zu durchlaufenden Generationen ist
            (seed, grid) = populate(initializeGrid(80, 60), ratio)                                                                      # Ein Grid mit dem berechneten Ratio wird zufällig generiert
            alive_result = alive(grid)                                                                                                  # Generiertes Grid wird auf die Anzahl der lebenden Zellen überprüft
            repetition_result = repetition(grid)                                                                                        # Generiertes Grid wird auf Wiederholungen überprüft

            with open(f"data/{5 * i}.data", "a") as file:                                                                               # Datei zum Abspeichern der Ergebnisse wird temporär im "append"-Modus geöffnet
                file.write(json.dumps({"seed": seed, "ratio": ratio, "alive": alive_result, "repetition": repetition_result}) + "\n")   # Ergebnisse der Überprüfungen des Grids wird mit seed und ratio in der Datei im JSON-Format angehängt
            
            generations += 1                                                                                                            # Anzahl der durchgelaufenen Generationen wird um 1 erhöht
            print(generations)                                                                                                          # Anzal der durchlgelaufenen Generationen wird ausgegeben

# Funktion zum Überprüfen der Anzahl der lebenden Zellen
def alive(grid, generations=100):
    newGrid = copyGrid(grid)                    # Gegebenes Grid wird kopiert
    alive = []                                  # Liste alive, welche mit der Anzahl der lebenden Zellen gefüllt werden wird, wird erstellt
    for gen in range(generations):              # For-loop um die Anzahl der zu beobachtenden Generationen
        living = 0                              # Anzahl der lebenden Zellen wird auf 0 gesetzt
        for i in range(len(newGrid)):           # For-loop um die Höhe des Grids
            for j in range(len(newGrid[i])):    # For-loop um die Breite des Grids
                if newGrid[i][j] == 1:          # Abfrage ob die Zelle am Leben ist
                    living += 1                 # Anzahl der lebenden Zellen wird um 1 erhöht
        alive.append(living)                    # Anzahl der lebenden Zellen einer Generation wird an alive angehängt
        newGrid = step(newGrid)                 # Die nächste Generation wird generiert
    return alive                                # alive wird zurückgegeben

# Funktion zum Überprüfen auf Wiederholungen
def repetition(grid):
    gridA = copyGrid(grid)              # Gegebenes Grid wird in gridA kopiert
    gridB = copyGrid(grid)              # Gegebenes Grid wird in gridB kopiert

    while(True):                        # Unendlicher while-loop
        gridA = step(gridA)             # Die nächste Generation von gridA wird generiert
        gridB = step(step(gridB))       # Die übernächste Generation von gridB wird generiert
        if gridA == gridB:              # Abfrage ob gridA und gridB gleich sind (Wenn ja wurde eine Periode erkannt)
            break                       # While-loop wird unterbrochen

    gridT = copyGrid(grid)              # Gegebenes Grid wird in gridT kopiert
    stepsToStart = 0                    # Anzahl der Generationen bis zum ersten Erreichen der Periode wird auf 0 gesetzt
    while(gridT != gridA):              # While-loop solange gridT nicht gleich gridA (Periode) ist
        stepsToStart += 1               # stepsToStart wird um 1 erhöht
        gridT = step(gridT)             # Die nächste Generation von gridT wird generiert

    stepsToEnd = 0                      # Anzahl der Generationen zum Erreichen des Endes der Periode (Anfang der zweiten Periode) wird auf 0 gesetzt
    while(True):                        # Unendlicher while-loop
        stepsToEnd += 1                 # stepsToEnd wird um 1 erhöht
        gridT = step(gridT)             # Die nächste Generation von gridT wird generiert
        if gridT == gridA:              # Abfrage ob gridT und gridA gleich sind (Wenn ja wurde das Ende der Periode erreicht)
            break                       # While-loop wird unterbrochen
    return (stepsToStart, stepsToEnd)   # stepsToStart und stepsToEnd wird zurückgegeben


if __name__ == "__main__":  # Abfrage ob die Datei ausgeführt wurde
    main()                  # Ausführung der main()-Funktion
