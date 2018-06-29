#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage: py.exe mcb.pyw save<keyword> - Saves clipboard to keyword.
#	mcp.pyw <keyword> - loads keyword to clipboard
#	mcb.pw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

def main():
	mcbShelf = shelve.open('mcb')
	if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
		mcbShelf[sys.argv[2]] = pyperclip.paste()
	elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
		if sys.argv[2].lower() == 'all':
			for key in list(mcbShelf.keys()):
				del mcbShelf[key]
		elif sys.argv[2] in mcbShelf:
			del mcbShelf[sys.argv[2]]
		else:
			shownotfound(sys.argv[2])
	elif len(sys.argv) == 2:
		if sys.argv[1].lower() == 'list':
			for i in mcbShelf.keys():
				print(i)
		elif sys.argv[1] in mcbShelf:
			pyperclip.copy (mcbShelf[sys.argv[1]])
		else:
			shownotfound(sys.argv[1])
	else: 
		print('Incorrect format: use mcb list to list keywords, mcb save <keyword> to save, mcb delete <keyword> to delest, mcb <keyword> to copy data to clipboard, or mcb delete all to empty data.')
	mcbShelf.close()

def shownotfound(txt):
	print('Error: %s is not found in keywords, try mcb.pw list for a list of keywords' % (txt))


main()

