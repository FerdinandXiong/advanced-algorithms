from collections import namedtuple

# algorithm returns the value of the maximal sum, the start and end index
def max_sum_array(array, start, end):
    # for arrays of length 1, we return the single element list and its indices
    if start == end:
        return array[start]
    # for bigger arrays, we need to DIVIDE    
    else:
        mid = (start + end)//2
        maxSumLeft = max_sum_array(array, start, mid)
        maxSumRight = max_sum_array(array, mid + 1, end)

        # in the CONQUER step, we return the biggest sum between left, right and crossing sum
        # the crossing sum at least has the last element of the left array and the first element of
        # the right array. From these two elements, we need to iterate to the start of the left array
        # and the end of the right array and find the max value for them and sum  them up to find the
        # maximal crossing value
        
        maxCrossingLeft = array[mid]
        crossingValue = 0
        for i in range(mid, start, -1):
            crossingValue += array[i]
            if(crossingValue>=maxCrossingLeft):
                maxCrossingLeft = crossingValue
                
        maxCrossingRight = array[mid +1]
        crossingValue = 0
        for i in range(mid +1, end):
            crossingValue += array[i]
            if(crossingValue>=maxCrossingRight):
                maxCrossingRight = crossingValue
                
        maxCrossingSum = maxCrossingLeft + maxCrossingRight
        
        return max(maxSumLeft, maxSumRight, maxCrossingSum)
