"""Write a program that takes a string and
 extracts the first and last character using subscripts (indexing)."""
import string
from itertools import count


def extractLetters(string):
    first = string[0]
    last = string[-1]
    result = first + last
    return result

r = extractLetters("hello")
print(f"First character:  {r[0]} Last character: {r[1]} ")


"""Write a program that slices the first 3 
characters and the last 2 characters from a string."""

def extractFromLastandFirst(string):
    first = string[0:2]
    last = string[-1:-3:-1]
    return first , last


a , b = extractFromLastandFirst("Python")
print(f" {a} and {b}")

"""Write a program that takes two strings as 
input and concatenates them with a space in between."""

def addSpace(string1, string2):
    return string1 + " " + string2

print(addSpace("Good", "Morning"))


"""Write a program that takes a string and
 converts it to both uppercase and lowercase."""

def UpperandLower(sting1):
    return sting1.upper() , sting1.lower()

up , down = UpperandLower("Hello World")
print(f"Uppercase: {up} Lowercase: {down}")


"""Write a program that checks whether a 
string starts with the letter "A" and ends with the letter "Z"."""


def meetsCondition(string1):
    upper_str = string1.upper()

    return upper_str.startswith("A"), upper_str.endswith("Z")


first, last = meetsCondition("aaaZ")
print(f"Starts with A: {first} ends with Z : {last}")


"""Write a program that counts how many times the letter "a" appears in a given string.
# Input: "banana"
# Output: "a" appears 3 times
"""

def countLetter(string1):
    count = 0
    for letter in string1:
        if letter == "a":
            count += 1
    return count


print (countLetter("banana"))


"""Write a program that takes a sentence and 
splits it into words, then joins the words back into a 
sentence with hyphens (-) between them."""


def spilitSentance(string1):
    words  = string1.split()
    result = "-".join(words)
    return result

print(spilitSentance("I love Python"))

"""Write a program that takes a user’s name as 
input and creates a greeting message like "Hello, [Name]!"."""

def printHello(string1):
    result = "Hello, " + string1 + "!"
    return result

print(printHello("Alex"))