# 딕셔너리에서 최소/최대 정렬
fruits = {
    "사과":300,
    "오렌지":200,
    "바나나":500,
    "배":1000,
    "포도":2000
}

# zip() 함수를 이용해서 키와 값을 뒤집는다.

# MAX
max_fruits = max(zip(fruits.values(),fruits.keys()))
print(max_fruits)
#MIN
min_fruits = min(zip(fruits.values(),fruits.keys()))
print(min_fruits)

#키를 비교
print(min(fruits))
print(max(fruits))

# value가 동일값인 경우 key를 가지고 비교
fruits = {"사과":300, "오렌지":300}
print( min(zip(fruits.values(), fruits.keys())))

