#!/usr/bin/python3
import sys
vals = sys.argv
vals.pop(0)
answers = []
for i in vals:
    arr = list(str(i))
    ans = 0
    for a in range(len(arr)):
        tmp = int(arr[a]) * (a + 1)
        ans += tmp
    answers.append(ans)

for a in answers:
    print(a,end=" ")
print("")
