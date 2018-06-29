#Reads a sentence, and tells you the longest word and its length.
def main():
    sentence = input("Input sentence for analysis\n>> ")
    longestWord = ""
    longestLength = 0
    numberWords = 0
    sentArray = sentence.split()
    for word in sentArray:
        if len(word)>longestLength:
            numberWords = 1
            longestLength = len(word)
            longestWord = word
        elif len(word)==longestLength:
            numberWords += 1
            longestWord += ", and "
            longestWord += word
    if numberWords == 0:
        print("\n\nYour sentence is no good. Try typing a real one!")
    elif numberWords == 1:
        print("\n\nThe longest word is",longestWord,". And it has ",longestLength,"letters")
    else:
        print("\n\nThe record length is ",longestLength,". And the words are ",longestWord,".")
main()
