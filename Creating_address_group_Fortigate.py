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

