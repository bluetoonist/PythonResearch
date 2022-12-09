def greeting(name):
    greeting_msg = "Hello"

    def add_name():
        # greeting_msg 는 전역변수도 아니고 지역변수도 아님
        # greeting_msg += "" # UnBoundLocalError 발생

        # nonlocal 을 이용한 해결
        # nonlocal은 Python3에서 추가된 기능임
        nonlocal greeting_msg

        return ("%s%s" % (greeting_msg, name))

    msg = add_name()

    print(msg)


if __name__ == '__main__':
    greeting('python')
