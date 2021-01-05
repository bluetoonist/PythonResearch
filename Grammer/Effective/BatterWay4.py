"""Batter Way 4 : 복잡한 표현식 대신 헬퍼 함수 작성
"""

# Example, URL에서 쿼리 문자열을 디코드
from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=10)
print(repr(my_values))

# 결과 딕셔너리에 get 메서드를 사용하면 각 상황에 따라 다른 값을 반환
print("Red : ", my_values.get("red"))
print("Green : ", my_values.get("green"))
print("Opacity :", my_values.get("opacity"))

# 파라미터가 없거나 비어있으면 기본값으로 0으로 할당
# Tips) 빈 문자열, 빈 리스트, 0이 모두  암시적으로 False로 평가됨
# 첫 번째 서브 표현식이 False 일 때 or 연산자 뒤에 오는 서브 표현식을 평가한 값이 됨

red = my_values.get('red', [''])[0] or 0
green = my_values.get('green', [''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0

print("Red: %r " % red)
print("Green : %r" % green)
print("Opacity: %r" % opacity)


# Helper Function Desciption !
def get_first_value(values, key, default=0):
    found = values.get(key, [])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found


# Helper Function Call
green = get_first_value(my_values, "green")
print(green)
