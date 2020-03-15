# bisect Module : 정렬된 상태로 데이터를 추가할 수 있는 모듈을 의미
# Heap Module :  리스트를 생성하고 정렬 ( 리스트가 긴 경우 힙 정렬은 시간이 오래 걸림 )
"""
데이터가 많은 경우 힙 정렬 방식보다 시간과 메모리 낭비를 줄일 수 있음.

"""

import bisect
import random

random.seed(1) # seeding : seed 값에 따라 똑같은 난수를 발생시킴

# for i in range(5):
#     print("%5.4f" %random.random(),end='')

print('New Index List')
print('=== ===== ====')
li = []

for n in range(1,15):
    num = random.randint(1,100)
    #bisect(sequence, data)
    pos = bisect.bisect(li,num) # 아이템이 추가되었을 때 인덱스 값 리턴
    # 중복된 값이 나올 때 오른쪽에 배치가 됨 => insort()는 정렬시 오른쪽에 정렬 ( insort_right() )
    #                                                          왼쪽에 정렬 ( insort_left() )
    bisect.insort(li,num) # 리스트를 정렬 상태로 유지

# 왼쪽 정렬시
    """
        bisect_left()
        insort_left() 사용
    """
    print('%3d %3d' %(num, pos), li)


