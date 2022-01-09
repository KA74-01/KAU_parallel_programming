from multiprocessing import Array, Process
import numpy as np

arr = Array('d', range(10))

for i in range(len(arr)):
    arr[i] = i+5


def f(a, iterator):
    a[iterator] = a[iterator]*a[iterator]


if __name__ == '__main__':
    processes = []
    for i in range(len(arr)):
        p = Process(target=f, args=(arr, i))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()

    print(min(arr[:]))
    print(np.argmin(arr))
