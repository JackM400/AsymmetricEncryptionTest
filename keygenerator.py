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
    privatekey = keypairGenerator(p, q)
    print("Private key : ", privatekey)
    publickey = keypairGenerator(p, q)
    print("Public key : ", publickey)
    encrypt(privatekey, message)


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def gcdInverse(relCoPrime, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while relCoPrime > 0:
        temp1 = temp_phi // relCoPrime  # / for python 2 , // for 3
        temp2 = temp_phi - temp1 * relCoPrime
        temp_phi = relCoPrime
        relCoPrime = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


def keypairGenerator(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    relCoPrime = random.randrange(1, phi)

    # check relCoPrime  and phi are relatively prime
    g = gcd(relCoPrime, phi)
    while g != 1:
        # variable relcoprime is coprime to  e,phi
        relCoPrime = random.randrange(1, phi)
        g = gcd(relCoPrime, phi)

    # extend Euclids to get private key
    gi = gcdInverse(relCoPrime, phi)

    return ((relCoPrime, n), (gi, n))


def encrypt(privatekey, message):
    # Encrypt ==> (message^x) % PQ
    # break key up
    n = privatekey
    encryptedmessage = ((char ** privatekey) % n) for char in encryptedmessage


def decrypt(publickey, encryptedmessage):
    decryptedmessage = ""
    return decryptedmessage


initialise()
