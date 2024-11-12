from collections import namedtuple

# Define the named tuple for structured access
SubarrayResult = namedtuple('SubarrayResult', ['max_sum_value', 'start', 'end'])

# algorithm returns the value of the maximal sum, the start and end index
# RUNTIME RUNTIME θ(nlog(n))
def max_sum(array, start, end):
    # for arrays of length 1, we return the single element list and its indices
    # RUNTIME 1
    if start == end:
        print('Subarray with index ' + str(start) + ' has sum_value ' + str(array[start]))
        return SubarrayResult(array[start], start, end)
    # for bigger arrays, we need to DIVIDE
    # RUNTIME 2T(n/2)
    else:
        mid = (start + end)//2
        maxSumLeft = max_sum(array, start, mid)
        maxSumRight = max_sum(array, mid + 1, end)

        # in the CONQUER step, we return the biggest sum between left, right and crossing sum
        # the crossing sum at least has the last element of the left array and the first element of
        # the right array. From these two elements, we need to iterate to the start of the left array
        # and the end of the right array and find the max value for them and sum  them up to find the
        # maximal crossing value 
        # RUNTIME n for traversing the whole array
        # -> TOTAL RUNTIME 2T(n/2) + n -> nlogn
       
        maxCrossingLeft = array[mid]
        maxLeftIndex = mid
        crossingValue = 0
        for left_index in range (mid, start, -1):
            crossingValue += array[left_index]
            if crossingValue>=maxCrossingLeft:
                maxCrossingLeft = crossingValue
                maxLeftIndex = left_index
                
        maxCrossingRight = array[mid +1]
        maxRightIndex = mid + 1
        crossingValue = 0
        for right_index in range(mid + 1, end):
            crossingValue += array[right_index]
            if(crossingValue>=maxCrossingRight):
                maxCrossingRight = crossingValue
                maxRightIndex = right_index
                
        maxCrossingSum = maxCrossingLeft + maxCrossingRight
        
        max_max_sum = max(maxSumLeft.max_sum_value, maxSumRight.max_sum_value, maxCrossingSum)

        match max_max_sum:
            case maxSumLeft.max_sum_value:
                print('Subarray with startindex ' + str(start) + ' and endindex ' + str(end) 
                + ' has max_sum_value ' + str(max_max_sum) + ' starting from ' + str(maxSumLeft.start) 
                + ' ending at ' + str(maxSumLeft.end))
                return maxSumLeft
            case maxSumRight.max_sum_value:
                print('Subarray with startindex ' + str(start) + ' and endindex ' + str(end) 
                + ' has max_sum_value ' + str(max_max_sum) + ' starting from ' + str(maxSumRight.start) 
                + ' ending at ' + str(maxSumRight.end))
                return maxSumRight
            case maxCrossingSum:
                print('Subarray with startindex ' + str(start) + ' and endindex ' + str(end) 
                + ' has max_sum_value ' + str(max_max_sum) + ' starting from ' + str(maxLeftIndex) 
                + ' ending at ' + str(maxRightIndex))
                return SubarrayResult(maxCrossingSum, maxLeftIndex, maxRightIndex)