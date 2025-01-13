# key gen takes 2 large primes p and q and returns private key d
# by selecting as the public key a natural number e that is relatively prime to (p-1), (q-1), 
# we generally select e as 65537
# since e needs to be greater then 1 and smaller then phi_n
def genKey(p, q, e):
    n = p*q
    phi_n = (p-1) * (q-1)
    if phi_n < e:
        print("prime numbers to small")
    # d = e^-1 => d*e = 1(mod(p-1)(q-1))
    # d is calculated by the extended euclidian algorithm    
    _ , d = extendedEuclid(phi_n, e)
    
    return d

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
# returns x and y
def extendedEuclid(a, b):
    if b == 0:
        return 1, 0
    x1, y1 = extendedEuclid(b, a % b)
    x = y1
    y = x1 - (a//b) * y1
    return x, y
    
    
def encrypt(key, message):
    message * key