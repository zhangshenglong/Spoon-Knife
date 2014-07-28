import os
import re
lis=raw_input("Please enter the sentence : ")
print lis
with open('e6engl') as tmp:
    lines = tmp.readlines()                           
    row_number =len(lines)                                     
    coun = [ 0 for i in range(row_number)]                 
    li=re.split(r'\s+',lis)     
    lis_len=len(li)    
    print lines 
    number=-1                          
    for I in lines: 
        number=number+1                                       
        Ic=re.split(r'\s+',I)
        I_long=len(Ic)
        for j in range(lis_len):                            
            for k in range(I_long):
                if cmp(li[j].lower(),Ic[k].lower())==0:
                    coun[number]=coun[number]+1                      
    for m in range(row_number):                              
        if coun[m]==max(coun):
            print 'The similar sentence is: %s ' %lines[m]

