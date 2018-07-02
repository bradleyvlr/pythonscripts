#!/usr/bin/python3
dat = open("data")
lin = dat.readlines()
answers = []
for l in lin:
    l = l.replace("\n", "")
    l = l.split(" ")
