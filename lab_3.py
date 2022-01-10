from multiprocessing import Process, Array
import random
# input parametrs
# N = count of array
# p = iterations
# K = count of elements
N = 10
p = 20
K = 8
#probability of moving left
probability = 0.5
#creating array
arr = Array('i', range(N*(p+1)))

arr[0] = K
for i in range(1, len(arr)):
    arr[i] = 0

#func for ploting results
def ploting(a, iterations, n):
    for i in range(iterations + 1):
        print('iteration %s' %i, a[i * n:(i + 1) * n])

#main function of runinng elements
def running(a, n, iterations, prob):
    point = 0

    for i in range(1, iterations + 1):
        rand = random.random()
        if (rand < prob and point != 0) or point == n - 1:
            point -= 1
            a[point + i * n] += 1
        else:
            point += 1
            a[point + i * n] += 1


if __name__ == '__main__':
    processes = []
    #creatin k processes for evey element
    for i in range(K):
        proc = Process(target=running, args=(arr, N, p, probability))
        processes.append(proc)
        proc.start()

    for process in processes:
        process.join()
    #running(arr, N, p, probability)
    ploting(arr, p, N)
