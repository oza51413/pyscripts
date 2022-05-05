#!/usr/bin/python3 
import re

#Usage:reads the sys log file and returns all the IPv4 addresses

def linux_logfile_reader():
	#reads the log file 
	with open('syslog','r') as rf: 
		logfile = rf.read()

	#use regex to find IPv4 pattern
	pattern = re.compile('\d{3}[.]\d{2}[.]\d{3}[.]\d{1,3}')
	addresses = pattern.finditer(logfile)
	for ip in addresses:
		print(ip.group())

linux_logfile_reader()
