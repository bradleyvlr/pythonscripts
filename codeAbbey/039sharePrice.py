#!/usr/bin/python3
import math
dat = open("data")
lin = dat.readlines()
answers = []
for l in lin:
    l = l.replace("\n", "")
    l = l.split(" ")
    sm = 0
    for i in range(1,len(l)):
        l[i] = int(l[i])
        sm += l[i]
    mn = sm/(len(l)-1)
    sd = 0
    for i in range(1,len(l)):
        sd += ((l[i]-mn)**2)/(len(l)-1)
    sd = math.sqrt(sd)
    print(sd)
    print("comm:  " + str((mn/100)))
    if mn/100 < sd/4:
        answers.append(l[0])
for a in answers:
    print(a,end=' ')
print()


