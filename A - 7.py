fname = input('Enter file name:')
fhand = open(fname)
inp = fhand.read()
ip = inp.rstrip()
print(ip.upper())
