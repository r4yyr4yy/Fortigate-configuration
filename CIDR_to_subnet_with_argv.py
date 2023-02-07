import sys
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
