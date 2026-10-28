"""Create examples to compare two numbers
 using all relational operators
 (>, <, ==, !=, >=, <=). Write down the results
 for different types of numbers.
"""
def areEqual(x,y):
    return x==y
def areNotEqual(x,y):
    return x!=y
def isGreater(x,y):
    return x>y
def isLess(x,y):
    return x<y
def isGreaterandequal(x,y):
    return x>=y
def isLessandequal(x,y):
    return x<=y


x = 12
y = 12
z = 12.1
k = -12



print(f"are {x} and {y} equal? {areEqual(x,y)}")
print(f"are {x} and {z} not euqal? {areNotEqual(x,z)}")
print(f"is {x} less that {y} ? {isLess(x,y)}")
print(f"is {z} greater than {y} ? {isGreater(z,y)}")
print(f"is {k} less than or greater than {x} ? {isLessandequal(k,x)}")
print(f"is {x} less than or greater than { k} ? {isGreaterandequal(x,k)}")