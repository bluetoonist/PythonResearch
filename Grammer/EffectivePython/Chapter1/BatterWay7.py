"""map과 filter 대신 리스트 컴프리헨션을 사용
"""

# 1
# 리스트에 있는 각 숫자의 제곱을 계산하는 식
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = [x ** 2 for x in a]
print(squares)

# 2
# 인수가 하나뿐인 함수를 적용하는 상황이 아니면,
# 간단한 연산에는 리스트 컴프리헨션이 내장 함수 map보다 명확
# map을 쓰려면 계산에 필요한 lambda 함수를 생성해야 해서 깔끔해보이지 않음
squares = map(lambda x: x ** 2, a)
print(list(squares))

# 3
# 리스트 컴프리헤션을 사용하면 입력 리스트에 있는 아이템을 걸러낼 수 있음
even_squares = [x ** 2 for x in a if x % 2 == 0]
print(even_squares)

# 4
# filter를 map 연계해서 사용해도 같은 결과를 얻을 수 있지만 훨씬 읽기 어려움
alt = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, a))
assert even_squares == list(alt)
