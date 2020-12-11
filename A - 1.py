hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h <= 40:
    gpay = r*h
elif h > 40:
    gpay = (r*40) + (1.5*r*(h-40))
print (gpay)
