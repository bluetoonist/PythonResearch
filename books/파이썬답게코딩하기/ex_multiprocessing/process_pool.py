import multiprocessing


def pring_initial_msg():
    print("Start Process: %s" % multiprocessing.current_process().name)


def worker(data):
    return data * 2


def main():
    pool = multiprocessing.Pool(processes=4, initializer=pring_initial_msg)

    data_list = range(10)
    result = pool.map(worker, data_list)

    pool.close()
    pool.join()
    print("Result: %s " % result)


if __name__ == '__main__':
    main()
