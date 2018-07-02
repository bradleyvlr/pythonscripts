#!/usr/bin/python3
dat = open("data")
lin = dat.readlines()
answers = []
for l in lin:
    l = l.replace("\n", "")
    l = l.split(" ")
    ab = []
    run = (int(l[2])-int(l[0]))
    rise = (int(l[3])-int(l[1]))
    slope = int(rise/run)
    ab.append(slope)
    b = int(l[1]) - int(l[0])*slope
    ab.append(b)
    answers.append(ab)
for a in answers:
    print("("+str(a[0])+" "+str(a[1])+")",end=" ")
print("")
