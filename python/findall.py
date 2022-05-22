import re
fname=input('Enter File name:')
if len(fname)<1:
    name = "regex_sum_1550736.txt"
handle = open(fname)
count=0
for line in handle:
    line = line.rstrip()
    numstring = re.findall('[0-9]+', line)
    if len(numstring)<1:
        continue
    for i in range(0,len(numstring)):
        numstring[i]= int(numstring[i])
        count= count + numstring[i]
    #f=type(numstring)
print(count)
