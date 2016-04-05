# A: Array, n: Length of array
def checkIfElementOccursMoreThanHalfOfLenght(A, n):
    mid1 = findRankKElt(n/2)
    mid2 = findRankKElt(n/2 + 1)
    count1 = 0
    count2 = 0
    for element in A:
        if(mid1 == element)
            count1++
        if(mid2 == element)
            count2++

    if(count1 > n/2 || count2 > n/2):
        return True
