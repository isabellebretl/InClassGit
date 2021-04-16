import random
import string

def password(a):
    pwd = string.ascii_letters
    print ( ''.join(random.choice(pwd) for i in range(a)) )