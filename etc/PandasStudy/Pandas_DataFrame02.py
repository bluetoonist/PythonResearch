from pandas import Series, DataFrame

daeshin = {'open':  [11650, 11100, 11200, 11100, 11000],
           'high':  [12100, 11800, 11200, 11100, 11150],
           'low' :  [11600, 11050, 10900, 10950, 10900],
           'close': [11900, 11600, 11000, 11100, 11050]}

daeshin_day = DataFrame(daeshin)
print(daeshin_day)

# DataFrame 객체에서 칼럼의 순서는 DataFrame 객체를 생성할 때 columns라는 키워드를 지정할 수 있습니다.
daeshin_day = DataFrame(daeshin, columns=['open', 'high', 'low', 'close'])

# DataFrame에서 인덱스 역시 DataFrame 객체를 생성하는 시점에 index를 통해 지정할 수 있습니다
date = ['16.02.29', '16.02.26', '16.02.25', '16.02.24', '16.02.23']
daeshin_day = DataFrame(daeshin, columns=['open', 'high', 'low', 'close'], index=date)
print("="*50)
# DataFrame 객체의 로우에 접근하려면 loc 메서드를 사용해 인덱스 값을 넘겨주면 됩니다
print(daeshin_day.loc['16.02.29'])