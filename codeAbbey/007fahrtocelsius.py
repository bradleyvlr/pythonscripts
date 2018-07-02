#!/usr/bin/python3
import sys
arr = sys.argv
answers = []
for i in range(1,len(arr)):
    ans = int(round((int(arr[i]) - 32) * (5 / 9)))
    answers.append(ans)
for a in answers:
    print(a,end=" ")
print("")
