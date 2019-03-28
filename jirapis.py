#!/usr/bin/env python
import requests
import json
import urllib3
import getpass
import os

jiraurl='https://jira.endurance.com/rest/api/2/search?jql=description~%22List%20of%20Affected%22%20and%20project=%22Enterprise%20-%20Monitoring%20Center%20Server%20Issues%22%20and%20status=open&fields=id,key,description'

username=raw_input("Enter username : ")
password=getpass.getpass("Enter the password : ")

# Disalbe or ignore ssl verification warnings message
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


response = requests.get(jiraurl, verify=False, auth=(username, password))
jsondata= json.loads(response.text)

count = len(jsondata['issues'])

def datacollect():
    for i in range(count):
        data =  str(jsondata['issues'][i]['key']) + '\n' + str(jsondata['issues'][i]['fields']['description'])
        with open('/root/datafile.txt' , 'w+') as f:
            f.write(data)
        


def listoftlds():
    file = open('/root/datafile.txt').read().splitlines()
    for index, line in enumerate(file):
        if 'EMCSI' in line or 'Start time' in line or 'End time' in line or 'TLDs' in line:
            print(line)
        elif "---" in line :
            for data in file[index+1:index+1000]:
                if not '---' in data:
                    print(data)
    os.remove('/root/datafile.txt')

datacollect()
listoftlds()
