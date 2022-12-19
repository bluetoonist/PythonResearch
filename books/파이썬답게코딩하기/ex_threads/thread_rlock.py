import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format="name :%(threadName)s, argument: %(message)s")

RESOURCE = 0


def set_reverse(lock):
    logging.debug("Start Batch")

    with lock:
        logging.debug("Grab Lock")

        if RESOURCE != 0:
            set_one(lock, True)
        else:
            set_zero(lock, True)


def set_zero(lock, end=False):
    logging.debug("Start set Zero")

    while True:
        with lock:
            logging.debug("Grab lock and set RESOURCE to 0")
            RESOURCE = 0
            time.sleep(0.5)
        time.sleep(1)

        if end:
            break


def set_one(lock, end=False):
    logging.debug("Start set one")

    while True:
        with lock:
            logging.debug("Grab lock and set RESOURCE to 1.")
            RESOURCE = 1
            time.sleep(0.5)
        time.sleep(1)

        if end:
            break


def main():
    lock = threading.RLock()

    zero = threading.Thread(target=set_zero, name="zero", args=(lock,))
    zero.daemon = True
    zero.start()

    one = threading.Thread(target=set_one, name="one", args=(lock,))
    one.daemon = True
    one.start()

    time.sleep(6)

    reverse = threading.Thread(target=set_reverse, name="reverse", args=(lock,))
    reverse.start()


if __name__ == '__main__':
    main()
