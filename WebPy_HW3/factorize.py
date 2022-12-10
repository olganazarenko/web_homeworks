from multiprocessing import cpu_count, Pool
import logging
from time import time, sleep


def factorize(*numbers: int) -> list[int]:

    list = []

    for num in numbers:
        result = []
        for i in range(1, num +1):
            if num % i == 0:
                result.append(i)
        list.append(result)

    return list

    # numbers = list(filter(lambda x: (x % 5 == 0), common_list))
    # numbers.sort()
    # print(numbers)


if __name__ == "__main__":
    timer = time()
    print(f'The start of a simple script:{timer}')
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    print(f'Time elapsed, simple script: {time() - timer}')
    print(f'Values are: \n {a}, \n {b}, \n {c}, \n {d}')

    sleep(2)
    print('____________')

    timer = time()
    print(f'The start of multiprocessing:{timer}')
    a, b, c, d = factorize(128, 255, 99999, 10651060)

    with Pool(processes=2) as pool:
        pool.map(factorize, (128, 255, 99999, 10651060))
        pool.close()
        pool.join()

    n_cores = cpu_count()
    print(f'Number of Logical CPU cores: {n_cores}')
    print(f'Time elapsed, multiprocessing: {time() - timer}')
    print(f'Values are: \n {a},\n {b},\n {c},\n {d}')

    # assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    # assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    # assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    # assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
    # 1521580, 2130212, 2662765, 5325530, 10651060]
