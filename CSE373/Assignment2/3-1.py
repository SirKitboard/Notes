def findK1thToK2thSmallestElement(A, k1, k2):
    k1thSmallest = findRankKElt(k1)
    k2thSmallest = findRankKElt(k2)
    arrayOfElements = []
    for element in A:
        if(element >= k1thSmallest && element =< k2thSmallest):
            arrayOfElements.append(element)
    return arrayOfElements
