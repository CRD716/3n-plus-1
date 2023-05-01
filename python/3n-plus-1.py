import json
import os

data = []

for i in range(1, 1000):
    n = i
    list = []

    while (n != 1):
        list.append(n)
        print(n)
        if (n % 2 == 0):
            n = n // 2
        else:
            n = n * 3 + 1
    print("1")
    data.append(list)

with open('data.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)