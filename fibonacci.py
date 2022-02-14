#A number is fibonacci if (5*n*n+4) or (5*n*n-4) is a perfect square
import math #Import math module.
def perfectsquare(x)
    c=int(math.sqrt(x))
    return c*c==x
n=int(input("please enter number: "))
a=5*(n*n)+4
b=5*(n*n)-4
if perfectsquare(a) or perfectsquare(b):
    print(n,"is fibonacci number")
else:
    print(n,"is not fibonacci number")
