#!/usr/bin/python3
import sys
arr = sys.argv
arr.pop(0)
marx = int(arr.pop(0))
mirn = marx
for a in arr:
    a = int(a)
    if a > marx:
        marx = a
    elif a < mirn:
        mirn = a
print(str(marx) + " " + str(mirn))
