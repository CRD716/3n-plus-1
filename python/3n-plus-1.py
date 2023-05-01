import json
import time, os
start_time = time.time()
data = []

for i in range(1, 100):
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

print("Time to complete (seconds): ")
print(time.time() - start_time)

with open(os.path.join(os.pardir,'data.json'), 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)