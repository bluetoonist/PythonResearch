""" None을 반환하기 보다는 예외를..
"""

# Bad Case
def devide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return None

    # 분자가 0이 되면 반환 값도 0이 됨 (분모가 0일 아닐 떄)

# `None` 대신 False에 해당하는 값을 검사할 수 있음 (14 ~ 21 Line)
x,y = 0,5
result = devide(x,y)

# Caused
# result의 bool 값은 False
# not result는 True가 됨
if not result:
    print("Invalid Inputs")


print("="*100)
# Solution 1
# 반환 값을 두 개로 나눠서 튜플에 담는 것 -> None을 반환하는 것 만큼 나쁨
def solution_1(a,b):
    try:
        return True, a/b
    except ZeroDivisionError:
        return False, None

success, result = solution_1(x,y)
if not success:
    print("Invalid Inputs")

# Solution 2
# 호출하는 쪽에 입력값이 잘못 됐음을 알리도록 수정
def devide(a,b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise  ValueError("Invalid inputs") from e

# 호출하는 쪽에서 잘못된 입력에 대한 예외를 처리
x,y = 5,2
try:
    result = devide(x,y)
except ValueError:
    print("Invalid inputs")
else:
    print("Result is %.1f" % result)