fh = open('mbox-short.txt')
count = 0
for line in fh:
    line=line.rstrip()
    f=line.split()
    if len(f)<3:
        continue
    if f[0] != 'From':
        continue
    print(f[1])
    count=count+1


print("There were", count, "lines in the file with From as the first word")
