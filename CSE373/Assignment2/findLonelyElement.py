#A: Array, n: length
def findLonelyElement(A, n):
    if(n==0):
        return None;
    if(n==1):
        return A[0]

    mid = n/2
    if(mid%2 == 0):
        if(A[mid] == A[mid+1]):
            A = A[mid+2:n]
            n = len(A)
            return findLonelyElement(A, n)
        else:
            A = A[0:mid]
            n = len(A)
            return findLonelyElement(A, n)
    else:
        if(A[mid] == A[mid-1]):
            A = A[mid+1:n]
            n = len(A)
            return findLonelyElement(A, n)
        else:
            A = A[0:mid-1]
            n = len(A)
            return findLonelyElement(A, n)
