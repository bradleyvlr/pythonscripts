#With a bunch of text copied to the keyboard, this uses regexes to find e-mail addresses and phone numbers
#It is mostly for practice with using regexes in Python.

import pyperclip, re

def main():
	mytext = pyperclip.paste()
	emails = getemails(mytext)
	phones = getphones(mytext)
	print("\n\nHere Are The Phone Numbers:\n")
	for i in phones:
		print(i)
	print("\n\nHere Are The E-Mails:\n")
	for i in emails:
		print(i)

def getphones(text):
	phoneReg = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?(\d{3})(\s|-|\.)(\d{4})(\s*(ext|x|ext.)\s*(\d{2,5}))?)', re.VERBOSE)
	return phoneReg.findall(text)	
def getemails(text):
	emailReg = re.compile(r'[a-zA-Z]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4})', re.VERBOSE)
	return emailReg.findall(text)

main()
