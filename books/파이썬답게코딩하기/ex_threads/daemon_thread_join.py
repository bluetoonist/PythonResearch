import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format="name :%(threadName)s, argument: %(message)s")


def daemon():
    logging.debug("Start")
    time.sleep(2)
    logging.debug("Exit")


def main():
    t = threading.Thread(name="deamon", target=daemon)
    t.daemon = True

    t.start()
    t.join()


if __name__ == '__main__':
    main()
