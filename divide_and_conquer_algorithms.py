from collections import namedtuple

# Define the named tuple for structured access
SubarrayResult = namedtuple('SubarrayResult', ['max_sum', 'start', 'end'])

# algorithm returns the value of the maximal sum, the start and end index
def max_sum_array(array, start, end):
    # for arrays of length 1, we return the single element list and its indices
    if start == end:
        return SubarrayResult(array[start], start, end)  
    # for bigger arrays, we need to divide    
    else:
        mid = (start + end)//2
        maxSumLeft = max_sum_array(array, start, mid)
        maxSumRight = max_sum_array(array, mid + 1, end)

        # in the conquer step, we return the bigger sum if it is bigger than the arraysum 
        # from the start indice of the left array to the end indice to the right array. 
        # Instead summing from the left to the right end of the array,
        # we should calculate the value with the formular:
        # maxSumLeft.max_sum + sum(maxSumLeft.end + 1 to maxSumRight.start) + maxSumRight.max_sum
        # Then we take the max between these 3 elements
        valueBetweenLeftAndRight = 0
        for i in range(maxSumLeft.end + 1, maxSumRight.start):
            valueBetweenLeftAndRight += array[i]
        
        if(maxSumLeft.max_sum + valueBetweenLeftAndRight <= 0):
            if (maxSumLeft.max_sum < maxSumRight.max_sum):
                return maxSumRight
            else:
                return maxSumLeft
        elif(maxSumRight.max_sum + valueBetweenLeftAndRight <= 0):
            return maxSumLeft
        else:
            return SubarrayResult(maxSumLeft.max_sum + valueBetweenLeftAndRight + maxSumRight.max_sum,
                                  maxSumLeft.start, maxSumRight.end)
