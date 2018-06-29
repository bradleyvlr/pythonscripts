#! python3
# This takes a madlib file with ADJECTIVE, NOUN, ADVERB, and VERB typed in caps.
# It will prompt the user to replace the words
# it will then write the new madlib to a file, and print the madlib to console

#I need sys, to get filename. i need os to access the file. i need re to match words
import sys, os, re

# Main Function will open the madlib file, file will be specified with a command line argument.
def main():
	checker()
	
	madlibfile = open(sys.argv[1], 'r')
	madlibreader = madlibfile.read()
	newmadlib = matcher(madlibreader)
	print(newmadlib)	

	madlibfile.close()
	
# Function to match regex, call a function to prompt user, and replace text and then return new text
def matcher(text):
	pos = re.compile(r'(ADJECTIVE|ADVERB|VERB|NOUN)')
	poslist = pos.findall(text)
	lst = text.split()
	for j in range(len(poslist)):
		poslist[j] = getter(poslist[j])
	poscount = 0
	for i in range(len(lst)):
		if pos.search(lst[i]) != None:
			lst[i] = pos.sub(poslist[poscount], lst[i])
			poscount +=1
	newtext = ' '.join(lst)
	return newtext	

#Function to Prompt user for part of speech. IN=Regex Match , RETURN=User Input
def getter(part):
	if part == 'ADJECTIVE' or part == 'ADVERB':
		print('\nEnter an %s:' % (part.lower()))
	else:
		print('\nEnter a %s:' % (part.lower()))
	replacement = input()
	return replacement


#simple error message with hint on how to use the program
def errormsg():
	print('Syntax is bad>> use --madlibber.py <filename>\n\nAlso make sure that the madlib file exists and is in the correct format; NOUN must be in all caps')
	sys.exit(2) 

# Checker makes sure that the file exists, I may later add a quick regex check to make sure the format is good.
def checker():
	if len(sys.argv) != 2:
		errormsg()
	elif not os.path.isfile(sys.argv[1]):
		errormsg()
	else:
		print("BOOTING UP*********\n\n\n") 



main()
