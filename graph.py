import matplotlib.pyplot as plt
import json
data = []

with open('data.json', 'r') as f:
    data = json.load(f)

for i in data:
    plt.plot(i)

plt.show()