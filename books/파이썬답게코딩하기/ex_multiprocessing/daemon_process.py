import time
import multiprocessing


def daemon():
    print("Start")
    time.sleep(5)
    print("Exit")


def main():
    d = multiprocessing.Process(name="daemon", target=daemon)
    d.daemon = True

    d.start()
    time.sleep(3)


if __name__ == '__main__':
    main()
