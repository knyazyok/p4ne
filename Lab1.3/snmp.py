from pysnmp.hlapi import *

IP="10.31.70.209"
PORT=161
DESCR_MIB="sysDescr"
IFACES_MIB="1.3.6.1.2.1.2.2.1.2"

snmp_name = ObjectIdentity('SNMPv2-MIB',DESCR_MIB,0)
snmp_interfaces = ObjectIdentity(IFACES_MIB)

descr = getCmd(SnmpEngine(), CommunityData('public', mpModel=0), UdpTransportTarget((IP, PORT)), ContextData(), ObjectType(snmp_name))
ifaces = nextCmd(SnmpEngine(), CommunityData('public', mpModel=0), UdpTransportTarget((IP, PORT)), ContextData(), ObjectType(snmp_interfaces),lexicographicMode=False)

print("Description:")
for i in descr:
    for j in i[3]:
        print(j)

print("")

print("Interfaces:")
for i in ifaces:
    for j in i[3]:
        print(j)