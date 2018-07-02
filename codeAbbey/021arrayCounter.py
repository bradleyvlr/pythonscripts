#!/usr/bin/python3
import sys
arr = sys.argv
arr.pop(0)
rng = arr.pop(0)
cnt = []
for i in range(int(rng)):
    cnt.append(0)
for t in arr:
    cnt[int(t)-1] += 1
for a in cnt:
    print(a,end=" ")
print()
