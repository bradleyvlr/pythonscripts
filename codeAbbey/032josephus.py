#!/usr/bin/python3
def main():
    ppl = int(input("How many people are to be killed?  - "))
    stp = int(input("How many steps between kills?  - "))
    arr = []
    for a in range(ppl):
        arr.append(a + 1)
    num = 0
    while len(arr) > 2:
        num += stp
        while num > len(arr):
            num -= len(arr)
            zeroElim(arr)
        arr[num-1] = 0
        print(arr)
        print(num)
    zeroElim(arr)
    print(arr[0])
def zeroElim(array):
        if 0 in array:
            midi = []
            for a in range(len(array)):
                if array[a] == 0:
                    midi.append(a) 
            for m in range(len(midi)):
                array.pop(midi[m]-m)
main() 
