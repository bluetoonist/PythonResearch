import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format="name :%(threadName)s, argument: %(message)s")


def print_local_data(local_data):
    try:
        data = local_data.index
    except:
        logging.debug("Value nos et Yet")
    else:
        logging.debug("Value:%s" % data)


def set_local_data(local_data, index):
    print_local_data(local_data)
    local_data.index = index
    print_local_data(local_data)


def main():
    local_data = threading.local()
    print_local_data(local_data)
    local_data.index = 0
    print_local_data(local_data)

    for i in range(5):
        t = threading.Thread(target=set_local_data, name=("thread-%s" % i), args=(local_data, i + 1))
        t.start()


if __name__ == '__main__':
    main()
