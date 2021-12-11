import sys

#Author: Daniel Edwards
#Date: 12-09-2021
#Validate each octet

#Verify each octet in the IP Addresses
def ip_addr_check(ip_list):
	octets = ip_list.split('.')
	#return print(len(octets) and type(octets))
	#Different conditions for the types of iput
	#1) Single or multiple IP Addresses submited
	#2) A file of IP Addresses submitted

	'''for ip in ip_list:
		ip = ip.rstrip("\n")
		octets = ip.split('.')
		print(octets)'''

	#[int(ip) for ip in octets if(len(octets) == 4) and (all(0 <= int(octets[ip] <=255)))]


ip_addr_check("192.168.12.4")