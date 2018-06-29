#!/usr/bin/python
import sys
print(sys.argv)
print(len(sys.argv))
answer = 0
for i in range(1,len(sys.argv)):
    answer += int(sys.argv[i])
print("The sum of all those numbers is " + str(answer))

