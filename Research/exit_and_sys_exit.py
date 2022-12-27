import os


class AException(Exception):
    """"""


SOME_VAR = "THIS TEXT PRINTABLE?"


def ex():
    # except에 정의되지 않은 EOF 에러가 발생하면 어떻게 될까?
    try:
        print('1')
        a = input("text: ")  # Exepect EOFError!
        if a:
            raise AException()

    except AException:
        print("AException")

    return False


if __name__ == '__main__':
    # 메인 로직에서 except이 일어난 경우에 대해 exit(1)를 호출하면 finally 로 넘어간다.

    try:
        ex = ex()
    except:
        print("except")
        exit(1)
    finally:
        if ex:
            print(SOME_VAR)
