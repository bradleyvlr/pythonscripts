#!/usr/bin/python3
dat = open("data")
lin = dat.readlines()
answers = []
for l in lin:
    l = l.replace("\n", "")
    l = l.split(" ")
    pages = int(l[2])
    pone = max(int(l[0]),int(l[1]))
    ptwo = min(int(l[0]),int(l[1]))
    timeinit = pages*pone
    timeTwo = 0
    pagOne = pages
    pagTwo = 0
    while timeinit > timeTwo + pone:
        pagOne -= 1
        timeinit -= pone
        pagTwo += 1
        timeTwo += ptwo
    answers.append(timeinit)
for a in answers:
    print(a,end=" ")
print()
    
