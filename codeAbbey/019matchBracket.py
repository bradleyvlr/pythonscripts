#!/usr/bin/python3
dat = open("data")
lin = dat.readlines()
answers = []
oBrack = ['<','[','(','{']
cBrack = ['>',']',')','}']
for l in lin:
    l = l.replace("\n", "")
    l = list(l)
    brackArr = []
    ans = 1
    for i in l:
        if i in oBrack:
            brackArr.append(i)
        elif i in cBrack:
            if cBrack.index(i) == oBrack.index(brackArr[-1]):
                brackArr.pop(-1)
            else:
                ans = 0
                break
        else:
            print(i)
    print(brackArr)
    answers.append(ans)
for a in answers:
    print(a,end=" ")
print('')
            
    
    
