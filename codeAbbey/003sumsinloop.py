#!/usr/bin/python3
import sys

data = sys.argv
if len(data)%2==0:
    print("data sets must be even, otherwise this won't work")
    exit(0)
else:
    answers = []
    for i in range(2,int(1+len(data)/2),2):
        for j in range(1,int(1+len(data)/2),2):
            answers.append(data[i]+data[j])
for a in answers:
    print(a,end=" ")
            
