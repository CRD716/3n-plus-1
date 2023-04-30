import matplotlib.pyplot as plt
import time
start_time = time.time()

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
    plt.plot(list)

print("Time to complete (seconds): ")
print(time.time() - start_time)
plt.show()