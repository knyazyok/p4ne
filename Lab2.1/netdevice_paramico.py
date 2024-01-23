import paramiko,time,pandas,re

IP = "10.31.70.209"
REST_IP = "10.31.70.209"
LOGIN = "restapi"
PASSWORD = "j0sg1280-7@"

BUF_SIZE = 20000
TIMEOUT = 1

ssh_connection = paramiko.SSHClient()
ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_connection.connect(IP, username=LOGIN, password=PASSWORD, look_for_keys=False, allow_agent=False)
session = ssh_connection.invoke_shell()

session.send("\n")
session.recv(BUF_SIZE)
session.send("terminal length 0\n")
time.sleep(TIMEOUT)

session.send("\n")
session.recv(BUF_SIZE)
session.send("show interfaces\n")
time.sleep(TIMEOUT*2)
s = session.recv(BUF_SIZE).decode()

session.close()

iface_list = [["Name","Input Packets","Input Bytes","Output Packets","Output Bytes"]]
out = s.split("\n")
for i in out:
    if i[0] != " " and not re.search("show interfaces",i) and re.search("is",i):
        name = i.split()[0]
    elif re.search("packets input",i):
        ipackets = i.split()[0]
        ibytes = i.split()[3]
    elif re.search("packets output",i):
        opackets = i.split()[0]
        obytes = i.split()[3]
        iface_list.append([name,ipackets,ibytes,opackets,obytes])
#for i in iface_list:
#    print("\t\t\t\t".join(i))

df = pandas.DataFrame(iface_list)

print(df)