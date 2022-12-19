import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format="name :%(threadName)s, argument: %(message)s")


def first_wait(e1, e2):
    while not e1.is_set():
        event = e1.wait(1)
        logging.debug("Event Status: (%s)", event)

        if event:
            logging.debug("e1 is set")
            time.sleep(3)
            logging.debug("Set e2")
            e2.set()


def second_wait(e2):
    while not e2.is_set():
        event = e2.wait(1)
        logging.debug("Event Status: (%s)", event)

        if event:
            logging.debug("e2 is Set.")


def main():
    e1 = threading.Event()
    e2 = threading.Event()

    t1 = threading.Thread(name="first", target=first_wait, args=(e1, e2))
    t1.start()

    t2 = threading.Thread(name="second", target=second_wait, args=(e2,))
    t2.start()

    logging.debug("Wait ...")
    time.sleep(5)
    logging.debug("Set e1")
    e1.set()
    time.sleep(5)
    logging.debug("Exit")


if __name__ == '__main__':
    main()
