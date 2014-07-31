#!/bin/env python
# -*- coding utf-8 -*-
import re
import sys
import os
ipLists = []

def ipMatch(line):
	ipObject=re.search(r"(\d{1,3}\.){3}\d{1,3}",line)
	return ipObject.group(0)

with open('../data/e5') as file:
    lines = file.readlines()
    for oneLine in lines:
        ipLists.append(ipMatch(oneLine))

ipLists = set(ipLists)
ipLists = list(ipLists)
print 'the ip is : %s\nthe count is %d '  %(ipLists,len(ipLists))
