import requests,pandas

HOST_IP='10.31.70.209'
LOGIN='restapi'
PASSWORD='j0sg1280-7@'
HEADERS = {
    "accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}
URL='/restconf/data/Cisco-IOS-XE-process-memory-oper:memory-usage-processes'
PROTO='https://'

requests.packages.urllib3.disable_warnings()
r = requests.get(PROTO + HOST_IP + URL, auth=(LOGIN, PASSWORD), headers=HEADERS, verify=False)

sorted_list = sorted(r.json()['Cisco-IOS-XE-process-memory-oper:memory-usage-processes']\
                         ['memory-usage-process'], key=lambda x: int(x['allocated-memory']),reverse=True)
top_dict = sorted_list[0:9]
top_list=[]
for i in top_dict:
    top_list.append([i['pid'],i['name'],i['allocated-memory']])
df = pandas.DataFrame(top_list,columns=["PID","Name","Allocated Memory"])
print(df.to_string(index=False))