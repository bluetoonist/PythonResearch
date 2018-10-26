from collections import namedtuple

Member = namedtuple('Member',['email','date'])

member1 = Member('asdf@naver.com','2014-10-04')
print(member1)

print(member1.email,member1.date)

print(len(member1))
email,date = member1
print(email,date)

stock_rec = [
    ('삼성',10,100),
    ("현대",10,90),
    ("기아",10,80),
]

def cal_stock(stock):
    tot = 0
    for n in stock:
        tot += n[1]*n[2]
    return tot

print(cal_stock(stock_rec))
Stock = namedtuple('stock',['name','amount','price'])

def cal_stock(stock):
    tot = 0
    for n in stock:
        s = Stock(*n) #*n은 하나의 요소에 대해 분리를 해주는 역할을 함
        tot += s.amount*s.price
    return tot
print(cal_stock(stock_rec))

n1 = ('삼성',10,100)
print(*n1)