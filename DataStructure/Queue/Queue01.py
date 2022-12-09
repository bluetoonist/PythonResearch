import queue

# FIFO
q = queue.Queue()

for i in range(3):
    q.put(i)

# FIFO
# Frist In Frist Out

while not q.empty():
    print(q.get(),end=' ') # Queue 끄집어 냄
print()

# LIFO Queue
# LIFO? Last IN First Out
# 먼저 들어간게 나중에 나옴

lq = queue.LifoQueue()

for i in range(5):
    lq.put(i) # 4 3 2 1 0

while not lq.empty():
    print(lq.get(),end=' ')
print()

