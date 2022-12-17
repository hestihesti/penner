from termcolor import colored
import socket
import time
import os
import sys

def booking():
	x = ''
  
# Runs on loop so you can retrieve multiple ip address's
	while x != 'quit':
		url = input('What Is The URL: ')
		IP_address = socket.gethostbyname(url)
		print(IP_address)
		layout2 = IP_address + '\n'

		with open('IPs.txt', 'a') as f2:
			f2.write(layout2)
      print(colored('IP Address Has Been Saved To "IPs.txt"', 'green'))
		x = input('[cont]inue  OR  [quit]: ')

booking()
