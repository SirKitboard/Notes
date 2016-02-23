file_name = input("Input old file name :")
content = []

f = open(file_name)
for line in f:
    line = line.replace('<span>', '')
    line = line.replace('</span>', '')
    # print(line)
    content.append(line)

splitFileName = file_name.split('.')
if(len(splitFileName) > 1):
    newFileName = splitFileName[0] + '_output.' + splitFileName[1]
else:
    newFileName = splitFileName[0] + '_output'

f = open(newFileName, "w")
for line in content:
    f.write(line)
