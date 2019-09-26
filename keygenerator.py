import math
import random


# check if number provided is prime
def prime_check(number):
    if number == 2:
        return True
    if number % 2 == 0 or number <= 1:
        return False

    sqr = int(math.sqrt(number)) + 1

    for divisor in range(3, sqr, 2):
        if number % divisor == 0:
            return False
    return True


def generate_prime(index):
    number = 3
    prime_index = 2
    if index == 1:
        return 2
    while prime_index < index:
        number = number + 2
        if prime_check(number):
            prime_index = prime_index + 1
    return number


def initialise():
    # message = input("Input message to encrypt\n")
    message = "My name isn’t slick, it’s Zoidberg. JOHN F***ING ZOIDBERG!"
    are_equal = True
    while are_equal:
        p = generate_prime(random.randint(4500, 15000))
        q = generate_prime(random.randint(4500, 15000))
        print("p :", p)
        print("q :", q)
        if p == q:
            are_equal = True
        else:
            are_equal = False
    private_key = key_pair_generator(p, q)
    print("Private key : ", private_key)
    public_key = key_pair_generator(p, q)
    print("Public key : ", public_key)
    encrypted_message = encrypt(private_key, message)
    print("Message to Transmit :".join(map(lambda x: str(x), encrypted_message)))
    print("message decrypted : ")
    decrypted_message = decrypt(public_key, encrypted_message)
    print(decrypted_message)


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def gcd_inverse(relative_co_prime, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while relative_co_prime > 0:
        temp1 = temp_phi // relative_co_prime  # / for python 2 , // for 3
        temp2 = temp_phi - temp1 * relative_co_prime
        temp_phi = relative_co_prime
        relative_co_prime = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        assert isinstance(phi, object)
        return d + phi


def key_pair_generator(p, q):
    n = p * q
    phi = (p - 1) * (q - 1) + 1
    rel_co_prime = random.randrange(1, phi)

    # check rel_co_prime  and phi are relatively prime
    g = gcd(rel_co_prime, phi)
    while g != 1:
        # variable relcoprime is coprime to  e,phi
        rel_co_prime = random.randrange(1, phi)
        g = gcd(rel_co_prime, phi)

    # extend Euclids to get private key
    gi = gcd_inverse(rel_co_prime, phi)

    return (rel_co_prime, n), (gi, n)


def encrypt(private_key, message):
    # Encrypt ==> (message^x) % PQ
    # break up private_key tuple
    # private_key = (relCoPrime, n), (gi, n)
    # 2 degree tuple (relCoPrime, n) + (gi, n)
    lhs1, rhs1 = private_key
    lhs2, rhs2 = lhs1
    print(lhs1)
    print(rhs1)
    # of ((a,b) ,(c,d))
    # what are x , y?

    encrypted_message = [(ord(char) ** lhs2) % lhs1 for char in message]
    print('Encrypted Message: ', encrypted_message)
    return encrypted_message


def decrypt(public_key, encrypted_message):
    # Decryption Process : (message^y) % PQ
    # break up public_key tuple
    # public_key = (relCoPrime, n), (gi, n)
    lhs1, rhs1 = public_key
    lhs2, rhs2 = lhs1

    decrypted_message = [chr((char ** lhs2) % lhs1) for char in encrypted_message]
    return decrypted_message


initialise()
