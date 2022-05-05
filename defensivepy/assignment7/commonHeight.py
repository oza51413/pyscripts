#!/usr/bin/python3
import csv
import statistics
#Usage:extracts the most frequently found height in csv file 
def height():
	#reading the csv file 
	with open('hw_25000.csv', "r") as rf :
		csv_reader = csv.DictReader(rf)	
		for line in csv_reader:
			list = []
			list.append(line[' "Height(Inches)"']) 
	print(statistics.mode(list))
height()

