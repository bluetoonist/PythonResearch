# Collections Module
# 컨테이너 데이터 타입들이 포함된 모듈

import collections

# collections Counter

ct1 = collections.Counter(['a','b','c','d','a','b','c'])
print("Collections Counter Method : Result",ct1)


# counter 객체는 산술 / 집합 연산이 가능
ct2 = collections.Counter(['a','b','c','d','a'])

print(ct1+ct2)
print(ct1-ct2)
print(ct1&ct2) #교집합
print(ct1|ct2) #합집합 두 집합에서 최대값만 출력

print("================================")

# defaultdict -> method
# 컨테이너를 초기화 할 떄 default 값을 지정
def default_aa():
    return "aa"

dic = collections.defaultdict(default_aa,n1='hi')
print(dic)
print(dic['n1'])
print(dic['n2'])



# collections deque
deq = collections.deque("Hello Python")
print(deq)

deq.append('o') #오른쪽에서부터 참
print(deq)

deq.appendleft('o') #왼쪽에서부터 참
print(deq)

# 마찬가지
deq.pop()
deq.popleft()
print("================================")

# namedtuple
# 튜플에 'name'을 할당해서 쓰는 자료형
Person = collections.namedtuple("Person","name age gender")
a = Person(name="kang",age='24',gender='남')
b = Person(name='hong',age='24',gender='여')
for n in [a,b]:
    print("%s는 %s세의 %s 입니다 " %n)

print("================================")

# orderdict
# orderdict는 순서를 중요시하는 사전형
dic1 = collections.OrderedDict()
dic1["서울"]="LG트윈스"
dic1["광주"]="KIA타이거즈"
dic1["대구"]="삼성라이온즈"

dic2 = collections.OrderedDict()
dic2["서울"]="LG트윈스"
dic2["대구"]="삼성라이온즈"
dic2["광주"]="KIA타이거즈"

print(dic1 == dic2) # Result == False