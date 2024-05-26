import multiprocessing
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_twin_primes(start, end, result):
    twin_primes = []
    previous_prime = None
    for num in range(start, end):
        if is_prime(num):
            if previous_prime is not None and num - previous_prime == 2:
                twin_primes.append((previous_prime, num))
            previous_prime = num
    result.extend(twin_primes)

def main():
    start_range = 2
    end_range = 1000000  
    num_processes = 8
    chunk_size = (end_range - start_range) // num_processes

    manager = multiprocessing.Manager()
    result = manager.list()

    processes = []
    for i in range(num_processes):
        start = start_range + i * chunk_size
        end = start_range + (i + 1) * chunk_size if i < num_processes - 1 else end_range
        process = multiprocessing.Process(target=find_twin_primes, args=(start, end, result))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    for twin_prime in result:
        print(twin_prime)

if __name__ == "__main__":
    main()