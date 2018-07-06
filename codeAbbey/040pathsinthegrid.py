#!/usr/bin/python3
def main():
    grid = getData()
    lng = len(grid) + len(grid[0]) - 2
def getData():
    dat = open("data")
    lin = dat.readlines()
    answers = []
    for l in range(len(lin)):
        lin[l] = lin[l].replace("\n", "")
        lin[l] = lin[l].split(' ')

def getBinary(num,mx):
    #I want to turn an int into a binary array, fixed at length of path
    arr = []
    for range(num,-1,-1):
        
