fhand = open('mbox-short.txt')
dt = dict()
for lines in fhand:
    if not lines.startswith('From'):
        continue
    if lines.startswith('From:'):
        continue
    else:
        lines.rstrip()
        words = lines.split()
        time = words[5].split(':')
        hr = time[0]
        dt[hr] = dt.get(hr,0) + 1

fhr = sorted(dt.items())
for k,v in fhr:
    print(k,v)
