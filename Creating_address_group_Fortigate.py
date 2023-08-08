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
    ('192.168.10.0', '255.255.255.128'),
    ('192.168.1.0', '255.255.255.128'),
    ('192.168.2.0', '255.255.255.128'),
    ('192.168.3.0', '255.255.255.128'),
    ('192.168.4.0', '255.255.255.128'),
    ('192.168.5.0', '255.255.255.128'),
    ('192.168.6.0',  '255.255.255.128'),
    # ...
]

config = generate_config(ip_list)
print(config)

