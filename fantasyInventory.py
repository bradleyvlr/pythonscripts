inventory = {'rope': 1,'sword': 2, 'potion': 5, 'shield': 1, 'hookshot': 1,'rupees': 254}
dragonLoot = ['rupees', 'potion', 'bottle', 'rope', 'bomb', 'bomb']

def displayInventory(invent):
	print('INVENTORY:')
	for i in invent.keys():
		print(invent[i], end=" ")
		print(i)

def addToInventory(loot, invent):
	for x in loot:
		if x in invent.keys():
			invent[x] += 1
		else:
			invent.setdefault(x, 1)
	
def main():
	print("\n\n*******************************\n\nThe Dragon Dropped Some Loot\n\nDo you want to pick it up?\nType 'y' for yes or anything for no")
	addq = input()
	if addq == 'y':
		addToInventory(dragonLoot,inventory)
	print("\n\n********************************\n\n")
	print("DO YOU WANT TO DISPLAY THE INVENTORY?\nPRESS 'y' FOR YES OR ANYTHING ELSE FOR NO")
	answer = input()
	if answer == 'y':
		displayInventory(inventory)
	print("\n\n\n\n")
main()
