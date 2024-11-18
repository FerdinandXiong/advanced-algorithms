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

# Define the named tuple for structured access
SubarrayResult2 = namedtuple('SubarrayResult', ['max_sum_value', 'start', 'end', 'I_value', 'I_end', 
                                                'J_value', 'J_start', 'whole_sum'])

# algorithm returns the value of the maximal sum, the start, end index of the sum, 
# I, J, their values and the whole array value
# RUNTIME RUNTIME θ(n)
def max_sum2(array, start, end):
    # basecase:
    if start == end:
        single_value = array[start]
        return SubarrayResult2(single_value, start, end, single_value, start, single_value, end, single_value)
    # divide in left and right subproblem: 
    # RUNTIME 2T(n/2)
    else:
        mid = (start + end)//2
        left_result = max_sum2(array, start, mid)
        right_result = max_sum2(array, mid + 1, end)
        
        # conquer:
        # our I can either end 
        # at its old end (left_result.I_end), 
            # in which case I_value is the old one (left_result.I_value)
        # or at the end of J (right_result.end), 
            # in which case I_value = left_result.whole_sum + right_result.I_value
        # So we need to compare 
        # (left_result.I_value) with left_result.whole_sum + right_result.I_value
        # and take the bigger value as our new I      
        I_value = left_result.whole_sum + right_result.I_value
        I_end = right_result.I_end
        if left_result.I_value > I_value:
            I_value = left_result.I_value
            I_end = left_result.I_end                        
        
        # our J can either start in I (left_result.start)
            # in which case J_value = left_result.J_value + right_result.whole_sum
        # or at its old start (right_result.J_start)
            # in which case I_value is the old one (right_result.I_value)
        J_value = right_result.whole_sum + left_result.J_value
        J_start = left_result.J_start
        if right_result.J_value > J_value:
            J_value = right_result.J_value
            J_start = right_result.J_start
            
        # whole_sum is addition between left and right
        whole_sum = left_result.whole_sum + right_result.whole_sum
        
        # if both cross -> this is new maxsum, if none cross, take bigger old max_sum
        # if one crosses and the other does not, take the bigger between crossed and
        # not crossed value
        
        max_sum_value = left_result.J_value + right_result.I_value
        if left_result.max_sum_value > max_sum_value:
            return SubarrayResult2(left_result.max_sum_value, left_result.start, left_result.end, I_value, I_end, J_value, J_start, whole_sum)
        elif right_result.max_sum_value > max_sum_value:
            return SubarrayResult2(right_result.max_sum_value, right_result.start, right_result.end, I_value, I_end, J_value, J_start, whole_sum)
        else:
            return SubarrayResult2(max_sum_value, left_result.J_start, right_result.I_end, I_value, I_end, J_value, J_start, whole_sum)