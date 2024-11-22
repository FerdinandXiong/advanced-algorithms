import cmath

from sympy import symbols, exp, pi, I, simplify

# fft takes an input array of size n = 2^k (polynomial of degree n-1) 
# and calculates the DFT, which is the point-value representation of a polynom

def fft(a):
    print("compute the fft of ")
    print(a)
    # base case O(1):
    n = len(a)
    if n <= 1:
        return a
    # slicing (O(n)), divide: 2(O(n/2))
    else:
        even, odd = a[::2], a[1::2]
        d_even = fft(even)
        d_odd = fft(odd)
        print(" fft even is ")
        print(d_even)
        print(" fft odd is ")
        print(d_odd)
        omega_n = cmath.exp(2j*cmath.pi/n)
        omega = 1
        d_result = [0] * n
        # conquer/merge: merge even and odd results by 
        # summing even and omega(root of unity) * odd for result[0] to result[n/2 - 1]
        # subtracting odd*omega from even for n/2 to n
        for k in range (n//2):           
            print(" for n= " + str(n) + ", k = " + str(k) + " and omega = " + str(omega)) 
            d_result[k] = d_even[k] + omega * d_odd[k]
            d_result[k + n//2] = d_even[k] - omega * d_odd[k]                      
            print (d_result)
            omega *= omega_n
    return d_result


def fft2(a):
    """
    Compute the FFT of an input array `a` with size n=2^k.
    Uses exact symbolic computation for roots of unity.
    """
    print("Compute the FFT of:")
    print(a)

    n = len(a)
    if n <= 1:
        return a
    
    # Recursive divide step
    even, odd = a[::2], a[1::2]
    d_even = fft2(even)
    d_odd = fft2(odd)

    print("FFT of even indices:")
    print(d_even)
    print("FFT of odd indices:")
    print(d_odd)

    # Exact n-th root of unity: omega_n = exp(2 * pi * I / n)
    omega_n = simplify(exp(2 * pi * I / n))
    omega = 1  # Initialize omega^k for k = 0
    d_result = [0] * n

    # Merge step
    for k in range(n // 2):
        print(f"For n={n}, k={k}, omega={omega}:")
        d_result[k] = simplify(d_even[k] + omega * d_odd[k])
        d_result[k + n // 2] = simplify(d_even[k] - omega * d_odd[k])
        print("Result so far:", d_result)

        # Update omega for the next iteration
        omega = simplify(omega * omega_n)

    return d_result
