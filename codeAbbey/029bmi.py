#!/usr/bin/python3
dat = open("data")
lin = dat.readlines()
answers = []
for l in lin:
    l = l.replace("\n", "")
    l = l.split(" ")
    bmi = float(l[0]) / float(l[1])**2
    if bmi < 18.5:
        answers.append('under')
    elif bmi < 25.0:
        answers.append('normal')
    elif bmi < 30.0:
        answers.append('over')
    else:
        answers.append('obese')
print(' '.join(answers))
