#!/usr/bin/env python
#title           : Device42.py
#description     : This script is used to get details of server/device from Device42
#author          : Sunny Thakur
#date		 : 20190329
#version         : 1.0
#usage           : python Device42.py
#python_version  : 2.7  
#==============================================================================
# Importing the modules needed to run the script.
import requests
import json
import sys
import getpass

# URLS List
hosturl='https://dcmgr.hou1.hostgator.com/api/1.0/devices/name/'
ipurl='https://dcmgr.hou1.hostgator.com/api/1.0/search/?query=ip&string='
passurl='https://dcmgr.hou1.hostgator.com/api/1.0/passwords/?device='

# Ignore SSL warnings
requests.packages.urllib3.disable_warnings()

# User credentials
username=raw_input("Enter the username : ")
password=getpass.getpass("Enter the password : ")

# Function to get details from hostname
def searchbyhost():
        hostname=raw_input("Enter the hostname : ")
        response = requests.get(hosturl+hostname, verify=False, auth=(username, password))
        passresponse = requests.get(passurl+hostname+"&plain_text=yes", verify=False, auth=(username, password))
        if str(response.status_code) == '200' and str(passresponse.status_code) == '200':
                jsondata= json.loads(response.text)
                passdata= json.loads(passresponse.text)
                listdata=['hw_model','manufacturer','os','service_level','type','virtual_host_name','ip_addresses']
                print("\n======== Details for "+hostname+" ========")
                for data in listdata:
                        if data in jsondata and str(jsondata[data]) != "None" and data == 'ip_addresses':
                                length=len(jsondata[data])
                                for i in range(length):
                                        if jsondata[data][i]['label'] == '' or str(jsondata[data][i]['label']) == 'None':
                                              	pass
					else:
						print(jsondata[data][i]['label'].strip().upper()+' address is : '+jsondata[data][i]['ip'])
                        elif jsondata[data] == 'virtual':
                                print(data.upper()+" : "+jsondata[data])
                                print('Host machine '+jsondata['virtual_host_name'])
                        elif data in jsondata and str(jsondata[data]) != "None":
                                print(data.upper()+" : "+jsondata[data])
                        else:
				pass
                if 'Passwords' in passdata:
                        for i in range(len(passdata['Passwords'])):
                                if passdata['Passwords'][i]['label'] == '':
                                        pass
                                else:
                                        print(passdata['Passwords'][i]['label'].strip().upper()+' password is '+passdata['Passwords'][i]['password'])
                else:
                        print("No passwords found")
        elif str(response.status_code) == '404':
		print("Device not found")
	else:
                print("Error connecting kindly check username/password")

# Function to get hostname/device from IP address                        
def searchbyIP():
        IP=raw_input("Enter the IP : ")
        response = requests.get(ipurl+IP, verify=False, auth=(username, password))
        if str(response.status_code) == '200':
                jsondata= json.loads(response.text)
                if "no matching IP found" in jsondata:
                        print("\n-----"+jsondata.upper()+"-----\n")
                else:
                        print("Hostname is "+jsondata['ips'][0]['device'])
                        question = raw_input("Do you want to continue to get hostname details ? [y/n] ")
                        if 'y' in question.lower():
                                searchbyhost()
                        else:
                                exitscript()
        else:
                print("Error connecting kindly check username/password")
def exitscript():
        print("Exiting..Bye...!")
        sys.exit()

print("1) HOSTNAME\n2)IP ADDRESS\n3)Exit")
choice=raw_input("Select the option to search : ")
switcher = {
        1: searchbyhost,
        2: searchbyIP,
        3: exitscript
        }

def selectoption(argument):
	func = switcher.get(argument, lambda :'Invalid option exiting the script')
    	return func()

if choice == '1' or choice == '2' or choice == '3':
	selectoption(int(choice))
else:	
	try:
		print(selectoption(int(choice)))
	except ValueError:
		print("Kindly provide valid option in number")
