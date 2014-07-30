#!/bin/env python
# -*- coding utf-8 -*-
import os
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8') 
PATH='../data/e6'
#PATH='e6engl'
def file_exists(filename):
    try:
        open(filename)
        return True
    except:
        print "The similar file is missing or is not readable"
        return exit(0)
def similar(filename,lis):
    tmp=open(filename)
    lines = tmp.readlines()                           
    row_number =len(lines)                                     
    coun = [ 0 for i in range(row_number)]                 
    li=re.split(r'\s+',lis)     
    lis_len=len(li)    
    #print lines 
    number=-1                          
    for I in lines: 
        number=number+1                                       
        Ic=re.split(r'\s+',I)
        I_long=len(Ic)
        for j in range(lis_len):                            
            for k in range(I_long):
                if cmp(li[j].lower(),Ic[k].lower())==0:
                    coun[number]=coun[number]+1                      
    print 'The similar sentence is:'
    for m in range(row_number):                              
        if coun[m]==max(coun):
            print lines[m].encode('gbk')
file_exists(PATH)
lis=raw_input("Please enter the sentence : ")
similar(PATH,lis)
