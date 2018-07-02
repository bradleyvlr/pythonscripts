#!/usr/bin/python3
import sys

data = sys.argv
if len(data)%2==0:
    print("data sets must be even, otherwise this won't work")
    exit(0)
else:
    answers = []
    for i in range(2,len(data),2):
            answers.append(int(data[i])+int(data[i-1]))
for a in answers:
    print(a,end=" ")
print('')
            
