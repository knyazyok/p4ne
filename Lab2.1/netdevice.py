import paramiko,requests,time,re

CONSOLE_IP = "10.31.70.209"
REST_IP = "10.31.70.210"
LOGIN = "restapi"
PASSWORD = "j0sg1280-7@"
REST_PORT = "55443"

BUF_SIZE = 20000
TIMEOUT = 1

ssh_connection = paramiko.SSHClient()
ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_connection.connect(CONSOLE_IP, username=LOGIN, password=PASSWORD, look_for_keys=False, allow_agent=False)
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

print(s)
out = s.split("\n")
for i in out:
    if i[0] != " " and not re.search("show interfaces",i) and re.search("is",i):
        print(i.split()[0])
    elif re.search("packets input",i) or re.search("packets output",i):
        print (i.split()[0]+" "+i.split()[3])