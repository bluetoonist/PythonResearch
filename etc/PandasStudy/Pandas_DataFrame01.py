from pandas import DataFrame

# DataFrame 객체를 생성하는 가장 쉬운 방법은 파이썬의 딕셔너리를 사용하는 것입니다
raw_data = {'col0':[1,2,3,4],
            'col1':[10,20,30,40],
            'col2':[100,200,300,400]}

data = DataFrame(raw_data)
print(data)

# 파이썬 딕셔너리에서 키를 통해 값에 접근했던 것과 같이 DataFrame 객체의 각 칼럼에 접근할 수 있습니다.
print("="*50)
print(data['col0'])

print("="*50)
print(data['col1'])

print("="*50)
print(data['col2'])