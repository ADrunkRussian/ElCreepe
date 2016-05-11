#!/usr/bin/env/ python

#Created by ADrunkRussian
#Github.com/ADrunkRussian
#Contact me on twitter @ADrunkRussian1
# V1.4

import os
import urllib2
import json
import codecs
import subprocess

os.system('cls' if os.name == 'nt' else 'clear')
ans=True
while ans:

	print 
	print '=============================================='
	print '#                                            #'
	print '#                  ElCreepe                  #'
	print '#                                            #'	
	print '=============================================='
	print 'For help type help\n'
	ans=raw_input("ElCreepe > ")

	if ans.lower()=="modules":
		os.system('cls' if os.name == 'nt' else 'clear')
		with open('Modules.txt', 'r') as f:
			for line in f:
				subprocess.call(['/bin/grep', line, 'Modules.txt'])
				break
	if ans=="help":
		os.system('cls' if os.name == 'nt' else 'clear')
		with open('Help.txt', 'r') as f:
			for line in f:
				subprocess.call(['/bin/grep', line, 'Help.txt'])
				break
 	if ans=="install":
		os.system('cls' if os.name == 'nt' else 'clear')
		ans=raw_input("Is this the first time you are updating or installing packages?\n")
		if ans.lower()=="yes" or ans.lower()=="y":
			print "\nPlease add the following to your /etc/apt/sources.list:\n\ndeb http://http.kali.org/kali kali-rolling main non-free contrib\n"
			os.system("gedit /etc/apt/sources.list")
			ans=raw_input("Are you done?\n")
			if ans.lower()=="yes" or ans.lower()=="y":
				ans=raw_input("What modules would you like to install? (Name or all)")
				if ans.lower()=="all":
					os.system("python Moduleupdate.py")
					break

		if ans.lower()=="no" or ans.lower()=="n":

			ans=raw_input("So you're updating?\n")
			if ans.lower()=="yes" or ans.lower()=="y":
				os.system("sudo apt-get -y update | sudo apt-get -y upgrade")
			if ans.lower()=="no" or ans.lower()=="n":
				break

	if ans.lower()=="goofile":
		print
        	print '======================================================================'
        	print '#                                          			    #'
        	print '#               		     Goofile    		            #'
        	print '#                                              			    #'
        	print '======================================================================'
        	print 'Goofile is a tool that scans a domain in order to locate a type of file.'

        	goofdomain=raw_input("Please enter a domain. \nElCreepe > ")

		gooftype=raw_input("\nPlease enter the types of files you would like to search for.\nEx. pdf \nPlease seperate by spaces \nElCreepe >")

		os.system("goofile -d " + goofdomain + " -f " + gooftype)

	if ans.lower()=="metagoofil":
		print
                print '======================================================================'
                print '#                                                                    #'
                print '#                             Goofile                                #'
                print '#                                                                    #'
                print '======================================================================'
                print 'Goofile is a tool that scans a domain in order to locate a type of file.'
                print 'For help type help\n'

