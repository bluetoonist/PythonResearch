msg = "Hello"


def write():
    global msg  # global 변수를 사용하기 위한 KeyWord
    msg += "World"
    print(msg)


def main():
    print("=== print msg ===")
    print(msg)

    print("=== write function ====")
    write()

    print("=== print msg ===")
    print(msg)


if __name__ == '__main__':
    main()
