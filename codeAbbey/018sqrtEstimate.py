#!/usr/bin/python3
dat = open("data")
lin = dat.readlines()
answers = []
for l in lin:
    l = l.replace("\n", "")
    l = l.split(" ")
    r = 1
    for i in range(int(l[1])):
        r = (r + (int(l[0])/r))/2
    answers.append(r)
for a in answers:
    print(str(a),end=" ")
print('')
