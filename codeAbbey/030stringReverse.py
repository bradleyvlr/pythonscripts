#!/usr/bin/python3
original = input("Give me a string to reverse:  ")
arr = []
for c in original:
    arr.append(c)
new = []
for i in range(len(arr)-1,-1,-1):
    new.append(arr[i])
print(''.join(new))

