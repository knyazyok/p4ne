import glob

ip_addr=[]
for i in glob.glob("C:\\Users\\utkinia\\Documents\\Python\\config_files\\*.log"):
    f=open(i)
    for string in f:
        if string.find("ip address") != -1 & string.find("no") == -1:
            string=string.strip().replace("ip address","")
            ip_addr.append(string)

for i in sorted(list(set(ip_addr))):
    print(i)