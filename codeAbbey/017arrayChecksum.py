#!/usr/bin/python3
import sys
arr = sys.argv
arr.pop(0)
result=0
for i in arr:
    result = ((result + int(i))*113)%10000007
print(result)
