#A: array, n: length
def findFrequentElement(A, n):
    if n == 1:
        return A[0]
    leftSplit = A[0:n/2]
    rightSplit = A[n/2: n-1]
    leftFrequent = findFrequentElement(leftSplit, len(leftSplit))
    rightFrequent = findFrequentElement(rightSplit, len(rightSplit))

    if(leftFrequent is None and rightFrequent is None):
        return None
    if(leftFrequent == rightFrequent):
        return leftFrequent
    if(leftFrequent is not None and rightFrequent is not None):
        leftFrequentCount = 0
        for element in A:
            if leftFrequent == element:
                leftFrequentCount+=1

        rightFrequentCount = 0
        for element in A:
            if rightFrequent == element:
                rightFrequentCount+=1

        if(leftFrequentCount > rightFrequentCount and leftFrequentCount > n/2):
            return leftFrequent
        elif(rightFrequentCount > leftFrequentCount and rightFrequentCount > n/2):
            return rightFrequent
        else:
            return None
    if(rightFrequent is not None):
        rightFrequentCount = 0
        for element in A:
            if rightFrequent == element:
                rightFrequentCount+=1
        if(rightFrequentCount > n/2):
            return rightFrequent
        else:
            return None
    if(leftFrequent is not None):
        leftFrequentCount = 0
        for element in A:
            if leftFrequent == element:
                leftFrequentCount+=1
        if(leftFrequentCount > n/2):
            return leftFrequent
        else:
            return None
