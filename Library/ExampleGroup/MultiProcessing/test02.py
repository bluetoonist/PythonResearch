from multiprocessing import Process, Manager
import Evtx.Evtx as evtx
from bs4 import BeautifulSoup

path = "C:\Windows\System32\winevt\Logs\Security.evtx"
EventCount = 0
AllEvent = 0

with evtx.Evtx(path) as log:
    for cnt in log.records():
        AllEvent += 1

def GetCount(SharedM, MinNum ,MaxNum):
    pass

# def Ret4Div(Number, p):
#     TempList = []
#     allocate = int(Number/p)
#     for _ in range(p):
#         TempList.append(allocate)
#
#     TempList[p-1] += Number%p

    # try:
    #     for i in range(len(TempList)):
    #         if i == 0:
    #             print(TempList[0])
    #         print(TempList[i],TempList[i+1])
    #         #     TempList[0] = 0
    #         # TempList[i + 1] = TempList[i] + TempList[i + 1]
    # except:
    #     pass
    #
    # return TempList

if __name__ == '__main__':
    print(AllEvent)
    # RetList = Ret4Div(AllEvent,4)
    # print(RetList)

    with Manager() as manager:
        shm = manager.list([0 for n in range(3)])
        shm[1] = []