# 딕셔너리의 특정부분을 이용해서 새로운 딕셔너리를 만들기

stock = {
"삼성":100,
"현대":90,
"기아":80,
"대우":70,
"아모레":120,
"코리아나":60,
"한국화장품":80
}

st1 ={key:value for key,value in stock.items() if value >= 100}
print(st1)

#stock_car = {key for key,value in stock.items()}
#print(stock_car)
stock_car_key = {'삼성','현대','기아','대우'}
stock_car_key = { key:value for key,value in stock.items() if key in stock_car_key }
print(stock_car_key)

# dict()
aa = dict(a=1,b=2,c=3)
print(aa)
abc = dict([("aa",11),("bb",22),("cc",33)])
print(abc)

stock_car1 = dict([key,value] for key,value in stock.items() if value>=100 ) # 성능면에서 떨어짐
print(stock_car1)
#성능면에서 속도가 떨어짐 굳이 사용하는 것을 권하지는 않음
stock_car1 = {key:stock[key] for key in stock.keys() & stock_car_key}
print(stock_car1)

