"""Batter Way11 : 이터레이터를 병렬 처리시 zip !

@ NOTE
- 리스트 컴프리헨션을 사용하면 소스 리스트(Source List)에 표현식을 적용하여 파생 리스트(Derived List)를 쉽게 얻을 수 있음

"""

names = ["Cecilia", "Lise", "Marie"]
letters = [len(n) for n in names]

# 1
# 두 리스트를 병렬로 순회하라면 names의 길이만큼 순회
logest_name = None
max_letters = 0

for i in range(len(names)):
    count = letters[i]
    if count > max_letters:
        logest_name = names[i]
        max_letters = count
print(logest_name)
# 문제
# 1.전체 루프문이 보기 안 좋아진다.
# 2.names와 letter를 인덱스로 접근하면 코드를 읽기 어려워짐
# 3.루프의 인덱스 i로 배열에 접근하는 동작이 두번 일어남

# 2
# enumerate를 사용하면 문제점을 약간 개선할 수 있지만 완벽하진 않음

for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        logest_name = name
        max_letters = count

# 3
# 위의 코드를 좀 더 명료하게 하는 내장 함수 zip을 제공
# zip은 지연 제너레이터로 이터레이터 두 개 이상을 감쌈
# zip 제너레이터는 각 이터레이터로부터 다음 값을 담은 튜플을 얻어옴

for name, count in zip(names, letters):
    if count > max_letters:
        logest_name = name
        max_letters = count

# 4 zip을 사용할 떄는 두 가지 문제가 있음
# 1. Python2에서는 zip이 제너레이터가 아님, 완전히 순회해서 zip으로 생성한 모든 튜플을 반환
# 이 과정에서 메모리를 많이 사용하여 프로그램이 망가짐 Python2에서 매우 큰 이터레이터를 zip으로 묶어서
# 사용하려 한다면 내장 모듈 itertools에 있는 izip을 사용

# 2. 입력 이터레이터들의 길이가 다르면 zip이 이상하게 동작, 즉 이터레이터릐 길이 같을 때 제대로 동작
# zip으로 실행할 리스트이 길이가 같다고 확신할 수 없다면 대신 내장 모듈 itertools의 zip_longest를 사용하는 방안 고려 (Python2, izip_logest)
