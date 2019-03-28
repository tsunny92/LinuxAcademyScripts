#!/usr/bin/env pythob

import argparse

parser = argparse.ArgumentParser(description='Search for words including partial word')
parser.add_argument('snippet', help='Partial or complete word in words dictionary')

args = parser.parse_args()

snippet = args.snippet.lower()

with open('/usr/share/dict/words') as f:
    words = f.readlines()

matches = [word.strip() for word in words if snippet in word.lower()]

# Replaced below code with above one 
'''
for word in words:
    if snippet in word.lower():
        matches.append(word.strip())
'''
print("Total Matches found are : "+str(len(matches))+"\n---------------------------------------")

for match in matches:
    print(match)

