import re,ipaddress,glob

LOG_PATH="C:\\Users\\utkinia\\Documents\\Python\\config_files"
def str_to_ip(ipstr):
    if re.search("ip address", ipstr):
        net_objects = re.search("([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})", ipstr)
        if net_objects:
            addr = ipaddress.IPv4Interface(net_objects.groups())
            return addr
        else:
            return None
    else:
        return None

def sort_key(i):
    return int(i.ip) + (int(i.network.netmask) * 2**32)


all_address=[]
for i in glob.glob(LOG_PATH+"\\*.log"):
    f = open(i)
    for j in f:
        a = str_to_ip(j)
        if a != None:
            all_address.append(a)

for i in sorted(all_address,key=sort_key):
    print(i)