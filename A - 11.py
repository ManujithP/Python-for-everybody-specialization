dt = dict()
fhand = open('mbox-short.txt.txt')
for line in fhand:
    if not line.startswith('From'):
        continue
    if line.startswith('From:'):
        continue
    else:
        line.rstrip()
        words = line.split()
        bit = words[1]
        dt[bit] = dt.get(bit,0) + 1
        
count = None
lt = dt.items()
for n,c in lt:
    if count is None or c > count:
        count = c
        fname = n

print(fname,count)
