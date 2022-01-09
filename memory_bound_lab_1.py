import time
from multiprocessing import Pool


fib_n = 35
proc_count = 4


def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    start_time = time.perf_counter()
    print("1 fib = ", fibonacci(fib_n), "  fib 2 =", fibonacci(fib_n+1), "  fib 3 =", fibonacci(fib_n+2))
    end_time = time.perf_counter()
    print(f"Elapsed run time: {end_time - start_time} seconds.")

    #parallel
    start_time = time.perf_counter()
    with Pool(proc_count) as p:
        print(p.map(fibonacci, range(fib_n, fib_n+3)))
    end_time = time.perf_counter()
    print(f"Elapsed run time: {end_time - start_time} seconds.")
