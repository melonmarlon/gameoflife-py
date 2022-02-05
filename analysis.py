import json
import matplotlib.pyplot as plt # Libary zum erstellen von Graphen

## Script zum Auswerten der generierten Daten und erstellen von Verschiedenen Graphen ##

repetitions = []    # Leere Liste mit den späteren durchschnittlichen Wiederholungen pro Ratio wird erstellt

for i in range(1, 20):                                              # For-loop um die Ratios von 0.05 bis 0.95 (i * 5) zu erreichen
    with open(f"data/{5 * i}.data", "r") as file:                   # Datei mit Daten des Momentanen Ratios wird im "read"-Modus geöffnet
        content = file.read().strip().split("\n")                   # Inhalt der Datei wird Zeilenweise in content geladen

    alive_length = len(json.loads(content[0])['alive'])             # Länge der Liste der Anzahl der lebenden Zellen pro Generation wird aus der ersten Zeile angenommen
    alive = [0 for i in range(alive_length)]                        # Mit 0 gefüllte Liste mit der länge alive_length wird gefüllt
    repetition = [0, 0]                                             # Liste mit den späteren durchschnittlichen Wiederholungen wird erstellt

    for c in range(len(content)):                                   # For-loop um die Anzahl der Zeilen der Datei (gespeicherten Egebnissen)
        alive_loaded = json.loads(content[c])['alive']              # Liste mit der Anzahl der lebenden Zellen wird gelesen
        repetition_loaded = json.loads(content[c])['repetition']    # Liste mit dem Anfang und der Länge der Wiederholung wird gelesen

        for j in range(alive_length):                               # For-loop um die Länge der Liste der Anzahl der lebenden Zellen pro Generation
            alive[j] += alive_loaded[j]                             # alive_loaded wird an alive angehängt
        
        repetition[0] += repetition_loaded[0]                       # Anfang der Wiederholung wird zu repetition[0] addiert
        repetition[1] += repetition_loaded[1]                       # Länge der Wiederholung wird zu repetition[1] addiert
    
    for a in range(alive_length):                                   # For-loop um die Länge der Liste der Anzahl der lebenden Zellen pro Generation
        alive[a] = round(alive[a] / len(content))                   # Durchschnitt der Anzahl der lebenden Zellen wird berechnet

    repetition[0] = round(repetition[0] / len(content))             # Durchschnitt des Anfangs der Wiederholungen wird berechnet
    repetition[1] = round(repetition[1] / len(content))             # Durchschnitt der Länge der Wiederholungen wird berechnet

    repetitions.append(repetition)                                  # Durchschnitt der durchschnittlichen Wiederholung wird an repetitions angehängt

    plt.figure()                                                    # Neues Diagrammobjekt wird initialisiert

    plt.bar([x + 1 for x in range(alive_length)], alive)            # Balkendiagramm mit den Generationen auf der x-Achse und den durchschnittlich lebenden Zellen pro Generation auf der y-Achse wird erstellt
    plt.title(f"Alive cells Ratio: {i * 5}%")                       # Titel des Diagramms wird gesetzt
    plt.xlabel("Generations [n]")                                   # x-Achsenbeschriftung wird gesetzt
    plt.ylabel("Alive cells [n]")                                   # y-Achsenbeschriftung wird gesetzt
    plt.xticks([x * 10 - 5 for x in range(1, 11)])                  # x-Achsenskalierung wird modifiziert

    plt.savefig(f"graphs/alive_cells-{i * 5}_ratio.png")            # Diagramm wird in Datei gespeichert
    plt.close()                                                     # Diagrammobjekt wird geschlossen

plt.figure()                                                                # Neues Diagrammobjekt wird initialisiert

plt.bar([x * 5 for x in range(1, 20)], [y[0] for y in repetitions], 4.5)    # Balkendiagramm mit den Ratios auf der x-Achse und den durchschnittlichen Anfängen der Wiederholungen auf der y-Achse wird erstellt
plt.title("Average generations until periodical behaviour")                 # Titel des Diagramms wird gesetzt
plt.xlabel("Ratio [%]")                                                     # x-Achsenbeschriftung wird gesetzt
plt.ylabel("Average generations until periodical behaviour [n]")            # y-Achsenbeschriftung wird gesetzt
plt.xticks([x * 5 for x in range(1, 20)])                                   # x-Achsenskalierung wird modifiziert

plt.savefig("graphs/period_start-ratio.png")                                # Diagramm wird in Datei gespeichert
plt.close()                                                                 # Diagrammobjekt wird geschlossen

plt.figure()                                                                # Neues Diagrammobjekt wird initialisiert

plt.bar([x * 5 for x in range(1, 20)], [y[1] for y in repetitions], 4.5)    # Balkendiagramm mit den Ratios auf der x-Achse und den durchschnittlichen Längen der Wiederholungen auf der y-Achse wird erstellt
plt.title("Average length of periodical behaviour")                         # Titel des Diagramms wird gesetzt
plt.xlabel("Ratio [%]")                                                     # x-Achsenbeschriftung wird gesetzt
plt.ylabel("Average length of periodical behaviour [n]")                    # y-Achsenbeschriftung wird gesetzt
plt.xticks([x * 5 for x in range(1, 20)])                                   # x-Achsenskalierung wird gesetzt

plt.savefig("graphs/period_length-ratio.png")                               # Diagramm wird in Datei gespeichert
plt.close()                                                                 # Diagrammobjekt wird geschlossen
