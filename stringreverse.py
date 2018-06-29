#!/usr/bin/python3
def main():
    str = input("Give me a string yo...")
    words = list(str)
    words.reverse()
    newstring = ''.join(words)
    print(newstring) 
    return newstring
main()
