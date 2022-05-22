name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words=line.split()
    key=words[1]
    #print(key)
    counts[key]=counts.get(key,0) + 1

#for k,v in counts.items():
#    print(k,v)
bigword = None
bigcount = None
for key in counts:
    if bigcount is None:
        bigcount = counts[key]
    if bigcount < counts[key]:
        bigcount = counts[key]
        bigword = key
print(bigword, bigcount)
