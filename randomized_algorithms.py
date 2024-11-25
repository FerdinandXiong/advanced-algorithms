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

# simple implementation: returns True if it is possibly prime
# returns False if not prime
# RUNTIME O(1), good if you assume that the input is not Prime
def simple_primality_test(n): 
    if 2 ** (n-1) % n == 1:
        return True
    else:
        return False