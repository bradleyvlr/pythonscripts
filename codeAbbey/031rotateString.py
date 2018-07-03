#!/usr/bin/python3
dat = open("data")
lin = dat.readlines()
answers = []
for l in lin:
    l = l.replace("\n", "")
    l = l.split(" ")
    num = int(l[0])
    string = l[1]
    print(string[num::]+string[0:num])
    newString = string[num::] + string[::num]
for a in answers:
    print(a,end=" ")
print()
