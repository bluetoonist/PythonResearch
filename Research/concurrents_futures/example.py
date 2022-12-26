import time
import random


# def gcd(pair):
#     a, b = pair
#
#     low = min(a, b)
#     for i in range(low, 0, -1):
#         if a % i == 0 and b % i == 0:
#             return i


def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


# rand_list = [random.randrange(1000000, 9000000) for _ in range(20)]

# print(rand_list)

# numbers = []
# for x in range(6):
#     a, b = random.sample(rand_list, 2)
#     result = (a, b)
#     numbers.append(result)

# Result

# start = time.time()
# result = list(map(gcd, numbers))
# end = time.time()
# print(end - start)

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# start = time.time()
# pool = ThreadPoolExecutor(max_workers=2)
# results = list(pool.map(gcd, numbers))
#
# end = time.time()
# print(end - start)

numbers = [(1963309, 2265973), (2030677, 3814172),
           (1551645, 2229620), (2039045, 2020802)]

if __name__ == '__main__':
    start = time.time()
    pool = ProcessPoolExecutor()  # the one change
    results = list(pool.map(gcd, numbers))
    end = time.time()
    print('Took %.3f seconds' % (end - start))
