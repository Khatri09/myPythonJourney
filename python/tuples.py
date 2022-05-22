name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
hcount=dict()
hlst=list()
for line in handle:
    line = line.rstrip()
    words=line.split()
    if len(words) > 2 and words[0] == 'From':
            hr = words[5].split(':')
            hcount[hr[0]] = hcount.get(hr[0], 0) + 1
            #print(hcount)
for k,v in hcount.items():
    hlst.append((k,v))
    #print(k,v)
hlst.sort()
#print(hlst)
for k,v in hlst:
    print(k,v)
