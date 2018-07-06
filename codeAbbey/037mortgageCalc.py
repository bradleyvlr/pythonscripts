#!/usr/bin/python3
import sys, math
def main():
    P = int(sys.argv[1])
    R = int(sys.argv[2])
    M = int(sys.argv[3])
    minInit = math.ceil(binPay(M,P,R))
    print(iterMin(M,R,P,minInit))
    

def payoff(p,r,m,payment):
    month = 0
    while p > 0 and month < 1000:
        p = p+(p*(r/1200))-payment
        month += 1
    return month

def binPay(month,p,r):
    hi = 1000000
    low = 0
    current = 0
    step = 0
    while (month+1) != current:
        pguess = (hi+low)/2
        current = payoff(p,r,month,pguess)
        if current < (month+1):
            hi = pguess
        elif current > (month+1):
            low = pguess
        step += 1
    return pguess


def iterMin(m,r,p,strt):
    current = 200
    while current>m:
        print(strt)
        strt += 1
        current = payoff(p,r,m,strt)
        print(current)
    return strt
     
main()
        


