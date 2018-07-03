#!/usr/bin/python3
import sys
arr = sys.argv
arr.pop(0)
answers = []
for i in arr:
    if len(i) == 3:
        i = '0' + i
    tmp = '1'
    step = 0
    tmpArr = [i]
    while tmp not in tmpArr and step < 1050:
        if step == 0:
            tmp = i
        tmpArr.append(tmp)
        tmp = str(int(tmp)**2)
        if len(tmp)<8:
            for r in range(8-len(tmp)):
                tmp = '0' + tmp
        tmp = tmp[2:6]
        step += 1
    answers.append(step)
for a in answers:
    print(str(a),end=' ')
print()
    
