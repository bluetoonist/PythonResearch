# Generator 제너레이터 ( yield )
"""
 yield 의 리턴값이 generator object
 yeiel는 generator 생성을 하고  next()함수를 가진다

"""
def generatorEx(n):
    for i in range(n):
        yield i**2

print(generatorEx(4)) # generator obj가 나타남

gen = generatorEx(4)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen)) # End

gen = generatorEx(3)
print(next(gen))

def countdown(n):
    while n>0:
        yield n
        n -= 1
    print("end")

cnt = countdown(3)
print(cnt)
print("====================================")

for i in generatorEx(5):
    print(i)

