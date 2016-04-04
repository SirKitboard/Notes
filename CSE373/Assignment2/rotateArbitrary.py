# A: input matrix, m: height of A, n: width of matrix
def rotateArbitrary(A, m, n):
    if(n<=1):
        return A
    else:
        rotatedQuad1 = rotateArbitrary(A[0:(m/2)-1][0:(n/2)-1], m/2, n/2)
        rotatedQuad2 = rotateArbitrary(A[0:(m/2)-1][n/2:n-1], m/2, n/2)
        rotatedQuad3 = rotateArbitrary(A[n/2:m-1][0:(n/2)-1], m/2, n/2)
        rotatedQuad4 = rotateArbitrary(A[n/2:m-1][n/2:n-1], m/2, n/2)

        B[0:(m/2)-1][0:(n/2)-1] = rectangularCopy(rotatedQuad4)
        B[0:(m/2)-1][n/2:n-1] = rectangularCopy(rotatedQuad1)
        B[n/2:m-1][0:(n/2)-1] = rectangularCopy(rotatedQuad2)
        B[n/2:m-1][n/2:n-1] = rectangularCopy(rotatedQuad3)

        return A
