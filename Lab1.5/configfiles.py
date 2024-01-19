import glob

ip_addr=[]
for i in glob.glob("C:\\Users\\utkinia\\Documents\\Python\\config_files\\*.log"):
    f=open(i)
    for string in f:
        if string.find("ip address") != -1 and string.find("no") == -1:
            string=string.replace("ip address","").strip()
            elements=string.split(" ")
            for i in elements:
                if not i[0] in "0123456789" or i == "":
                    elements.remove(i)
            ipaddr = " ".join(elements)
            ipaddr = ipaddr.strip()
            ip_addr.append(ipaddr)

for i in sorted(list(set(ip_addr))):
    print(i)