# 딕셔너리 키를 여러값에 매핑하기 ( collections.defauldict )

d = {}
# Dictionary의 setdefault를 이용해 초기값을 지정할수 있음
d.setdefault('sel',[]).append("02")
d.setdefault('sel',[]).append("서울")

print(d)

# collections 모듈의 defaultdict를 이용하면 간편해짐
from collections import defaultdict
d = defaultdict(list)
d['sel'].append("02")
d['sel'].append("서울")
print(d)

d =defaultdict(set)
d['incheon'].add('032')
d['incheon'].add("인천")
print(d)

color = [('파랑', 3), ('노랑', 2), ('빨강',1),('파랑',4), ('노랑', 5)]
d =defaultdict(list)
for key,val in color:
    d[key].append(val)
print(d)

li = list(d.items()) # items()를 이용해 확인가능
print(li)

#문자열의 갯수도 확인가능
str1 = 'hello hi goodmoring'
d = defaultdict(int)
for key in str1:
    d[key] += 1
li = list(d.items())
print(d)