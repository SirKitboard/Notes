def findLengthOfInfiniteArray(A):
    low = 0
    high = 1
    while(A[high]):
        low = high
        high *= 2
    while(A[low]):
        low+=1
    return low

def findElementInInfiniteArray(A, x):
    n = findLengthOfInfiniteArray(A)
    start = 0
    end = n-1
    while start < end:
        mid = (start + end)/2
        if A[mid] == x:
            return mid
        elif(x < A[mid]):
            end = mid-1
        else:
            start = mid+1

    return None
