import json
import matplotlib.pyplot as plt

for i in range(1, 20):
    with open(f"data.fin/{5 * i}.data", "r") as file:
        content = file.read().strip().split("\n")

    alive_length = len(json.loads(content[0])['alive'])
    alive = [0 for i in range(alive_length)]

    for c in range(len(content)):
        alive_loaded = json.loads(content[c])['alive']
        for j in range(len(alive_loaded)):
            alive[j] += alive_loaded[j]

    for a in range(len(alive)):
        alive[a] = round(alive[a] / alive_length)

    fig, ax = plt.subplots()

    x = []
    for j in range(alive_length):
        x.append(j)

    ax.bar(x, alive)
    plt.show()
