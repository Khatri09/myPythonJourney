fopen = open('input.txt')

largest = None
PID = None
for i in fopen:
    i = i.rstrip()
    newlist = i.split()
    CPU = int(newlist[1])
    if CPU not in range(0,101):
        print("out of range")
        exit()

    if largest is None:
        largest = CPU
        PID = newlist[0]
    elif CPU > largest:
        largest = CPU
        PID = newlist[0]
print(PID)
