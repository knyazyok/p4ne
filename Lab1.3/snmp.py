from pysnmp.hlapi import *

IP="10.31.70.209"
PORT=161
DESCR_MIB="sysDescr"
IFACES_MIB="1.3.6.1.2.1.2.2.1.2"
COMMUNITY="public"
HUMAN_DATA_ELEMENT=3

def snmp_human_data(snmp_data):
    for i in snmp_data:
        for j in i[HUMAN_DATA_ELEMENT]:
            print(j)

snmp_name = ObjectIdentity('SNMPv2-MIB',DESCR_MIB,0)
snmp_interfaces = ObjectIdentity(IFACES_MIB)

descr = getCmd(SnmpEngine(), CommunityData(COMMUNITY, mpModel=0), UdpTransportTarget((IP, PORT)), ContextData(), ObjectType(snmp_name))
ifaces = nextCmd(SnmpEngine(), CommunityData(COMMUNITY, mpModel=0), UdpTransportTarget((IP, PORT)), ContextData(), ObjectType(snmp_interfaces),lexicographicMode=False)

print("Description:")
snmp_human_data(descr)
print("")
print("Interfaces:")
snmp_human_data(ifaces)