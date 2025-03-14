import cmath
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

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


import sympy as sp

def fft2(a, inverse=False, depth=0):
    """
    Compute the FFT of an input array `a` with size n=2^k.
    Uses exact symbolic computation for roots of unity.
    """
    indent = "    " * depth  # Indentation based on depth
    print(f"{indent}Compute the{' inverse' if inverse else ''} FFT of:")
    print(f"{indent}{a}")

    n = len(a)
    if n <= 1:
        print(f"{indent}Base case reached (n <= 1), returning: {a}")
        return a
    
    # Recursive divide step
    even, odd = a[::2], a[1::2]
    print(f"{indent}Splitting into even and odd indices:")
    print(f"{indent}Even: {even}")
    print(f"{indent}Odd: {odd}")

    print(f"{indent}Recursively computing{' inverse' if inverse else ''} FFT of even indices:")
    d_even = fft2(even, inverse=inverse, depth=depth + 1)
    print(f"{indent}Recursively computing{' inverse' if inverse else ''} FFT of odd indices:")
    d_odd = fft2(odd, inverse=inverse, depth=depth + 1)

    print(f"{indent}{'inverse ' if inverse else ''}FFT of even indices:")
    print(f"{indent}{d_even}")
    print(f"{indent}{'inverse ' if inverse else ''}FFT of odd indices:")
    print(f"{indent}{d_odd}")

    # Exact n-th root of unity: omega_n = exp(2 * pi * I / n)
    omega_n = sp.simplify(sp.exp(-2 * sp.pi * sp.I / n) if inverse else (sp.exp(2 * sp.pi * sp.I / n)))
    omega = 1  # Initialize omega^k for k = 0
    d_result = [0] * n

    # Merge step
    for k in range(n // 2):
        print(f"{indent}For n={n}, k={k}, omega={omega}:, omega_n={omega_n}")       
        print(f"{indent}    result[{k}] = d_even[{k}] + {omega} * d_odd[{k}]")
        d_result[k] = sp.simplify(d_even[k] + omega * d_odd[k])
        print(f"{indent}    result[{k + n//2}] = d_even[{k}] - {omega} * d_odd[{k}]")
        d_result[k + n // 2] = sp.simplify(d_even[k] - omega * d_odd[k])
        print(f"{indent}    Result so far:")
        print(f"{indent}    {d_result}")

        # Update omega for the next iteration
        print(f"{indent}    omega = {omega} * {omega_n}")
        omega = sp.simplify(omega * omega_n)
        print(f"{indent}    = {omega}")

    print(f"{indent}Returning result for depth {depth}: {d_result}")
    return d_result

def pointwise_multiplication(a, b):
    a_array = sp.Matrix(a)
    b_array = sp.Matrix(b)
    result = a_array.multiply_elementwise(b_array)
    return [sp.simplify(x) for x in result]  # Ensuring simplified symbolic form

def normalize(arr):
    return [x / len(arr) for x in arr]

def multiply_polynomials(pol1, pol2):
    value_1 = fft2(pol1)
    value_2 = fft2(pol2)
    value_product = pointwise_multiplication(value_1, value_2)
    coefficient_product = fft2(value_product, inverse=True)
    print("coefficient_product after fft inverse:")
    print(coefficient_product)
    coefficient_product = normalize(coefficient_product)
    print("coefficient_product after normalization:")
    print(coefficient_product)
    print("finished")
    plot_polynomial(coefficient_product, filename=f"output/fft")
    
    return coefficient_product
    
# calculates all additions a + b of 2 sets A and B in nlogn time
# idea: construct 2 polynoms polA = x^a1, x^a2, ... and polB = x^b1, x^b2
# with an, bn ∈ [n - 1]
# then, do fft multiplication with them, the result contains all
# sums of a and b
def setAddition(setA, setB, n):
    polA = [0] * n
    polB = [0] * n
    
    for i in setA:
        polA[i] = 1
        
    for i in setB:
        polB[i] = 1
    
    mult_result = multiply_polynomials(polA, polB)
    result_set = set()
    for i in range (n):
        print(f"i = {i}, multresult[i] = {mult_result[i]}")
        if(mult_result[i] > 0):
            result_set.add(i)
    return result_set

def plot_polynomial(coeffs, filename):
    """
    Plot the polynomial given its coefficients and save it as a PNG.
    
    Args:
    - coeffs: List of polynomial coefficients (e.g., [3, 6] for 6x + 3)
    - depth: Recursion depth (used for labeling)
    - filename: Name of the file to save the plot
    """
    x = sp.symbols('x')
    
    # Construct polynomial
    polynomial = sum(c * x**i for i, c in enumerate(coeffs))
    func = sp.lambdify(x, polynomial, modules=['numpy'])

    # Generate x values and compute y values
    x_vals = np.linspace(-2, 2, 400)
    y_vals = func(x_vals)

    # Plot
    plt.figure(figsize=(6, 4))
    plt.plot(x_vals, y_vals, label=f"{polynomial}", color='b')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linestyle='--', linewidth=0.5)
    plt.legend()
    
    # Save the figure
    plt.savefig(filename, dpi=300)
    plt.close()

