#!/usr/bin/python3
import math
dat = open("data")
lin = dat.readlines()
answers = []
for l in lin:
    l = l.replace("\n", "")
    l = l.split(" ")
    start = int(l[0])
    req = int(l[1])
    intrst = int(l[2])
    year = 0
    while start < req:
        
        start = (math.floor(100*(start + (start*(intrst/100)))))/100
        print(start)
        year += 1
    print("Start: " + str(start) + "\treq: " + str(req))
    print(year)
    answers.append(year)
for a in answers:
    print(str(a),end=' ')
print()
