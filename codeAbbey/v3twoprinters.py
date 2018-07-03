#!/usr/bin/python3
import math
dat = open("data")
lin = dat.readlines()
answers = []
for l in lin:
    l = l.replace("\n", "")
    l = l.split(" ")
    pages = int(l[2])
    histhigh = pages
    histlow = 0
    pone = max(int(l[0]),int(l[1]))
    ptwo = min(int(l[0]),int(l[1]))
    pagOne = math.ceil(pages/2)
    pagTwo = pages - pagOne
    timeOne = pagOne * pone
    timeTwo = pagTwo * ptwo
    minTime = 100
    while histhigh - histlow > 1:
        if timeTwo > timeOne:
            histlow = pagOne
            pagOne = math.ceil((histhigh + pagOne)/2)
        elif timeTwo < timeOne:
            histhigh = pagOne
            pagOne = math.ceil((histlow + pagOne)/2)
        else:
            minTime = timeOne
            histlow = pagOne
            histhigh = histlow
            break
        pagTwo = pages - pagOne
        timeOne = pagOne * pone
        timeTwo = pagTwo * ptwo
    if minTime == 100:
        minTime = min(max((histhigh*pone),((pages-histhigh)*ptwo)),max((histlow*pone),((pages-histlow)*ptwo)))
    answers.append(minTime)
for a in answers:
    print(a,end=" ")
print()
    
