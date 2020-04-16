# 데이터베이스 자료를 딕셔너리에 저장 후 정렬 시키는 방법
records = [
    {'id':'test', 'pw':'1234', 'name':'홍길동', 'hp':'010-1234-1234'},
    {'id':'test', 'pw':'1234', 'name':'강호동', 'hp':'010-1978-1234'},
    {'id':'test3', 'pw':'1234', 'name':'이경규', 'hp':'010-1334-1234'},
    {'id':'afdf2', 'pw':'1234', 'name':'이문세', 'hp':'010-1245-1234'},
    {'id':'kkine', 'pw':'1234', 'name':'이수근', 'hp':'010-1248-1234'}
]


# operator module : itemgetter
from operator import itemgetter
from pprint import pprint
rec_by_name = sorted(records, key=itemgetter('name')) #itemgetter : Get the Key
rec_by_id = sorted(records,key=itemgetter('id'))

pprint(rec_by_name)
print("")

rec_by_name_tel1 = sorted(records,key=itemgetter('id','hp'),reverse=True) # itemgetter(정렬인자1,정렬인자2)
pprint(rec_by_name_tel1)

# 데이터 베이스  group by 절과 같은 기능 수행하기
