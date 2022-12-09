"""Batter Way10 range -> enumerate

@NOTE
- range는 정수 집합을 순회(iterate)하는 루프를 실행할 때 유용
"""

from random import randint

random_bits = 0
for i in range(64):
    if randint(0, 1):
        random_bits |= 1 << i
        print(random_bits)

# 1
# 아래의 코드는
flavor_list = ['a', 'b', 'c', 'd', 'e', 'f']
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print("%d : %s" % (i + 1, flavor))

# 다음과 같은 문제가 있음
# 1. 리스트의 길이를 알아야 함
# 2. 배열을 인덱스로 접근해야 하며, 읽기 불편


#2
# '1'의 상황을 처리하기 위한 내장함수 enumerate를 제공
#  enumereate는 지연 제너레이터(Lazy generator)로 이터레이터를 감쌈
for i, flavor in enumerate(flavor_list):
    print(f"{i+1} : {flavor}")