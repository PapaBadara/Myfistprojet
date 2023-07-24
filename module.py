from math import *

def diffAvant1(f,x,h):
    return (f(x+h)-f(x))/h

print(" -"*15)
print("{: ^8}|{: ^20}".format("h","cos(0)"))
print(" -" * 15)
for n in range(1,13):
    x=0
    f=sin
    h=10**-n
    print('{: 7.1e} | {: .15f}'.format(h, diffAvant1(f,x,h)))
