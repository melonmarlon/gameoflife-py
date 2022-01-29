import json
import matplotlib.pyplot as plt

repetitions = []

for i in range(1, 20):
    with open(f"data/{5 * i}.data", "r") as file:
        content = file.read().strip().split("\n")

    alive_length = len(json.loads(content[0])['alive'])
    alive = [0 for i in range(alive_length)]
    repetition = [0, 0]

    for c in range(len(content)):
        alive_loaded = json.loads(content[c])['alive']
        repetition_loaded = json.loads(content[c])['repetition']

        for j in range(len(alive_loaded)):
            alive[j] += alive_loaded[j]
        
        repetition[0] += repetition_loaded[0]
        repetition[1] += repetition_loaded[1]
    
    for a in range(len(alive)):
        alive[a] = round(alive[a] / len(content))

    repetition[0] = round(repetition[0] / len(content))
    repetition[1] = round(repetition[1] / len(content))

    repetitions.append(repetition)

    plt.figure()
    plt.bar([x + 1 for x in range(alive_length)], alive)
    plt.title(f"Alive cells Ratio: {i * 5}%")
    plt.xlabel("Generations [n]")
    plt.ylabel("Alive cells [n]")
    plt.xticks([x])

    plt.savefig(f"graphs/{i * 5}.alive.png")

plt.figure()
plt.bar([x * 5 for x in range(1, 20)], [y[0] for y in repetitions], 4.5)
plt.title("Average generations until periodical behaviour")
plt.xlabel("Ratio [%]")
plt.ylabel("Average generations until periodical behaviour [n]")
plt.xticks([x * 5 for x in range(1, 20)])

plt.savefig("graphs/period_start-ratio.png")
