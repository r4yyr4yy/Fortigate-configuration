import socket
import struct

def cidr_to_subnet(cidr):
    network, net_bits = cidr.split('/')
    host_bits = 32 - int(net_bits)
    netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
    return network, netmask

with open('ip_cidr.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    cidr = line.strip()
    network, netmask = cidr_to_subnet(cidr)
    print(f"('{network}', '{netmask}'),")
