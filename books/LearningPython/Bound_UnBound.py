# 바운드 메소드
class Spam:
    def doit(self, message):
        print(message)


object1 = Spam()
object1.doit("Hello World")

# 바운드 메소드 객체는 호출의 괄호 직전에 생성됨
# 실제로 호출하지 않고도 가져올수 있음
object1 = Spam()
x = object1.doit
x('Hello World')


# python 3.x 버전대의 언바운드 메소드는 단순 함수로 취급함

class Selfless:
    def __init__(self, data):
        self.data = data

    def selfless(args1, args2):
        return args1 + args2

    def normal(self, args1, args2):
        return self.data + args1 + args2


X = Selfless(2)
print(X.normal(3, 4))
print(Selfless.normal(X, 3, 4))
print(Selfless.selfless(3, 4))


class Sum:
    def __init__(self, val):
        self.val = val

    def __call__(self, args):
        return self.val + args


print("===========")
sobject = Sum(2)
actions = [sobject]
for act in actions:
    print(act(5))
