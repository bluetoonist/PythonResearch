from multiprocessing import Process, Manager
import Evtx.Evtx as evtx
from bs4 import BeautifulSoup

path = "C:\Windows\System32\winevt\Logs\Security.evtx"
EventCount = 0
AllEvent = 0
with evtx.Evtx(path) as log:
    for x in log.records():
        AllEvent +=1

def CountTotal(d,MinNum,MaxNum):
    global EventCount
    print(MinNum,MaxNum)
    try:
        with evtx.Evtx(path) as log:
            for y in range(MinNum, MaxNum):
                print("Numbering : ",y)
                GetOne = log.get_record(1)
                print(GetOne)
                # GetOne = log.get_record(int(y))
                # soup = BeautifulSoup(GetOne.xml(), "html.parser")
                # System_ = soup.find("system")
                # EventId = int(System_.find("eventid").text)
                # if EventId == 4624:
                #     EventCount += 1
                #     print("EvsentCount", EventCount)
                #     d[0] += EventCount
    except Exception as  e:
        print(e)

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.list([0 for i in range(5)])
        print(AllEvent)

        p1 = Process(target=CountTotal, args=(d,1,13325))
        # p2 = Process(target=CountTotal, args=(d,13325,AllEvent-13325))
        p1.start()
        # p2.start()

        p1.join()
        # p2.join()

        print(d)

