#array : 시퀀스 자료구조를 정의하는데 , list와의 차이점은 모든 자료형이 동일하다

import array

str1 = "aabcdefgh"

# array.array(typecode,  data)
# 지원하는 타입 코드가 궁금하다면 -> print(array.typecodes)
# https://docs.python.org/3.7/library/array.html

arr = DataStructure.array.array("u", str1)
print(arr)

arr1 = DataStructure.array.array('i', range(5))
print(arr1)

arr1.extend(range(5)) # extend 가능
print(arr1)

print(arr1[3:6]) # 문자열 슬라이싱 가능

print(list(enumerate(arr1))) # enumerate를 적용한 array