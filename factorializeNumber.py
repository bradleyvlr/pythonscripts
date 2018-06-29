def main():
   num = int(input("Which number would you like to factorialize >> "))
   for i in range(1,num): 
       num = num * i
   print("your answer is: ", num)
   return num
main()
