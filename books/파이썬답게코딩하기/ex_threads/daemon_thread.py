import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format="name :%(threadName)s, argument: %(message)s")


def daemon():
    logging.debug('Start')
    time.sleep(4)
    logging.debug("Exit")


def main():
    t = threading.Thread(name="daemon", target=daemon)
    t.daemon = True
    t.start()


if __name__ == '__main__':
    main()
