#!/usr/bin/python3
dat = open("data")
lin = dat.readlines()
answers = []
for l in lin:
    l = l.replace("\n", "")
    l = l.split(" ")
    pages = int(l[2])
    time = 0
    pone = max(int(l[0]),int(l[1]))
    ptwo = min(int(l[0]),int(l[1]))
    time = round(pages/((1/pone)+(1/ptwo)))
    time = time - (time % pone) + pone
    answers.append(time)
for a in answers:
    print(a,end=" ")
print()
    
