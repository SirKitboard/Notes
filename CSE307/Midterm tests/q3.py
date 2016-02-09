def toDigits(a):
    digList = []
    while a>0:
        digList.insert(0,a%10)
        a = int(a/10)
    return digList

print (toDigits(123))
