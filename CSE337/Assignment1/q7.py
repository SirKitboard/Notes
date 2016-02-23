# file_name = input("Input old file name :")
import operator

file_name = input("Input html file name :")
webpage = ""

f = open(file_name)
for line in f:
	webpage+=line

startingIndex = -1

str_dataURL = "data-imageurl=\""
str_dataNotes = "data-notes=\""
str_closingTag = "\">"

notes = []

# print(webpage.index(str_dataURL))
startingIndex = webpage.find(str_dataURL, startingIndex+1)
while startingIndex > 0:
	# print(startingIndex)
	imageURL = webpage[startingIndex + len(str_dataURL):webpage.find(str_closingTag, startingIndex+1)]
	notesStartingIndex = webpage.find(str_dataNotes, startingIndex+1)
	numNotes = webpage[notesStartingIndex + len(str_dataNotes):webpage.find(str_closingTag, notesStartingIndex + 1)]
	notes.append({
		'imageURL': imageURL,
		'numNotes': int(numNotes)
	})
	# print(numNotes)
	# print(imageURL)
	startingIndex = webpage.find(str_dataURL, startingIndex+1)

notes = sorted(notes, key=operator.itemgetter('numNotes'), reverse=True)

# print(notes)

f = open("output.html", "w")
f.write("""
<html>
<head>
<title>Most Notes</title>
</head>
<body>
<ol>
""")

for i in range(0,5):
	f.write('<li><a href="'+notes[i]["imageURL"]+'">'+str(notes[i]["numNotes"])+'</a></li>\n')

f.write("</ol></body></html>")
