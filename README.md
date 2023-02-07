
This is to help automate in the creation of address group on Fortigate firewall.

# With argument

The CIDR_to_subnet_with_argv.py takes a test file with ip address in the format ex. 192.168.10.1/24 on each line 
as in the file IP_CIDR_Notation.txt.

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

To run the run use: py CIDR_to_subnet_with_argv.py name_of_IP_file.txt

# Without argument 

The CIDR_to_subnet_without_argv.py takes no argument 
however, the name of the text file as in line 10 of the script needs to be edited in the format 