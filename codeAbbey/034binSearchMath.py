#!/usr/bin/python3
import math
dat = open("data")
lin = dat.readlines()
answers = []
for l in lin:
    l = l.replace("\n", "")
    l = l.split(" ")
    A = float(l[0])
    B = float(l[1])
    C = float(l[2])
    D = float(l[3])
    blow = 0
    bhi = 100
    while bhi - blow > 10.0 ** (-7):
        x = (bhi + blow)/2
        midi = A*x + (B * (math.sqrt(x**3))) - (C * math.e ** ((-1*x)/50)) - D
        if midi > 0:
            bhi = x
            print("bhi: " + str(bhi))
        elif midi < 0:
            blow = x
            print("blow: " + str(bhi))
        else:
            bhi = midi
            blow = midi
    answers.append(bhi)
for a in answers:
    print(str(a),end=' ')
print()
