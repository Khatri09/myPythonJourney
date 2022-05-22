# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
z = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    x = line.find(' ')
    new = line[x+1:]
    z = z + float(new)
    #print(new)
    count = count + 1

print("Average spam confidence:", z/count)
