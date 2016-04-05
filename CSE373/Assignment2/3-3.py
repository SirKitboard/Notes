# A: Array, W: Weights, k1, k2
def findK1thToK2thSmallestElementWithWeights(A, W, k1, k2):
    k1thSmallest = findRankKElt(k1)
    k2thSmallest = findRankKElt(k2)
    elements = []
    weights = []
    for index, element in A:
        if(element >= k1thSmallest && element =< k2thSmallest):
            arrayOfElements.append(element)
            weights.append(W[index])
    return (arrayOfElements, weights)

# A: Array, W: Weights, k1, k2
def sumOfWeightsOfElementsBetweenk1andk2(A, W, k1, k2):
    (elements, weights) = findK1thToK2thSmallestElementWithWeights(A, W, k1, k2)
    sum = 0
    for index, element in elements:
        sum += sum + weights[index]
    return sum

#A: Array, W: weights, n: length, leftWantedSum: sum of left side needed, rightWantedSum: sum of right side needed, totalSum: total sum needed
def findWeightSplitElement(A, W, n, leftWantedSum, rightWantedSum, totalSum):
    k = n/2
    elementX = findRankKElt(A, k)
    weightX = weight of elementX
    leftSum = sumOfWeightsOfElementsBetweenk1andk2(A, W, 0, k)
    rightSum = totalSum - leftSum - weightX
    if(leftSum < leftWantedSum and rightSum <= rightWantedSum):
        return k
    elif(leftSum < leftWantedSum and rightSum > rightWantedSum):
        leftWantedSum = leftWantedSum - leftSum
        (A, W) = findK1thToK2thSmallestElementWithWeights(A, W, n/2, n-1)
        length = len(A)
        totalSum = rightSum
        element = findWeightSplitElement(A, W, length, leftWantedSum, rightWantedSum, totalSum)
        return element
    else:
        rightWantedSum = rightWantedSum - rightSum
        (A, W) = findK1thToK2thSmallestElementWithWeights(A, W, 0, n/2 - 1)
        length = len(A)
        totalSum = leftSum
        element = findWeightSplitElement(A, W, length, leftWantedSum, rightWantedSum, totalSum)
        return element
