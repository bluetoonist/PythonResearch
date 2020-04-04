from multiprocessing import Process, Manager
import os

def RetSum(Mobj):
    funcList = [1,2,3]
    for x in funcList:
        Mobj[0] += x
    print("PROCESS ID : " ,os.getpid()," Number : ",Mobj[0])

if __name__ == '__main__':
    with Manager() as manager:
        Mobj = manager.list([0 for x in range(3)])
        MpList= []

        for _ in range(3):
            MpList.append(Process(target=RetSum,args=(Mobj,)))

        for _ in MpList:
            _.start()
        for _ in MpList:
            _.join()

        print(Mobj)