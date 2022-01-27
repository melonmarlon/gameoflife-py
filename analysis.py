import json
import matplotlib.pyplot as plt

for i in range(1, 20):
    with open(f"data.fin/{5 * i}.data", "r") as file:
        content = file.read().strip().split("\n")
    for c in range(len(content)):
        print(f"{json.loads(content[c])['alive']}")
