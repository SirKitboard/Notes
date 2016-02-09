#pylint: disable=W0312
#pylint: disable=C

#Aditya Balwani, SBUID : 109353920

import fileinput

class ExcelData(object):
	# Initialize data with column names
	def __init__(self, colNames): 
		self.colNames = colNames
		self.rows = []
		self.colsDeterminable = True

	# Add a row of data
	def insertRow(self, row):
		self.rows.append(row)
		if self.colsDeterminable:
			if len(self.rows) > 1:
				if len(row) != len(self.colNames):
					self.colsDeterminable = False

	# Print number of rows and columns
	def printSummary(self):
		print("Number of rows : ", (1+len(self.rows)))
		if self.colsDeterminable:
			print("Number of columns : ", len(self.colNames))
		else:
			print("Cannot determine number of columbns")

	# Return boolean based on whether data is valid or not
	def isValid(self):
		return self.colsDeterminable

	# Print a column
	def printCol(self,i):
		columnDic = {}
		for row in self.rows:
			columnDic[row[i]] = (columnDic[row[i]] if row[i] in columnDic.keys() else 0) + 1
		for key,value in sorted(columnDic.items()):
			print(value,"\t",key.strip())


	# Print all columns. Called the printCol method
	def printAll(self):
		for i, col in enumerate(self.colNames):
			print("\n-------------")
			print("Column ",i,": ",col.strip())
			print("-------------")
			self.printCol(i)


def main(): 
	data = None
	for i,row in enumerate(fileinput.input()):
		#print(i,row)
		row = row.split("\t")
		if i == 0:
			data = ExcelData(row)
		else:
			data.insertRow(row)

	data.printSummary()
	if data.isValid():
		data.printAll()

main()
