lst = list()
fhand = open('romeo.txt.txt')
for line in fhand:
    bit = line.rstrip()
    bit = line.split()
    for i in bit:
        if i in lst:
            continue
        else:
            lst.append(i)
            lst.sort()
print (lst)
