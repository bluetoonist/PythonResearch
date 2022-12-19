import threading


def worker(count):
    print("name: %s, argument: %s" % (threading.current_thread().name, count))


def main():
    for i in range(5):
        t = threading.Thread(target=worker, name="thread %i" % i, args=(i,))
        t.start()


if __name__ == '__main__':
    main()
