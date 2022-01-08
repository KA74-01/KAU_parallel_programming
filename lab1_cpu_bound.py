from multiprocessing import Pool
import time

start_time = time.time()
arg=265353255952032858325023859320
proc_count=4

def factorize_naive(n):
    """ A naive factorization method. Take integer 'n', return list of
        factors.
    """
    if n < 2:
        return []
    factors = []
    p = 2

    while True:
        if n == 1:
            return factors

        r = n % p
        if r == 0:
            factors.append(p)
            n = n / p
        elif p * p >= n:
            factors.append(n)
            return factors
        elif p > 2:
            # Advance in steps of 2 over odd numbers
            p += 2
        else:
            # If p == 2, get to 3
            p += 1
    assert False, "unreachable"


if __name__ == '__main__':
    for i in range(proc_count):
        print("process №%s" % i, factorize_naive(arg))
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    with Pool(proc_count) as p:
        print(p.map(factorize_naive, [arg, arg, arg, arg]))
    print("--- %s seconds ---" % (time.time() - start_time))



