#!/usr/bin/python3
dat = open("data")
lin = dat.readlines()
answers = []
for l in lin:
    l = l.replace("\n", "")
    l = l.split(" ")
    num = int(l[0])*int(l[1])+int(l[2])
    arr = list(str(num))
    sm = 0
    for a in arr:
        sm += int(a)
    answers.append(sm)

for a in answers:
    print(a,end=" ")
print('')
