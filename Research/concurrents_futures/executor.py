from concurrent import futures
import os
import time

max_worker = os.cpu_count()


def worker(index):
    import os
    print("[%s] Woker Index: %s" % (os.getpid(), index))
    time.sleep(2)
    return "Complete Index: %s" % index


def main():
    future_list = []

    executor = futures.ProcessPoolExecutor(max_workers=max_worker)

    with futures.ProcessPoolExecutor(max_workers=max_worker) as executor:
        for i in range(6):
            future = executor.submit(worker, i)
            future_list.append(future)

        results = []

        for future in futures.as_completed(future_list):
            res = future.result()
            results.append(res)
            print(future)

        print(results)


if __name__ == '__main__':
    main()
