import json

for i in range(1, 20):
    with open(f"data/{5 * i}.data", "r") as file:
        content = file.read().strip().split("\n")
    for c in range(len(content)):
        rep_length = json.loads(content[c])['repetition'][1]
        if rep_length != 1 and rep_length != 2:
            print(f"At data/{5 * i}.data on line {c + 1} the period-length is: {rep_length}")
