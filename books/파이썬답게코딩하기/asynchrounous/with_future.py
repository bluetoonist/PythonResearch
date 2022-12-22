import time
import concurrent.futures


def worker(index):
    print("Worker index: %s" % index)
    time.sleep(index)
    return ("Complete %s worker job " % index)


def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        future_list = []
        for i in range(5):
            future = executor.submit(worker, i)
            future_list.append(future)

        finished, pending = concurrent.futures.wait(
            future_list,
            timeout=2,
            return_when=concurrent.futures.ALL_COMPLETED
        )

        for w in finished:
            print("Finished Worker: %s" % w.result())

        for w in pending:
            print("Not finished worker: %s" % w.result())


if __name__ == '__main__':
    main()
