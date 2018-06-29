myList = ['apples', 42, 'johnny', 'blasphemy', 'bananas', 'tofu', 'cats']
for i in myList:
	if myList.index(i) == len(myList) - 1:
		print(', and ' + str(i))
	elif myList.index(i) == 0:
		print(str(i), end="")
	else:
		print(', ' + str(i), end="")

