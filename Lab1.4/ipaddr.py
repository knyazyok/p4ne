import random
from ipaddress import IPv4Network

class IPv4RandomNetwork(IPv4Network):
    def __init__(self,):
        IPv4Network.__init__(self,(random.randint(0x0b000000,0xdf000000),random.randint(8,24)),False)
    def key_value(self):
        return int(str(int(self.netmask))+str(int(self.network_address)))
    def regular(self):
        if self.is_global():
            return True
        else:
            return False

def sort_key(i):
    return i.key_value()

nets=[]
for i in range(0,50):
    net = IPv4RandomNetwork()
    if net.regular:
        nets.append(net)

for i in sorted(nets,key=sort_key):
    print(i)