import logging
import threading

logging.basicConfig(level=logging.DEBUG, format="name :%(threadName)s, argument: %(message)s")


def worker(count):
    logging.debug(count)


def main():
    for i in range(5):
        t = threading.Thread(target=worker, name="thread %i" % i, args=(i,))
        t.start()


if __name__ == '__main__':
    main()
