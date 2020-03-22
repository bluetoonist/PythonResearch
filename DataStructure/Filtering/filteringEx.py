# Filtering

li = [1,10,23,11,-21,4,-11,-3,5]

# List Comprehension
print([ n for n in li if n>0])

print([n for n in li if n <0]) # 음수만을 출력하는 필터링

plus_number = (n for n in li if n>0)
for x in plus_number:
    print(x)

# filter() 이용 : filter() 함수는 iterator를 생성
l1_1 = ["10","-12","20","-13",'=','*']
def is_int(val):
    try:
        aa= int(val)
        return True
    except ValueError:
        return False

intVal = list(filter(is_int,l1_1))
print(intVal)

# 필터링은 조건에 만족하는 값만 걸러내기도 하고, 새로운 값으로 치환할 수도 있다.
mylist = [10,20,-1,11,-3,-13]
val_1 = [n if n>0 else "음수" for n in mylist]
print(val_1)

# itertools.compress() : 어떤 시퀀스의 필터링 결과를 다른 시퀀스에 적용할 떄 사용한다.
local = [
    '서울','경기','인천','대구','광주','부산','광주'
]
cnt = [2,4,10,3,8,12,8]

from itertools import compress
filter_cnt = [ i>5 for i in cnt] # boolean(True Or False) return
print(filter_cnt)

filter_local = list(compress(local,filter_cnt))
print(filter_local)