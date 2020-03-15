# Heap : 이진 트리 형태의 자료구조

from showHeap import show_tree
from headData import data

# Python 에서 제공하는 heap 관련 Module
import heapq

# 정의된 showHeap 과 heapData에 있는 show_tree와 data
show_tree(data)

print("============  heappush  ============")
heap = []

for n in data:
    print("%3d" %n)
    heapq.heappush(heap,n) # List에 있는 Data를 하나씩 넣어줌 heappush()
    show_tree(heap)

print("============  heappop  ============")

heapq.heapify(data) # 메모리상에서 한꺼번에 정렬 ( heappush보다 빠름 )
show_tree(data)

for n in range(3):
    min_val = heapq.heappop(data) # Heap의 데이터를 하나씩 꺼냄 ( Default : MIN_HEAP )
    show_tree(data)
    print(min_val)

print("============  heapreplace  ============")

heapq.heapify(data)
show_tree(data)

for n in [3,15]:
    min_val = heapq.heapreplace(data, n) # Heap에 있는 Data를 두번쨰 인자 값으로 대체(replace)시켜줌
    print(min_val)
    show_tree(data)

print("============  nlargest & nsmallest  ============")

# Heap Data 중에서 상위 값 ( 앞의 인자 값만큼 )
print(heapq.nlargest(2,data))

# Heap Data 중에서 하위 값
print(heapq.nsmallest(2,data))