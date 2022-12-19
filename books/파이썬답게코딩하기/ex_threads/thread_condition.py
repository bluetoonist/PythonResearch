import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format="name :%(threadName)s, argument: %(message)s")


def receiver(condition):
    logging.debug("Start Receiver")

    with condition:
        logging.debug("Waiting...")
        condition.wait()
        time.sleep(1)
        logging.debug("End")


def sender(condition):
    logging.debug("Start Sender")

    with condition:
        logging.debug("Send Notify")
        condition.notify_all()
        logging.debug("Eng")


def main():
    condition = threading.Condition()

    for i in range(5):
        t = threading.Thread(target=receiver, name="receiver %s " % i, args=(condition,))
        t.start()

    send = threading.Thread(target=sender, name="sender", args=(condition,))

    time.sleep(1)
    with condition:
        condition.notify(1)

    time.sleep(3)
    send.start()


if __name__ == '__main__':
    main()
