"""Batter Way9 컴프리헨션이 클 떄는 제너레이터 표현식을 고려

@Note
- 리스트 컴프리헨션의 문제점은 입력 시퀀스에 있는 각 값별로 아이템을 하나씩 담은 새 리스트를 통쨰로 생성
- 입력이 적을 때는 괜찮지만 클 때는 메모리를 많이 소모해서 프로그램을 망가뜨리는 원인
"""

# 1
# *파일을 읽고 각 죽에 있는 문자의 개수를 반환하는 식
# -각 줄의 길이 만큼 메모리가 필요
# -파일에 오류가 있거나 끊김이 없는 네트워크 소켓일 경우 문제 발생

# 이 문제를 해결하기 위해 제너레이터 표현식을 제공
# - 실행될 떄 출력 시퀀스를 모두 구체화(메모리에 로딩)하지 않는다.
# - 대신 한번에 한 아이템을 내주는 이터레이터로 평가된다.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
it = ((x) for x in a)
print(it)  # Generator object

# 2
# 제너레이터 표현식에서 출력을 생성하려면 내장 함 next로 반환 받은 이터레이터를 전진
# 메모리 사용량을 걱정하지 않고 제너레이터 표현식을 사용
print(next(it))

# 3
# 다른 제너레이터 표현식과 함께 사용가능
# 'it' 이터레이터를 다른 제너레이터 표현식의 입력으로 사용한 예

roots = ((x, x ** 0.5) for x in it)
print(next(roots))
