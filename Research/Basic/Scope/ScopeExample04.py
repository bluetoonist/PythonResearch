def greeting(name):
    greeting_msg = "Hello "

    # 함수안에 함수가 선언된 형태인 Nested Function
    def add_name():  # 이 함수는 호출될 떄 실행됨
        return ("%s%s" % (greeting_msg, name))

    msg = add_name()
    print(msg)


if __name__ == '__main__':
    greeting('python')
