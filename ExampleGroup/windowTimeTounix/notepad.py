from datetime import datetime,timedelta

dt2 = "01d6120f03bdb599"
us = int(dt2,16) /10.
print(datetime(1601,1,1)+timedelta(microseconds=us))