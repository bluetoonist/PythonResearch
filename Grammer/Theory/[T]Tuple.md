# Tuple

> Sequence Unpacking     
```Example
- '*' 연산자를 사용해 다음과 같이 이용
>> x,*y = (1,2,3,4)
>> x = 1
>> y = 2,3,4 
```

> Named Tuple  
> 성능은  일반 튜플과 비슷  
> 튜플 항목을 인덱스 위치 또는 이름으로 참조 가능
```buildoutcfg
>> import collections.namedtuple  
>> Person = collections.namedtuple("Person","name age, gender")  
>> p = Peson("Ko, 25, 'Man'")
```
