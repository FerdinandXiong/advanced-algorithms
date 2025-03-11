import random
import math

# quicksort returns sorted array by comparing elements to a pivot element
# EXPECTED RUNTIME: O(n) + 1/n ∑{k = 0}^{n} (O(k-1) + O(n-k))
def quicksort(arr, start, end):
    if start < end:
        # compute pivot element
        pivot_index = random.randint(start, end)
        pivot = arr[pivot_index]
        
        # sort the array into the form [elements < pivot][pivot][elements > pivot]
        # first, swap the pivot element with the last element
        arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
        # next, iterate through the items of the array (n comparisons)
        i = start
        for j in range (start, end):
            # put swap elements < pivot to the start of the arr (increasing index)
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        # swap the pivot to the correct position
        arr[end], arr[i] = arr[i], arr[end]
        
        # recursively quicksort the rest of the elements
        # given a splitter element k, left side O(k-1), right side O(n-k)
        # since there are n possible positions for k, for the expected runtime,
        # each possible outcome needs to be multiplied by 1/n:
        # => EXPECTED RUNTIME for LEFT and RIGHT:
        # 1/n sum 1,k(O(k-1) + O(n-k)
        quicksort(arr, start, i-1) 
        quicksort(arr, i + 1, end)

# naive implementation: RUNTIME sqrt(n)
def naive_is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range (2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# For the fast exponentiation algorithm, our runtime calculation are based on 
# n as the exponent and a as base
def fast_exponent(base, exponent):
    if exponent == 1:
        # RUNTIME 1
        return base
    elif exponent % 2 == 0:
        # RUNTIME T(n/2) + log(a^n/2) * log(a^n/2) => log(n) * log(a^n/2)^2
        half_exponent = fast_exponent(base, exponent//2)
        return half_exponent * half_exponent
    else:
        # RUNTIME T(n/2) + log(a^n/2) * log(a^n/2) => log(n) * log(a^n/2)^2 * log(a)
        half_minus_1_exponent = fast_exponent(base, (exponent - 1)//2)
        return half_minus_1_exponent * half_minus_1_exponent * base

# equivalent to library implementation of pow()
def fast_exponent_mod(base, exponent, mod):
    if exponent == 1:
        # RUNTIME 1
        return base
    elif exponent % 2 == 0:
        # RUNTIME T(n/2) + log(a^n/2) * log(a^n/2) => log(n) * log(a^n/2)^2
        half_exponent = fast_exponent_mod(base, exponent//2, mod)
        return (half_exponent * half_exponent) % mod
    else:
        # RUNTIME T(n/2) + log(a^n/2) * log(a^n/2) => log(n) * log(a^n/2)^2 * log(a)
        half_minus_1_exponent = fast_exponent_mod(base, (exponent - 1)//2, mod)
        return (half_minus_1_exponent * half_minus_1_exponent * base) % mod

# simple implementation: can detect numbers that are not prime, 
# false is the only certain answer, since true could have false positives
# returns True : possibly prime, no conclusion can be made
# returns False => not prime
# RUNTIME O(1), good if you assume that the input is not Prime
def simple_probably_prime_test(n): 
    b = pow(2, n - 1, n)
    if b == 1:
        return True
    else:
        return False
    
# in order to decrease the possibility for false positives, 
# we can use the miller rabin test
# we use fermat's little theorem to test further numbers of the group
# in principle: a^(p-1) mod p = 1, we tested 2 for a, but we can take random numbers
def randomized_primality_test(n):
    a = random.randint(2, n-1)
    b =  pow(a, n - 1, n)
    print('n : ' + str(n) + '; a: ' + str(a) + '; b: ' + str(b))
    if b == 1:
        return True
    else: 
        return False

# tests the randomized primality test for all powers of 2
# starting with d = n - 1
def miller_rabin_test(n):
    print(f"trying Miller Rabin test for n = {n}")
    if n == 2:
        return True

    d = n - 1
    r = 0
    while d % 2 == 0:
        r += 1
        d //= 2
    
    print (f"pow x r = {r} times")    
    
    for _ in range (10): # randomly selected number
        a = random.randint(2, n-1)
        print(f"calculate one iteration of power with a = {a}:")
        x = pow(a, d, n)       
        print(f"x = {x}, after calculating x = a^d mod n = {a} ^ {d} mod {n}")
        if x == 1 or x == n - 1:
            continue
        
        for _ in range (r - 1):
            # checking for charimichael nubers: by squaring x
            print("in loop")
            x = pow(x, 2, n)
            print(f"x = {x}, after calculating x = a^d mod n = {a} ^ {d} mod {n}, continue with r = {r}")
            if x == n - 1:
                print("fails in loop because x == -1")
                break
            
        else:
            # fermats theorem violated => not prime
            return False            
    
    return True   