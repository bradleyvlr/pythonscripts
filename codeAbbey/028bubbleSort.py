#!/usr/bin/python3
import sys
arr = sys.argv
arr.pop(0)
result = 0
swap = 0
swpArr = []
while True:
    swpArr.append(swap)
    for i in range(len(arr)-1):
        tmp = 0
        if int(arr[i]) > int(arr[i+1]):
            tmp = arr.pop(i)
            arr.insert(i+1,tmp)
            swap += 1
    print(swap)
    print(swpArr)
    result +=1
    if swpArr[-1] == swap:
        break
print(str(result) + " " + str(swap))
            
