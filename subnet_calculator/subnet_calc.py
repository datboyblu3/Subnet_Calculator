import sys
import random
import os.path
import argparse

#Author: Daniel Edwards
#Date: 08-12-2021
#Validate each octet

parser = argparse.ArgumentParser()
parser.add_argument('--file', '-f', help='Specify a file containing IP addresses')
parser.add_argument('-i', '--ip', help='Specify IP address(es)')
args = parser.parse_args()


def validate_ip_octet(ip):

	'''
	Read input from command line for a file of IPs, single IP or
	an x amount specified by the user
	'''
	try:

		while True:
			#Take input as either a file or single IP address

	except KeyboardInterrupt:
		print("User interruption! Exiting now!")
	except ValueError:
		print("Incorrect value entered, please try again!")