stringArray = []

stringArray.append(input("Input the first string :"))
stringArray.append(input("Input the second string :"))
stringArray.append(input("Input the third string :"))
stringArray.append(input("Input the fourth string :"))

def sorter(str1, str2):
    str1 = lower(str1)
    str2 = lower(str2)

    if(str1>str2):
        return 1
    elif (str1 == str2):
        return 0
    else:
        return -1

sortedArray = sorted(stringArray, key=str.lower)

print(sortedArray)
