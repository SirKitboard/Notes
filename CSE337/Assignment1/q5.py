stringArray = []

stringArray.append(input("Input the first string :"))
stringArray.append(input("Input the second string :"))
stringArray.append(input("Input the third string :"))
stringArray.append(input("Input the fourth string :"))

sortedArray = sorted(stringArray, key=str.lower)

print("\nSorted Array:")
for element in sortedArray:
    print(element)
