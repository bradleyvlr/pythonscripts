#!/usr/bin/python3
dat = open("data")
lin = dat.readlines()
answers = []
for l in lin:
    l = l.replace("\n", "")
    l = l.split(" ")
    ave = 0
    for i in l:
        ave += int(i)
    ave = round(ave / (len(l)-1))
    answers.append(ave)
for a in answers:
    print(a,end=" ")
print("")
