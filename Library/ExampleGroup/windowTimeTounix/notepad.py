# windows Time stamp to unix
# 윈도우 타임스탬프를 현재 타임스탬프로 바꿔주는 코드

from datetime import datetime,timedelta

ExampleHexValue = "01d6120f03bdb599"
us = int(ExampleHexValue,16) /10.
print(datetime(1601,1,1)+timedelta(microseconds=us))