
This is to help automate in the creation of address group on Fortigate firewall.

## With argument
```
import ipaddress

def cidr_to_mask(cidr):
    """Convert CIDR notation to subnet mask."""
    return str(ipaddress.ip_network(cidr).netmask)

def main():
    """Main function to convert CIDR to subnet mask."""
    ## py CIDR_to_subnetNEW.py ip_cidr.txt
    with open(sys.argv[1], 'r') as f:
        for line in f:
            # Extract IP address and CIDR notation from the line
            ip_address, cidr = line.strip().split('/')
            # Convert CIDR to subnet mask
            subnet_mask = cidr_to_mask(f"{ip_address}/{cidr}")
            # Output the results
            print(f"('{ip_address}', '{subnet_mask}'),")



if __name__ == '__main__':
    main()
 ```
The CIDR_to_subnet_with_argv.py takes a test file with ip address in the format ex. 192.168.10.1/24 on each line 
as in the file IP_CIDR_Notation.txt.

```
52.129.96.0/20
52.219.170.0/23
52.219.168.0/24
3.127.48.128/26
3.123.12.192/26
150.222.230.102/31
3.122.128.0/23
52.93.126.135/32
18.157.71.192/26
18.157.237.192/26
18.157.237.128/26
150.222.129.244/31
15.230.131.2/32
150.222.122.104/31
15.177.68.0/23
```
To run the run use: 
```
py CIDR_to_subnet_with_argv.py name_of_IP_file.txt
```

## Without argument 

```
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
 ```
The CIDR_to_subnet_without_argv.py takes no argument 
NB: Text file open from code 

## Creation of address group in Fortigate firewall

```
def generate_config(ip_list):
    config = []
    for i, (ip, subnet) in enumerate(ip_list):
        config.append(f'config firewall address')
        config.append(f'edit "amazon/{ip}"')
        config.append(f'set subnet {ip} {subnet}')
        config.append(f'next')
        config.append(f'end')
    
    return '\n'.join(config)
   
    

ip_list = [
    ('52.129.96.0', '255.255.240.0'),
    ('52.219.170.0', '255.255.254.0'),
    ('52.219.168.0', '255.255.255.0'),
    ('3.127.48.128', '255.255.255.192'),
    ('3.123.12.192', '255.255.255.192'),
    ('150.222.230.102', '255.255.255.254'),
    ('3.122.128.0', '255.255.254.0'),
    ('52.93.126.135', '255.255.255.255'),
    # ...
]

config = generate_config(ip_list)
print(config)

```
