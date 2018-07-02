#!/usr/bin/python3
dat=open("data")
arr = dat.readlines()
answers = []
for d in arr:
    d = d.replace("\n","")
    d = d.split(" ")
    ans = 0
    for x in range(int(d[2])):
        a = int(d[0])
        b = int(d[1])*(x)
        ans += a + b
    answers.append(ans)
for a in answers:
    print(a,end=' ')
print('')
