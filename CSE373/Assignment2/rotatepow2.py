# A: input matrix, n: width of matrix, power of 2
def rotateSquarePow2(A, n):
    if(n<=1):
        return A
    else:
        rotatedQuad1 = rotateSquarePow2(A[0:(n/2)-1][0:(n/2)-1], n/2)
        rotatedQuad2 = rotateSquarePow2(A[0:(n/2)-1][n/2:n-1], n/2)
        rotatedQuad3 = rotateSquarePow2(A[n/2:n-1][0:(n/2)-1], n/2)
        rotatedQuad4 = rotateSquarePow2(A[n/2:n-1][n/2:n-1], n/2)

        A[0:(n/2)-1][0:(n/2)-1] = rectangularCopy(rotatedQuad4)
        A[0:(n/2)-1][n/2:n-1] = rectangularCopy(rotatedQuad1)
        A[n/2:n-1][0:(n/2)-1] = rectangularCopy(rotatedQuad2)
        A[n/2:n-1][n/2:n-1] = rectangularCopy(rotatedQuad3)

        return A
