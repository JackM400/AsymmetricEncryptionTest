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


def generatePrime(index):
    number = 3
    primeindex = 2
    if index == 1:
        return 2
    while primeindex < index:
        number = number + 2
        if primeCheck(number):
            primeindex = primeindex + 1
    return number


def initialise():
    # message = input("Input message to encrypt\n")
    message = "My name isn’t slick, it’s Zoidberg. JOHN F***ING ZOIDBERG!"
    areEqual = True
    while areEqual:
        p = generatePrime(random.randint(4500, 15000))
        q = generatePrime(random.randint(4500, 15000))
        print("p :", p)
        print("q :", q)
        if p == q:
            areEqual = True
        else:
            areEqual = False
    privatekey = keypairGenerator(p, q)
    print("Private key : ", privatekey)
    publickey = keypairGenerator(p, q)
    print("Public key : ", publickey)
    encryptedmessage = encrypt(privatekey, message)
    print("Message to Transmit :".join(map(lambda x: str(x), encryptedmessage)))
    print("message decrypted : ")
    decryptedmessage = decrypt(publickey, encryptedmessage)
    print(decryptedmessage)


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

    return (relCoPrime, n), (gi, n)


def encrypt(privatekey, message):
    # Encrypt ==> (message^x) % PQ
    # break up privatekey tuple
    # privatekey = (relCoPrime, n), (gi, n)
    # 2 degree tuple (relCoPrime, n) + (gi, n)
    lhs1, rhs1 = privatekey
    lhs2, rhs2 = lhs1
    print(lhs1)
    print(rhs1)
    # of ((a,b) ,(c,d))
    # what are x , y?

    encryptedmessage = [(ord(char) ** lhs1) % rhs1 for char in message]
    return encryptedmessage


def decrypt(publickey, encryptedmessage):
    # Decryption Process : (message^y) % PQ
    # break up publickey tuple
    # publickey = (relCoPrime, n), (gi, n)
    lhs, rhs = publickey

    decryptedmessage = [chr((char ** lhs) % rhs) for char in encryptedmessage]
    return decryptedmessage


initialise()
