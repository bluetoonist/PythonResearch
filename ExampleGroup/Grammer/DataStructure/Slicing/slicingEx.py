# 슬라이스에 'name' 설정하기

# 슬라이스
aa = [1,2,5,11,3,6,7,10]
saa = aa[3:6]
print(saa)

# name slicing
record = "김가네2419911123"
name = slice(0,3,2)
birth_year = slice(5,9)
print(record[birth_year])
print(record[name])

# Ex
code = "2011 2014 2015 1999 1981"
scode = slice(0,10)
print(code[scode])
scode = slice(0,10,4) # (start,stop,step)
print(code[scode])

# indices(len)
record1 = "고가네1501012341234서울"
name = slice(3,20,2)
print(len(record1))
print(name.indices(len(record1)))