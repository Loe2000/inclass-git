import random
import string

def password():
    a = int(input('Input the length of your password (integer): '))
    for x in range(a):
        string.ascii_letters
        print(random.choice(string.ascii_letters), end="")


password()