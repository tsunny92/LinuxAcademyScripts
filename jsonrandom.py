#!/usr/bin/env python

import json 
import random
import os

words = [words.strip() for words in open('/usr/share/dict/words').readlines()]

for identifier in range(10):
    amount = random.uniform(1.0,1000)
    content={'topic' : random.choice(words), 'Amount' : "%.2f" % amount }
    with open('/root/Rec/receipt-'+str(identifier)+'.json' , 'w') as f:
        json.dump(content, f)

