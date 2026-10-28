#Write a Python program that asks the user for two numbers and prints their sum.
def getNumber(pronpt):
    while True:
        try:
            return int(input(pronpt))
        except ValueError:
            print("please enter a number")

input1 = getNumber("Enter a number: ")
intput2 = getNumber("Enter another number: ")

print(f"the sum of the numbers is {input1+intput2}")