#!/usr/bin/python3
dat = open("data")
lin = dat.readlines()
org = int(lin.pop(0))
for x in lin:
    x = x.replace("\n","")
    x = x.split(" ")
    if x[0] == '+':
        org += int(x[1])
    elif x[0] == '-':
        org -= int(x[1])
    elif x[0] == '*':
        org *= int(x[1])
    elif x[0] == '/':
        org = org/int(x[1])
    elif x[0] == '%':
        org = org % int(x[1])
print(org)
