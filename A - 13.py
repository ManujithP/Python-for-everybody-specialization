import re
fhand = open('words.txt')
lst = list()
for line in fhand:
    line.rstrip()
    no = re.findall('[0-9]+',line)
    for i in range(0,len(no)):
        no[i] = int(no[i])
        lst.append(no[i])
print(sum(lst),'length:',len(lst))
