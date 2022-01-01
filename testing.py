#!/usr/bin/python

import os

output = os.system("ls -lh | grep -E -i -v \"total\" | "
                   "awk '{print $5,$NF}' | sort -k1 -h")
print(f"{output}")

