import threading


class Worker(threading.Thread):

    def __init__(self, args, name=""):
        threading.Thread.__init__(self)
        self.args = args

    def run(self):
        print(f"name: {threading.current_thread().name}, argument:{self.args[0]} ")


def main():
    for i in range(0, 5):
        t = Worker(name="thread %i" % i, args=(i,))
        t.start()


if __name__ == '__main__':
    main()
