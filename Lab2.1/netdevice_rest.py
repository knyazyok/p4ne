import pprint,requests,re,pandas

IP = "10.31.70.209"
REST_IP = "10.31.70.209"
LOGIN = "restapi"
PASSWORD = "j0sg1280-7@"
INTERFACE_PATH="/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces"
REST_PROTO="https://"
HEADERS = {
    "accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}


requests.packages.urllib3.disable_warnings()
r = requests.get(REST_PROTO + IP + INTERFACE_PATH, auth=(LOGIN, PASSWORD), headers=HEADERS, verify=False)
iface_list=[]
for i in r.json()['Cisco-IOS-XE-interfaces-oper:interfaces']['interface']:
    in_packets_total=int(i['statistics']['in-broadcast-pkts'])+int(i['statistics']['in-multicast-pkts'])+int(i['statistics']['in-unicast-pkts'])
    out_packets_total = int(i['statistics']['out-broadcast-pkts'])+int(i['statistics']['out-multicast-pkts'])+int(i['statistics']['out-unicast-pkts'])
    iface_list.append([i['name'],in_packets_total,int(i['statistics']['in-octets']),out_packets_total,int(i['statistics']['out-octets'])])

df = pandas.DataFrame(iface_list,columns=["Name","Input Packets","Input Bytes","Output Packets","Output Bytes"])
print(df.to_string(index=False))