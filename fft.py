import cmath

# fft takes an input array of size n = 2^k (polynomial of degree n-1) 
# and calculates the DFT, which is the point-value representation of a polynom

def fft(a):
    # base case O(1):
    n = len(a)
    if n <= 1:
        return a
    # slicing (O(n)), divide: 2(O(n/2))
    else:
        even, odd = a[::2], a[1::2]
        d_even = fft(even)
        d_odd = fft(odd)
        omega_n = cmath.exp(2j*cmath.pi/n)
        omega = 1
        d_result = [0] * n
        # conquer/merge: merge even and odd results by 
        for k in range (n//2):
            d_result[k] = d_even[k] + omega * d_odd[k]
            d_result[k + n//2] = d_even[k] - omega * d_odd[k]
            omega *= omega_n
    return d_result