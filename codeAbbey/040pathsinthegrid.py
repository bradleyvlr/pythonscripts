#!/usr/bin/python3
def main():
    grid = getData()
    lng = len(grid) + len(grid[0]) - 2
    pathTotal = 2**lng
    countValid = traverse(pathTotal,lng,grid)
    print(countValid)

def getBin(num,size):
    binNum=[]
    for fact in range(size-1,-1,-1):
        if num >= 2**fact:
            binNum.insert(0,1)
            num -= 2**fact
        else:
            binNum.insert(0,0)
    return binNum

def getData():
    dat = open("data")
    arr = dat.readlines()
    for a in range(len(arr)):
        arr[a] = arr[a].replace("\n","")
        arr[a] = arr[a].split(" ")
    return arr

def traverse(total,length,grd):
    count = 0
    for path in range(total):
        path = getBin(path,length)
        if path.count(0) >len(grd)-1 or path.count(1) > len(grd[0])-1:
            print('nah')
            continue
        if isValid(path,grd):
            count += 1
            print('plusOne')
            continue
        else:
            print('X')
            continue
    return count

def isValid(path,grid):
    x = 0
    y = 0
    for step in path:
        if step == 0:
            y += 1
        else:
            x += 1
        if grid[y][x] == 'X':
            return False
    return True

main()


