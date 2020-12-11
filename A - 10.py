fhand = open('mbox-short.txt.txt')
count = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    if line.startswith('From:'):
        continue
    bit = line.split()
    count = count + 1
    print(bit[1])
print('There were',count,'lines in the file with From as the first word')
