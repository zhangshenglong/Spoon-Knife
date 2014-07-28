lis = []
with open('logt') as tmp:
    lines = tmp.readlines()
    for l in lines:
        lis.append(l.split(' - - ')[0])
a=set(lis)
print 'the ip is : %s,the count is %d '  %(a,len(a))
