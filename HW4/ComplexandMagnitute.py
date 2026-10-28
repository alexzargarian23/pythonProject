"""  Create Complex Numbers and Calculate Magnitude
Create two fractions and perform addition, subtraction, multiplication, and division manually. Afterward, check the results using Python.
Create a decimal number and experiment with adding or subtracting very small decimal values.

"""
complex1 = 4 -3j +3j
complex2 = 4 -3j +3j
complex3 = 0.1 +0.12j
def calculateMagintute(x):
    return abs(x)


"""print (calculateMagintute(complex1))
print (calculateMagintute(complex2))
print (calculateMagintute(complex3))"""

from fractions import Fraction
f1 = Fraction(1,32)
f2 = Fraction (1,3)

""""print (f1 + f2)
print (f1 - f2)
print (f1 * f2)
print (f1 / f2)"""

from decimal import Decimal

d1 = Decimal('1.1')
d2 = Decimal('0.000000000000000000000000000000000000000000000000000000000009090909000099001')

print(d1-d2)

print(d1+d2)

print(d1*d2)
