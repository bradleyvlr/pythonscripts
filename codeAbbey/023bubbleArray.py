#!/usr/bin/python3
import sys
arr = sys.argv
arr.pop(0)
result = 0
swap = 0
for i in range(len(arr)-1):
    tmp = 0
    if int(arr[i]) > int(arr[i+1]):
        tmp = arr[i]
        arr.pop(i)
        arr.insert(i+1,tmp)
        swap += 1
for i in arr:
    result = ((result + int(i))*113)%10000007
print(str(swap) + " " + str(result))
