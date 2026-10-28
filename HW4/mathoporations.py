"""Create two integer variables and perform addition, subtraction, multiplication, and division.
Repeat the same for two floating-point numbers.
Repeat the same for complex numbers.
"""
x = 10
y = 12
xFloat = 10.12
yFloat = 12.21

def add(x,y):
    return x+y
def subraction(x,y):
    return x-y
def multiply(x,y):
    return x*y
def devision(x,y):
    return (x/y)

print(add(x,y))
print(subraction(x,y))
print(multiply(x,y))
print(devision(x,y))
## for flaot
print("the flaot oporations")
print(add(xFloat,yFloat))
print(subraction(xFloat,yFloat))
print(multiply(xFloat,yFloat))
print(devision(xFloat,yFloat))
