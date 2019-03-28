#!/usr/bin/env python3.6

msg = input("Enter the message to echo : ")
count = int(input("Enter the number of times to display message ").strip())

def displaymsg(msg , count):
    if count > 0:
        for i in range(count):
            print(msg)
    else:
        print(msg)
displaymsg(msg , count)
