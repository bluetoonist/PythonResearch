# UnPacking

pa = (1,2)

a,b = pa

print(a)
print(b)

li_data = ["홍길동",23,"서울",(1980,11,21)]

#name, age, local, birthday = li_data
#print(name,age,local,birthday)

#name, age, local, (year,month,day) = li_data
#print(year,month,day)

# Etc..
str1 = "Hello"
a,b,c,d,e = str1

# 특정 값 무시 or '*'를 이용하여 여러개를 언패킹

#특정 값 무시 '_'
name, _,local,_ = li_data
print(name,local)
person_info = ("장길산","jks@naver.com","010-1234-1234",'02-212-4565')

# How To Use : '*'
# 전체 길이를 알 수 없는 시퀀스에서 사용 가능
name, email, *phone = person_info
print(name,email,phone)

pointValue = [10,5,12,11,22,14,12,15,10,10,15,14]

*prePoint,curPoint = pointValue

print(prePoint)
print(curPoint)

address = [('우',234,123),("도","서울"),("도","경기"),("우",123,234)]

def show_zipcode(num1,num2):
    print("우",num1,num2)

def show_local(str1):
    print("도",str1)

for key,*arg in address:
    if key == "우":
        show_zipcode(*arg)
    elif key == "도":
        show_local(*arg)

str2 = "홍길동/23/12121212/123213-3434/123123123/서울"

name,age, *num,local= str2.split("/")
print(local)

li_data = ["홍길동",23,"서울",(1980,11,21)]
name,*_, (year,*_) = li_data
print(name)
print(year)