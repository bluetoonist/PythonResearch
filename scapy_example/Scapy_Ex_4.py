from scapy_example.all import *
"""
packet filtering 

"""

def ShowPacket(packet):
    data ="%s" %(packet[TCP].payload)
    if 'user' in data.lower() or 'pass' in data.lower():
        print("++[%s] :%s" %(packet[IP].dst ,data))
              
def main(param_filter):
    sniff(filter=param_filter, prn=ShowPacket, count=0 , store=0)

if __name__ == '__main__':
    filter1 = "tcp port 25 or tcp port 110 or tcp port 114"
    main(filter1)
