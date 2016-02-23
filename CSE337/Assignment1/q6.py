file_name = input("Input old file name :")

old = {}
new = {}

oldOnly = {}
newOnly = {}
both = {}

f = open(file_name)
for line in f:
	values = line.split('\t')
	if(len(values) > 1):
		key = values[0].lower() + values[1].lower()
		old[key] = line
		oldOnly[key] = line

file_name = input("Input new file name :")
f = open(file_name)
for line in f:
	values = line.split('\t')
	if(len(values) > 1):
		key = values[0].lower() + values[1].lower()
		new[key] = line
		if key in old:
			both[key] = line
			del oldOnly[key]
		else:
			newOnly[key] = line

# print(newOnly, both, oldOnly)

f = open("old.txt", "w")
for key in oldOnly:
    f.write(oldOnly[key])

f = open("new.txt", "w")
for key in newOnly:
    f.write(newOnly[key])

f = open("both.txt", "w")
for key in both:
    f.write(both[key])
