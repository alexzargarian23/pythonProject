"""Create and Compare Numbers of Different Types
Compare an integer and a float
Compare a decimal and a float
Compare two fractions
"""

# an integer
i = 12
# a float
f = 12.21
# a fraction
from fractions import Fraction
fraction = Fraction(4,2)
fraction2 = Fraction(1,3)
# a decimal
from decimal import Decimal
d = Decimal ("12.21")

def compNumbers(x,y):
    if x == y:
        return f"{x}  is equal to {y} "
    elif x<y:
        return f"{x} is less than {y}"
    else:
        return f"{x} is greater than  {y}"



print(compNumbers(i,f))
print(compNumbers(d,f))
print(compNumbers(fraction,fraction2))


