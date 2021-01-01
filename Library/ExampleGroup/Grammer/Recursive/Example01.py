# 1부터 num가지의 곱이 출력되게 만들자

def multiple(data):
    # data 가 1보다 크면 data return
    # 즉, 종료 조건에 해당
    # data가 1일 때, 결과값 1 반환

    if data <=1 :
        return data
    # 인자로 받은 data와 data-1을 호출
    # 1. 1 * (1-0)
    # 2. data가 2일 떄, 결과값 2 * (2-1) 반환
    # 3. data가 3일 때, 결과값 3 * (3-1) * (2-1) 반환
    return data* multiple(data-1)

# 호출한 횟수는 1부터 n까지 곱하는 함수
for _ in range(1,10):
    print(_, multiple(_))