fname = input('Enter the name of the file')
fhand = open(fname)
count = 0
ad = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        pos1 = line.find(' ')
        bit = line[pos1+1:]
        no = float(bit)
        co = float(count)
        ad = ad + no
avg = ad/co
print ('Average spam confidence:',avg)
