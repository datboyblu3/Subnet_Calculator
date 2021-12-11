import sys

#Author: Daniel Edwards
#Date: 12-09-2021
#Validate each octet

#Verify each octet in the IP Addresses
def ip_addr_check(ip_list):

	#Different conditions for the types of iput
	#1) Single or multiple IP Addresses submited
	#2) A file of IP Addresses submitted

	for ip in ip_list:
		ip = ip.rstrip("\n")
		octets = ip.split('.')
		print(octets)

		#[(ip) for ip in ip_list if(len(octets) == 4) and (all(0 <= int(octets[ip] <=255)))]

