#The code will check for any non alphanumeric characters and remove them
#Also, this will be case insensitive.
import re
def main():
    str = input("Which line would you like to check?\n>>")
    str = str.lower()
    arr = list(str)
    alphanum = re.compile('[a-z0-9]')
    reducedArr = [x for x in arr if alphanum.match(x)]
    str = ''.join(reducedArr)
    arr = reducedArr[::-1]
    flipped = ''.join(arr)
    if(str == flipped):
        print("Sure thing,", str, "is a palindrome")
    else:
        print("Sorry,", str, "is not a palindrome")
main()
