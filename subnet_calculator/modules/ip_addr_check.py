import sys

#Author: Daniel Edwards
#Date: 12-09-2021
#Validate each octet

#Verify each octet in the IP Addresses
def ip_addr_check(ip_list):

	for x,ip in enumerate(ip_list):
		ip = ip.rstrip("\n")
		octets = ip.split('.')
		if(len(octets) == 4) and (1 <= octets[x] <= 255):
			continue
		else:
			print("Invalid IP address")
			sys.exit()
			
	
	#[ip for ip in octets if(len(octets) == 4) and all(0 <= octets[ip] <=255)]
	


ip_addr_check("192.168.12.4")