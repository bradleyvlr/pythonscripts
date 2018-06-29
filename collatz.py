def isEven(num):
	if num % 2 == 0:
		return True
	else:
		return False

def collatz(number):
	
	if isEven(number):
		number = number // 2
	else:
		number = 3 * number + 1
	print(number)
	return(number)

def isInt():
	startInt = 0
	print("Give me an integer to collatz")
	try:
		startInt = int(input())
		return startInt
	except:
		print("WRONG!")
		return "WRONG"
		
def main():
	startBoi = 0
	while True:
		startBoi = isInt()
		if startBoi != "WRONG":
			break
	while startBoi != 1:
		startBoi = collatz(startBoi)
main()	
