import os.path
import argparse

#Author: Daniel Edwards
#Date: 12-08-2021
#Validate IP file existence

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help='Specify the file and/or the file\'s path containing IP addresses')
parser.add_argument('-i', '--ip', nargs='+', help='Specify IP address(es)')
args = parser.parse_args()


#Determine
def validate_ip_input():

	if args.file:
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

	elif args.ip:

		return print(f"The IPs are {args.ip}")

	
validate_ip_file()