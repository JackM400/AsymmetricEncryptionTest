import math
import random


# check if number provided is prime
def primeCheck(number):
    if number == 2:
        return True
    if number % 2 == 0 or number <= 1:
        return False

    sqr = int(math.sqrt(number)) + 1

    for divisor in range(3, sqr, 2):
        if number % divisor == 0:
            return False
    return True


def initialise():
    message = input("Input message to encrypt\n")
    areEqual = True
    while areEqual:
        pCheck = False
        while not pCheck:
            p = int(input("Input a prime, P\n"))
            if primeCheck(p):
                pCheck = True
            qCheck = False
            while not qCheck:
                q = int(input("Input a prime, Q\n"))
                if primeCheck(q):
                    qCheck = True
                if p == q:
                    print("P Q cannot be same prime\n")
                else:
                    areEqual = False


def gcd(x, y):
    return


def gcdInverse(relCoPrime, phi):
    return


def keypairGenerator(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    relCoPrime = random.randrange(1, phi)

    # check relCoPrime  and phi are relatively prime
    g = gcd(relCoPrime, phi)
    while g != 1:
        relCoPrime = random.randrange(1, phi)
        g = gcd(relCoPrime, phi)


initialise()
