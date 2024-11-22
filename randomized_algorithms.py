import random

# quicksort returns sorted array by comparing elements to a pivot element
# EXPECTED RUNTIME: n + 
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
        quicksort(arr, start, i-1) 
        quicksort(arr, i + 1, end)
    