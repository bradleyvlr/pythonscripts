#!/usr/bin/python3
import re
dat = open("data")
lin = dat.readlines()
answers = []
vow = re.compile(r'[aAeEoIiOuUyY]')
for l in lin:
    l = l.replace("\n", "")
    answers.append(len(re.findall(vow,l)))
for a in answers:
    print(a,end=" ")
print()
