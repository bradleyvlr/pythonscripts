#!/usr/bin/python3
import os
file = open('/home/rosalux/pythonscripts/codeAbbey/data')
answers = []

for i in file.readlines():
    i = i[:-1]
    lst = i.split(' ')
    a = lst[0]
    for j in lst:
        if int(j) < int(a):
            a = j
    answers.append(a)
for k in answers:
    print(k,end=" ")
print('')
