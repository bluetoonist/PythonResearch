# 우선 순위 큐 구현하기 ( 우선 순위에 따라 아이템을 정렬,
#                         우선 순위가 가장 높은 아이템을 pop )

# queue.PriorityQueue Class use ( Study in Thread After Write!)

# heapq Module application Create!
import heapq

class PriorityQueue:
    def __init__(self):
        self._list = []
        self.idx = 0 # 입력되는 순서를 나타내는 인덱스
    def put(self,item,priority):
        heapq.heappush(self._list,(priority,self.idx,item))
        self.idx +=1
    def pop(self):
        return heapq.heappop(self._list)

class Item:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return "Item({!r})".format(self.name) # !r은 repr() 호출하는 것과 같다 ( repr()은 객체를 문자열로 바꿔줌 ) !a는  ascii 로 변환

pQ = PriorityQueue()
pQ.put(Item("홍길동"),1)
pQ.put(Item("장길산"),2)
pQ.put(Item("김두한"),3)
pQ.put(Item("일지매"),4)

print(pQ._list)

print(pQ.pop())
print(pQ.pop())
print(pQ.pop())
print(pQ.pop())


