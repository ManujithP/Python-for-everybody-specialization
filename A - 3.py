hrs = input('Enter hours:')
h = float(hrs)
rate = input('Enter rate:')
r = float(rate)
def computepay(r,h):
    if h<=40:
        gpay = h*r
    if h>40:
        gpay = (r*40)+(1.5*r*(h-40))
    return gpay
x = computepay(r,h)
print("Pay",x)
