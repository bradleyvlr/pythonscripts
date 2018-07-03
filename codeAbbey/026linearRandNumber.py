#!/usr/bin/python3
dat = open("data")
lin = dat.readlines()
answers = []
for l in lin:
    l = l.replace("\n", "")
    l = l.split(" ")
    a = int(l[0])
    c = int(l[1])
    m = int(l[2])
    x = int(l[3])
    n = int(l[4])
    
    for i in range(n):
        x = ((a*x)+c)%m
    answers.append(x)
for f in answers:
    print(str(f),end=" ")
print()
