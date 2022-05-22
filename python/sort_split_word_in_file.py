fname = open('romeo.txt')
some=list()
for i in fname:
    i = i.rstrip()
    i_list=i.split()
    for j in i_list:
        if j not in some:
            some.append(j)

some.sort()
print(some)  
