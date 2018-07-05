#!/usr/bin/python3
import sys
def main():
    code = []
    sys.argv.pop(0)
    for a in sys.argv:
        if oddbincheck(binary(int(a))):
            if int(a) > 128:
                a = str(int(a) - 128)
            code.append(chr(int(a))) 
    for f in code:
        print(str(f),end="")
    print()


def binary(integer):
    midi = [0,0,0,0,0,0,0,0]
    for i in range(7,-1,-1):
        if integer >= 2**i:
            integer -= 2**i
            midi[(i * -1)-1] = 1
    return midi
def bininflate(b):
    b.pop(0)
    num = 0
    for c in range(len(b)):
        num += 2**c * b[-1 -c]

def oddbincheck(b):
    s = 0
    for i in b:
        s += i
    if s % 2 == 0:
        return True
    else:
        return False
main()
