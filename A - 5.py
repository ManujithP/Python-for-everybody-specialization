while True:
    try:
        i = input('Enter integer:')
        if i == 'done':
            break
        t = int(i)
    except:
        print('Invalid input')
s = None
l = None
for t in [7,2,10,4]:
    if t > l:
        l = t
print('Maximum is',l)
for t in [7,2,10,4]:
    if s is None:
        s = i
    if t < s:
        s = t
print('Minimum is',s)
