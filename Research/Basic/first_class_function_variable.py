# 함수가 fist class citizen 속성을 가지면 first-class function 이라고 한다
# - 변수에 함수를 할당할 수 있다
# - 매개변수로 함수를 전달할 수 있다
# - 반환값으로 함수를 사용할 수 있다.

def square(x):
    return x * x


def main():
    print("Function Call")
    print(square(10))

    print("Assgin Variable")
    f = square
    print(f(10))


if __name__ == '__main__':
    main()
