def coroutine():
    c = 0
    while True:
        msg = yield
        print(f"Hello, your input message is {msg}, {c}")
        c += 1


def main():
    c = coroutine()
    next(c)
    next(c)
    c.send("Test")
    c.send("Corouine")


if __name__ == '__main__':
    main()
