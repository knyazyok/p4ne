import pprint,requests,re,pandas

IP = "10.31.70.209"
REST_IP = "10.31.70.209"
LOGIN = "restapi"
PASSWORD = "j0sg1280-7@"

headers = {
    "accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}
requests.packages.urllib3.disable_warnings()
r = requests.get("https://" + IP + '/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces', auth=(LOGIN, PASSWORD), headers=headers, verify=False)
for i in r.json()['Cisco-IOS-XE-interfaces-oper:interfaces']['interface']:
    print(i['name'])
