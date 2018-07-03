#!/usr/bin/python3
dat = open("data")
lin = dat.readlines()
answers = []

for l in lin:
    l = l.replace("\n", "")
    l = l.split(" ")
    mdAns = []
    x = int(l[0])
    y = int(l[1])
    p = x * y
    while x != y:
        if x < y:
            y -= x
        else:
            x -= y
    mdAns.append(x)
    mdAns.append(int(p/x))
    answers.append(mdAns)

for a in answers:
    print('(' + str(a[0]) + ' ' + str(a[1]) + ') ',end="")
print()
