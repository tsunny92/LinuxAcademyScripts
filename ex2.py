#!/usr/bin/env python

import math
import os

pivalue = math.pi
digits = int(os.getenv('DIGITS') or 2)
print("%.*f" % (digits, pivalue))
