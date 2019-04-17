import re

n='wp-1'

if 'webhostbox.net' in n:
    print("You are looking for - "+n)
elif re.search(r'[a-z]+\-[0-9]+',n).group():
    print("You are looking for - "+n+".webhostbox.net")
else:
    print("You are looking for - "+n)
    

sent='Sunny is 10 and Paresh 9'

print(re.findall(r'[A-Z][a-z]*',sent))
