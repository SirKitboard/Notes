# A: array, n: length
def findPossibleFrequentElement(A, n):
    possibleIndex = 0, count = 1
    for index, element in A:
        if(A[possibleIndex] == element):
            count+=1
        else:
            count-=1
        if(count == 0):
            possibleIndex = index
            count = 1

    return a[possibleIndex]

# A: array, n: length, frq: element to be tested
def isFrequentElement(A, n, frq):
    count = 0
    for element in A:
        if element == frq:
            count+=1

    if count > n/2:
        return True
    else:
        return False

# A: array, n: length
def findFrequentElement(A, n):
    possibleFrequent = findPossibleFrequentElement(A, n)
    if(isFrequentElement(A, n, possibleFrequent)):
        return possibleFrequent
    else:
        return None
