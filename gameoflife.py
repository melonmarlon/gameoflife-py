##############
# Game Logic #
##############

# Gibt eine mit 0 gefüllte 2-D-Liste (Grid) mit den Dimensionen x und y zurück
def initializeGrid(x, y):
    grid = []                           # Erstellung eines leeren Grids
    for i in range(y):                  # For-loop um y für die Höhe
        horizontalLine = []             # Initialisierung einer leeren Liste für die x-Werte
        for j in range(x):              # For-loop um x für die Breite
            horizontalLine.append(0)    # 0 wird an horizontalLine angehängt
        grid.append(horizontalLine)     # horizontalLine wird an grid angehängt
    return grid                         # Erstelltes grid wird zurückgegeben

# Gibt ein neues Grid, welches eine Generation weiter als das gegebene Grid ist
def step(grid):
    newGrid = copyGrid(grid)                                                                                        # Gegebenes Grid wird kopiert
    for i in range(len(grid)):                                                                                      # For-loop um die Höhe des Grids
        for j in range(len(grid[i])):                                                                               # For-loop um die Breite des Grids
            neighbors = 0 - grid[i][j]                                                                              # Anzahl der neighbors einer Zelle wird um den Wert der Zelle reduziert
            for y in range(-1, 2):                                                                                  # For-loop um die Höhe des Nachbarfelds
                for x in range(-1, 2):                                                                              # For-loop um die Breite des Nachbarfelds
                    neighbors += grid[(i + y) % len(grid)][(j + x) % len(grid[i])]                                  # neighbors werden die Werte aller Nachbarn addiert
            if (grid[i][j] == 1 and (neighbors == 2 or neighbors == 3)) or (grid[i][j] == 0 and neighbors == 3):    # Abfrage ob die Zelle nach den Regeln von CGoL leben sollte:
                newGrid[i][j] = 1                                                                                   # Zelle wird lebend gesetzt
            else:                                                                                                   # Wenn die Zelle tot sein sollte:
                newGrid[i][j] = 0                                                                                   # Zelle wird tot gesetzt
    return newGrid                                                                                                  # Neues Grid wird zurückgegeben

# Gibt eine Referenz zu einem neuen Grid mit dem gleichen Inhalt wie das gegebene Grid zurück
def copyGrid(grid):
    return [[grid[i][j] for j in range(len(grid[0]))] for i in range(len(grid))]    # Neue Kopie des gegebenen Grids wird zurückgegeben

import random

# Gibt ein neues, zufällig in einem bestimmten Verhältnis mit lebenden Zellen gefülltes Grid zurück
def populate(grid, ratio, seed=None):
    if not seed:                                    # Abfrage ob kein seed gegeben wurde:
        seed = random.random()                      # seed wird zufällig zugewiesen
    random.seed(seed)                               # Zufallsalgorithmus wird mit dem seed initialisiert
    newGrid = copyGrid(grid)                        # Gegebenes Grid wird kopiert
    size_y = len(grid)                              # Höhe des Grids wird in size_y gespeichert
    size_x = len(grid[0])                           # Breite des Grids wird in size_x gespeichert
    cells_to_live = round(size_x * size_y * ratio)  # Anzahl der Zellen, die nach der Größe des Grids und dem gegebenen Ratio, zu leben haben wird in cells_to_live festgelegt
    while cells_to_live > 0:                        # While-loop während es noch Zellen gibt die leben sollten
        x = random.randint(0, size_x - 1)           # x-Koordinate wird zufällig festgelegt
        y = random.randint(0, size_y - 1)           # y-Koordinate wird zufällig festgelegt
        if newGrid[y][x] == 0:                      # Abfrage ob die Zelle tot ist
            newGrid[y][x] = 1                       # Zelle wird lebend gesetzt
            cells_to_live -= 1                      # cells_to_live wird um 1 reduziert
    return (seed, newGrid)                          # Verwendeter seed und das neue Grid wird zurückgegeben
        
############
# File I/O #
############

import pickle

# Schreibt den ein gegebenes Grid in eine Datei
def saveGrid(grid, fileName):
    with open(fileName, "wb") as file:  # Datei wird temporär geöffnet
        pickle.dump(grid, file)         # Grid wird in die Datei geschrieben

# Liest ein Grid aus einer gegebenen Datei
def readGrid(fileName):
    with open(fileName, "rb") as file:  # Datei wird temporär geöffnet
        return pickle.load(file)        # Aus Datei gelesenes Grid wird zurückgegeben

##############
# Visual I/O #
##############

# Gegebenes Grid wird mit Zeilenumbrüchen ausgegeben
def printGrid(grid):
    for i in grid:  # For-loop über die Höhe des Grids
        print(i)    # Einzelne Reihe des Grids wird ausgegeben
