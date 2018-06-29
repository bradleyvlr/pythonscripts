#The goal is to take a table and print it in a mildly readable way
#I will base the column width on the longest entry in a column.
#The lab says to right just, but I will center.

tableData = [['xerxes','qexycatl','Tyrannasaurus Rex','Okapi','Chupacabra'],['Lenin','Luxemburg','Trotsky','Marx','Engels'],['Mao','DuXiu','Zhou Enlai','Biao','Jeunesse'],['Reed','Haywood','Venzetti','Keller','Grant']]

def getColumnWidth(tab):
	maxList = []
	for x in tab:
		maxWidth = 0
		for y in x:
			if len(y) > maxWidth:
				maxWidth = len(y)
		maxList.append(maxWidth)
	return maxList
def tablePrinter(table):
	maxList = getColumnWidth(table)
	for x in range(len(table[0])):
		for y in range(len(table)):
			print(table[y][x].center(maxList[y]),end=" ")
		print('')
	
			
def main():
	tablePrinter(tableData)
main()
