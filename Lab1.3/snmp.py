from pysnmp.hlapi import *


IP = '10.31.70.107'
port = 161
snmp_ver = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)
snmp_int = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')


result_ver = getCmd(SnmpEngine(), CommunityData('public', mpModel=0), UdpTransportTarget((IP, port)), ContextData(), ObjectType(snmp_ver))
result_int = nextCmd(SnmpEngine(), CommunityData('public', mpModel=0), UdpTransportTarget((IP, port)), ContextData(), ObjectType(snmp_int), lexicographicMode=False)


for x in result_ver:
    for y in x[3]:
        print(y)


for x in result_int:
    for y in x[3]:
        print(str((y))[str(y).find('=') + 2:])
