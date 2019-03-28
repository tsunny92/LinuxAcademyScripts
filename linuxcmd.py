#!/usr/bin/env python3.6
import subprocess

listfiles = subprocess.run(['ls','-l','/root'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print("Files under /root \n"+listfiles.stdout.decode())
