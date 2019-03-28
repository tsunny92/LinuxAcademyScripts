#!/usr/bin/env python3.6

import os
import json
import glob

try:
    os.mkdir('/root/Processed')

except Exception as err:
    print(err)


receipts = glob.glob('/root/Rec/receipt-[1-5]*.json')
subtotal = 0.0

for path  in receipts:
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['Amount'])
    print("Found : "+str(path.split('/')[-1]))
print(subtotal)
