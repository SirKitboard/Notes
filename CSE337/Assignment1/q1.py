file_name = input("Input old file name :")
content = []

f = open(file_name)
for line in f:
    # Remove opening tags
    line = line.replace('<span>', '')

    # Removing closing tags
    line = line.replace('</span>', '')
    content.append(line)

splitFileName = file_name.split('.')
if(len(splitFileName) > 1):
    newFileName = splitFileName[0] + '_output.' + splitFileName[1]
else:
    newFileName = splitFileName[0] + '_output'

# Write new file
f = open(newFileName, "w")
for line in content:
    f.write(line)
