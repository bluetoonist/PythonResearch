msg = "Hello"  # Global Variable


def write():
    msg = "World"  # 전역변수 값을 변경하고 출력
    print(msg)


def main():
    print("=== print msg ===")
    print(msg)

    print("=== write function ===")
    write()

    print("=== print msg ===")
    print(msg) # write 함수에서 msg를 바꿨으니 'World'를 출력할 것으로 기대했으나 'Hello' 출력


if __name__ == '__main__':
    main()
