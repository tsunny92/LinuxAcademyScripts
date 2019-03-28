#!/usr/bin/env python
import  sys
import argparse
#print("All argument is", sys.argv[1:])


# Creating object using ArgumentParser class
parser = argparse.ArgumentParser(description='Read a file in reverse')

# Adding argument help options 
parser.add_argument('filename', help='File to read')
parser.add_argument('--limit', '-l', type=int, help='specify the no of lines to read')
parser.add_argument('--version', '-v', action='version' , version='%(prog)s 1.0')

# Calls the function to get info from above arguments added
args = parser.parse_args()
# print(args)

# Reversing the contents of the file

try:
    f = open(args.filename)
    limit = args.limit

except Exception as err:
    print("Error: "+str(err))
    sys.exit(2)

else:
    with f:
        lines = f.readlines()
    
        if args.limit:
            lines = lines[:limit]

        for line in lines:
            print("Before\n"+line.strip()[::1])
            print("After\n"+line.strip()[::-1])

    
'''
with open(args.filename) as f:
    lines = f.readlines()       # takes as a list for each line
    #lines.reverse()             # Reverse the list index
    
    if args.limit:
        lines = lines[:args.limit]

    for line in lines:
        print("Before\n"+line.strip()[::1])
        print("After\n"+line.strip()[::-1])

'''
