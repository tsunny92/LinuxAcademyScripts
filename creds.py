#!/usr/bin/env python
import os

if  os.path.isfile('usercreds.txt'):
    with open("usercreds.txt") as f:
        for line in f:
            if 'username' in line:
                username=line.split('=')[1]
            else:
                password=line.split('=')[1]
        print(password)
else:
    with open("usercreds.txt",'w+') as f:
        username=raw_input("Enter usernme : ")
        password=raw_input("Enter password : ")
        f.write("username="+str(username)+"\npassword="+str(password))
        f.seek(0)
        print(f.read())

