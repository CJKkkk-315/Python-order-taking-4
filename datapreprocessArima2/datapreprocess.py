#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
datapreprocess.py : This script is used for preprocess the wind data to generate simple wind speed data for arima.
input: the original format as "dataset for wind speed and wind diriction.csv"

usage:
You can directly run this script with the filename as argument
$python ./dataset_for_wind_speed_and_wind_diriction.csv

or you can import this file as module and use the processfile function

from datapreprocess import processfile

"""

__author__      = "" 
__copyright__   = "Copyright 2022"


import pandas as pd
import sys
import os
import time


def processfile(filename): #This function read the original file and caculate the wind speed daily mean for each date.
	timestr = time.strftime("%Y%m%d-%H%M%S")
	newfile_name = "Processed_data"+timestr+".csv"
	datecount = 0
	firstline = True
	currentdate = False
	totalwindspeed = 0.0
	currentdatecounter = 0
	with open(newfile_name, 'w') as f: #write to the new processed file
		with open(filename,'r') as g: #open the original date file
			print("Processing.... read file ",filename," and write to ", newfile_name)
			for line in g: #read the file line by line
				if firstline: #skip first line
					print("count,"+"Wind Speed daily mean",file=f)
					firstline = False
					continue
				#compare the date of current line to see if it is the same with current date
				templines = line.split(',')
				tmpdate = (int(templines[0]),int(templines[1]),int(templines[2]))
				#if date is the same we add the value and take average
				#print("Date:",tmpdate,currentdate)
				if tmpdate == currentdate:

					if templines[5].strip() == "":
						continue
					totalwindspeed += float(templines[5])
					currentdatecounter += 1

				else: #if not the same we update the date and write to file


					currentdate = tmpdate
					try:
						print("Date:",currentdate)
						print(str(datecount)+","+str(totalwindspeed/currentdatecounter),file=f)
						datecount += 1
					except ZeroDivisionError:
						print("ZeroDivisionError Occured")
						pass
					totalwindspeed = 0
					if templines[5].strip() == "":
						continue
					else:
						totalwindspeed = float(templines[5])
					currentdatecounter = 1

					
			#write the last date
			if currentdatecounter > 0:
				print(str(datecount)+","+str(totalwindspeed/currentdatecounter),file=f)


def main():
	processfile(sys.argv[1])

if __name__ == "__main__":
	main()
	