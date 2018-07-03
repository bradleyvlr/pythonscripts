#!/usr/bin/python
import sys
onearr = sys.argv
onearr.pop(0)
arr = []
for o in onearr:
    arr.append(int(o))
orgArr = []
for a in arr:
    orgArr.append(a)
arr.sort()
print(arr)
print(orgArr)
for a in arr:
    print(str(orgArr.index(a)+1))
print('')
