import time
import os
from multiprocessing import Pool
from multiprocessing import current_process
from threading import current_thread
import requests

#consts process count and number of io requests
proc_count = 4
req_count = 50

#io bound task
def make_request(num):

    pid = os.getpid()
    thread_name = current_thread().name
    process_name = current_process().name
    print(f"{pid} - {process_name} - {thread_name}")

    requests.get("https://httpbin.org/ip")

def main():
    for num in range(1, req_count):
        make_request(num)


if __name__ == "__main__":

    #create pool and maping it
    start_time = time.perf_counter()
    with Pool(proc_count) as p:
        p.map(make_request, range(1, req_count))
    end_time = time.perf_counter()

    runtime_1 = end_time - start_time
    print(f"Elapsed run time: {end_time - start_time} seconds.")

    #main processing
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    runtime_2 = end_time - start_time
    print(f"Elapsed run time: {end_time - start_time} seconds.")
    print("runtime paralell=", runtime_1, "runtime main=", runtime_2)
