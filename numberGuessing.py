import random
def inputGetter():
	print("Take a guess\n>>",end=" ")
	guess = input()
	try:
		guess = int(guess)
	except:
		guess = "WORDS"
	return guess

def guessChecker(toCheck, answer):
	if toCheck == "WORDS":
		print("Bruh, that's not a number...")
	elif toCheck == answer:
		print("Congrats, you have won")
		print("The answer was" , answer)
		return False
	elif toCheck > answer:
		print("Your guess is too high")
		return True
	elif toCheck < answer:
		print("Your guess is too low")
		return True

def main():
	print("I'm Thinking of a Number between 1 and 20")
	num = random.randrange(1,20)
	isOver = True
	turn = 0
	while isOver:
		turn += 1
		theGuess = inputGetter()
		isOver = guessChecker(theGuess,num)
	print("This took you" , turn , "turns")
	print("Goodbye")
main()
