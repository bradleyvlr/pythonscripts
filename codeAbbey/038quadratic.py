#!/usr/bin/python3
import math
dat = open("data")
lin = dat.readlines()
answers = []
for l in lin:
    l = l.replace("\n", "")
    l = l.split(" ")
    a = int(l[0])
    b = int(l[1])
    c = int(l[2])
    ans = []
    midi = b**2 - 4*a*c
    if midi < 0:
        ans.append(str(int((-1*b)/(2*a)))+'+'+str(int(math.sqrt(abs(midi))/(2*a)))+'i')
        ans.append(str(int((-1*b)/(2*a)))+'-'+str(int(math.sqrt(abs(midi))/(2*a)))+'i')
        answers.append(ans)
    else:
        ans.append(str(int(((-1*b)+math.sqrt(b**2-4*a*c))/(2*a))))
        ans.append(str(int(((-1*b)-math.sqrt(b**2-4*a*c))/(2*a))))
        answers.append(ans)
for a in range(len(answers)-1):
    print(answers[a][0]+' '+answers[a][1],end="; ")
print(answers[len(answers)-1][0],end=" ")
print(answers[len(answers)-1][1])
