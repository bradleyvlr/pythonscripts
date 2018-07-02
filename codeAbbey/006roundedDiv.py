#!/usr/bin/python3
import math, os

dat = open("data")
lin = dat.readlines()
answers=[]
for i in lin:
    i = i.replace("/n", "")
    arri = i.split(" ")
    ansi = int(arri[0])/int(arri[1])
    temp = int(arri[0])//int(arri[1])
    if ansi-temp >= 0.5:
        temp +=1
    answers.append(temp)
for a in answers:
    print(a,end=" ")
print("")
    
