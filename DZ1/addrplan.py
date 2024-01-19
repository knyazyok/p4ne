import re,ipaddress,glob,openpyxl

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
    return int(i.network_address) + (int(i.netmask) * 2**32)


all_address=[]
for i in glob.glob(LOG_PATH+"\\*.log"):
    f = open(i)
    for j in f:
        a = str_to_ip(j)
        if a != None:
            all_address.append(a)

networks=[]
for i in all_address:
    networks.append(i.network)

wb = Workbook()
ws = wb.active
ws.title = "Address Plan"
ws.append(["Network","Mask"])
for i in sorted(set(networks),key=sort_key):
    ws.append(str(i.network_address),str(i.netmask))
ft = Font(bold=True)
for row in ws["A1:B1"]:
    for cell in row:
        cell.font = ft
wb.save(LOG_PATH+"\\addrplan.xlsx")
