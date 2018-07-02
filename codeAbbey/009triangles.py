#!/usr/bin/python3
dat = open("data")
arr = dat.readlines()
answers = []
for d in arr:
    d = d.replace("\n","")
    d = d.split(" ")
    if int(d[0]) > (int(d[1]) + int(d[2])) or int(d[1]) > (int(d[0]) + int(d[2])) or int(d[2]) > (int(d[1]) + int(d[0])):
        answers.append(0)
    else:
        answers.append(1)
for a in answers:
    print(a,end=" ")
print('')

