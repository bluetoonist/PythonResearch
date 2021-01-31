from functools import wraps
def say_hi():
    print("Hi")

def decorate(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper

say_hi = decorate(say_hi)
say_hi()

print( "="* 50)

@decorate
def say_bye():
    print("Bye~")

say_bye()

print(  "\n\n"+"="* 50)
print(" Decorate를 인자로 받는 경우")
def decorate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Second Decorater Hi")
        func(*args, **kwargs)
        print("Second Decorater Bye")
    return wrapper

@decorate
def say(msg):
    print(msg)
say("How are you?")

## 데코레이터의 문제점
### 원래 함수의 메타 정보가 데코레이터의 메타 정보로 대체됨
### 데코레이터틀 받는 함수 위에 "@wraps(func)"을 선언함으로써 해결
print(" ======= [********] ======")
@decorate
def say_hi():
    print("Hi")

print(say_hi)
print(say_hi.__name__)



