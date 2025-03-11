# key gen takes 2 large primes p and q and returns private/secret key SA consisting of d and n
# by selecting as the public key a natural number e that is relatively prime to (p-1), (q-1), 
# we generally select e as 65537
# since e needs to be greater then 1 and smaller then phi_n
def gen_private_Key(p, q, e):
    n = p*q
    phi_n = (p-1) * (q-1)
    if phi_n < e:
        print("prime numbers to small")
    # d = e^-1 => d*e = 1(mod(p-1)(q-1))
    # d is calculated by the extended euclidian algorithm    
    _ , d = extendedEuclid(phi_n, e)
    if d < 0:
        d = d + phi_n    
    return d, n

# calculates pulic key PA consisting of e and n
def gen_public_key(p, q, e):
    n = p*q
    return e, n

# gcd (greatest common dividor) of 2 numbers definition: 
# bigest number which divides the 2 numbers
# euclid: not requred for rsa, but the basis for extended euclid
# theorem: gcd(a, b) = gcd(b, mod a)
def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)

# gcd(a,b)=a⋅x+b⋅y
# input: 2 integers a and b with b >= 0
# Output: returns x and y, such that x*a + yb = gcd(a, b)
def extendedEuclid(a, b):
    if b == 0:
        return 1, 0
    x1, y1 = extendedEuclid(b, a % b)
    x = y1
    y = x1 - (a//b) * y1
    return x, y

# intuition: encryption and decription relies on the principle PA(SA(message)) = message
# because M^ed mod n = M
# since M^ed = M^de, digital signature can be created by encrypting the message with d,
# which can be decrypted using e
    
# ciphertext c = m^e mod n
def encrypt(message, public_key):
    e, n = public_key
    return pow(message, e, n)

# original message m = c^e mod n
# decrypt is baasically the same method as signing
def decrypt(cyphertest, private_key):
    d, n = private_key
    return pow(cyphertest, d, n)

def text_to_int(text):
    return int.from_bytes(text.encode('utf-8'), byteorder='big')

def int_to_text(number):
    return number.to_bytes((number.bit_length() + 7) // 8, byteorder='big').decode('utf-8')