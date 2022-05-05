#!/usr/bin/python3
import os
import re

#Usage:utilizes the re module to parse all the emails from the attached file

def parse_emails():
	#reading the .txt file 
	with open('sampleungfacultystaffinfo.txt','r') as rf:
		file = rf.read()
	#using the re module to search for patterns
	pattern = re.compile('[a-zA-z0-9.-]+@[a-zA-z-]+\.(.com|edu)')
	matches = pattern.finditer(file)
	for match in matches:
		print(match.group())	
parse_emails()

