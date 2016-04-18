def isStringDecomposition(a, b, c, i, j):
    if(len(a) == 0 && len(b) == 0):
        T[0,0] = False
        return false
    if(a[0] == c[0]):
        if(T[i-1, j] != None):
            return T[i-1, j]
        else:
            success = isStringDecomposition(a[1:i], b, c[1:i+j], i-1, j)
            T[i-1, j] = success
            return success
    elif(b[0] == c[0]):
        if(T[i, j-1] != None):
            return T[i, j-1]
        else:
            success = isStringDecomposition(a, b[1:j], c[1:i+j], i, j-1)
            T[i, j-1] = success
            return success
    T[i, j] = False
    return False
