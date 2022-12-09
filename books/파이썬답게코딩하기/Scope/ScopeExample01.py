msg = "Hello"


# 변수의 유효범위는 LEGB
# L = Local
# E = Enclosed
# G = Global
# B = Built-in

def read_word():
    print(msg)
    print("world")


def read_exception():
    # UnboundLocalError
    # 지역 변수인 msg를 사용하기 이전에 출력했으므로 Error가 일어남

    print(msg)
    msg = "World"
    print(msg)


def main():
    print("==== first read ====")
    read_word()
    print("==== second read ====")
    read_exception()


if __name__ == '__main__':
    main()
