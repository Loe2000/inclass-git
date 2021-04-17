#Password generator - Write a program that takes in a number as input and returns a password of that length.
import random
import string

def password(a):
    for x in range(a):
        string.ascii_letters
        print(random.choice(string.ascii_letters), end="")


password(7)
