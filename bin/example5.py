#!/bin/env python
# -*- coding utf-8 -*-
import re
lis = []
def matc(self):
	result=re.search(r"(\d{1,3}\.){3}\d{1,3}",self)
	return result.group(0)
with open('../data/e5') as tmp:
    lines = tmp.readlines()
    for l in lines:
        lis.append(matc(l))
lis=set(lis)
lis=list(lis)
print 'the ip is : %s\nthe count is %d '  %(lis,len(lis))
