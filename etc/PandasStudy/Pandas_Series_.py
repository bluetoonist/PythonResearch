from pandas import Series, DataFrame

# Series는 자동으로 인덱스 생성 (0부터 시작)
kakao = Series([925600,94231,945623,965465,956489])
print(kakao)

# 리스트와 다른 점이...

# Series는 인덱싱 값을 지정할 수 있음
kakao2 = Series([925600,94231,945623,965465,956489],index=['1','2','3','4','5'])
print(kakao2)

# 알아서 덧셈 연산을 처리해 줍니다.
mine =  Series([10,20,30],index=['naver','sk','kt'])
freiend =  Series([10,20,30],index=['kt','naver','sk'])

merge = mine +  freiend
print(merge)