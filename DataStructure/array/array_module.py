import array
import binascii
#array 형태는 binary 형태로 씀

# array.array('typecode',value)
arr = DataStructure.array.array('i', range(5))

# array의 내용을 파일에 쓰거나 읽기
# tofile : write to file Function

f = open("test.txt", "w+b")
arr.tofile(f)
f.flush()

# array ----(stream(binary))----> file

with open("test.txt", "rb") as f1:
    data = f1.read()

    # Data return Binary
    print(binascii.hexlify(data))

    f1.seek(0) # file pointer return
    arr2 = DataStructure.array.array('i')
    arr2.fromfile(f1,len(arr))

    print(arr2)
