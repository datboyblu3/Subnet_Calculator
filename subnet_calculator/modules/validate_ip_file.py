import os.path
import argparse

#Author: Daniel Edwards
#Date: 08-12-2021
#Validate each octet

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help='Specify the file and/or the file\'s path containing IP addresses')
parser.add_argument('-i', '--ip', help='Specify IP address(es)')
args = parser.parse_args()


#Determine if file exists
def validate_ip_file():
	ip_file = args.file

	#Verify if file exists
	while True:
		if os.path.isfile(ip_file):
			print("Good to go")
			break
		else:
			print("File does not exist, please try again")

	selected_ip_file = open(ip_file,'r')
	selected_ip_file.seek(0)
	ip_list = selected_ip_file.readlines()
	selected_ip_file.close()

	return ip_list

	
