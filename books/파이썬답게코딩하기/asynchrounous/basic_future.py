import time
import concurrent.futures


def worker(index):
    print("Worker Index: %s" % index)
    time.sleep(index)
    return ("Completed %s worker job" % index)


def main():
    future_list = []
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=3)
    for i in range(3):
        future = executor.submit(worker, i)
        future_list.append(future)

    time.sleep(1)

    for idx, future in enumerate(future_list):
        if future.done():
            print("result : %s" % future.result())
            continue

        print("[%s worker] Wait for 1 second because it has not finished yet." % idx)

        try:
            result = future.result(timeout=1)
        except concurrent.futures.TimeoutError:
            print("[%s worker] Timeout Error" % idx)
        else:
            print("result: %s" % result)

    executor.shutdown(wait=False)


if __name__ == '__main__':
    main()
