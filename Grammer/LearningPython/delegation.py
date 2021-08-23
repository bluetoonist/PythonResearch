class Wrapper:
    def __init__(self, object):
        self.wrapped = object

    def __getattr__(self, item):
        print("Trace :", item)

        # getattr(X,N)은
        # X.__dict__[N] 과 같음)
        return getattr(self.wrapped, item)


if __name__ == '__main__':
    x = Wrapper([1, 2, 3])  # 리스트 래핑
    x.append(4)  # 리스트 메소드에 위임
    print(x.wrapped)  # 내장 객체들을 출력
