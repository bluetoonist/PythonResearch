"""Batter Way 3
: bytes, str, unicode 의 차이점을 알자

[+]NOTE
- 문자 타입이 분리되어 있어 2가지 상황에 부딪힘
1. UTF-8 로 인코딩 된 문자인 Raw 8 비트 값을 처리하려는 상황
2. 인코딩이 없는 유니코드 문자를 처리하려는 상황

위 두 가지 상황에서 변환하고 코드에서 원하는 타입과 입력값의 타입이
정확히 일치하게 하려면 헬퍼 함수 두 개가 필요하다.
"""


# Python3
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode("utf-8")
    else:
        value = bytes_or_str
    return value  # str 인스턴스


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode("UTF-8")
    else:
        value = bytes_or_str
    return value  # bytes 인스턴스


""" Python에서 raw 8bit 값과 유니코드 문자를 처리할 떄 중대한 이슈 두 개를 알아둬야함
[ISSUE #1]
- Python2에서 str이 7비트 아스키 문자만 포함하고 있다면, unicode와 str 인스턴스가 같은 타입처럼 보인다는 점
- Python3에서는 bytes와 str 인스턴스는 빈 문자열이라도 절대 같지 않으므로 함수에 넘기는 문자열의 타입을 신중하게 처리

[ISSUE #2]
- Python3에서 내장 함수 open이 반환하는 파일 핸들을 사용하는 연산은 기본으로 UTF-8 인코딩을 사용한다. (Python2는 바이너리)
"""

# 아래의 코드는 Python3에서는 에러가 남
import os

with open("test.bin", "w") as f:
    f.write(os.urandom(10))

# Solution : 데이터를 문자 쓰기모드('w')가 아닌 바이너리 쓰기 모드('wb')로 오픈
with open("test.bin", "wb") as f:
    f.write(os.urandom(10))
