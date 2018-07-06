#!/usr/bin/python3
def main():
    wrong=[[],[],[],[]]
    poss=[[],[],[],[]]
    final = [False,False,False,False]
    game = getData()
    cycle(final,wrong,poss,game)
    highOccur(poss,final)
    uniqOccur(poss,final)
    cycle(final,wrong,poss,game)
    highOccur(poss,final)
    uniqOccur(poss,final)
    inducer(poss,wrong,final)
    print(poss)

def getData():
    dat = open("data")
    lin = dat.readlines()
    game = []
    for l in range(len(lin)):
        lin[l] = lin[l].replace("\n", "")
        lin[l] = lin[l].split(" ")
        lin[l][0] = list(lin[l][0])
        lin[l][1] = int(lin[l][1])
    return lin

def cycle(finished,wr,ps,gm):
    for g in gm:
        if g[1] == 0:
            for i in range(4):
                if g[0][i] not in wr[i]:
                    wr[i].append(g[0][i])
        elif g[1] == 1:
            for i in range(4):
                if isNotTaken(g[0],ps,finished) and not finished[i]:
                    ps[i].append(g[0][i])
                elif not isNotTaken(g[0],ps,finished):
                    wr[i].append(g[0][i])
        else:
            for i in range(4):
                if not finished[i]:
                    ps[i].append(g[0][i])
        for i in range(4):
            if not finished[i]:
                for x in wr[i]:
                    if x in ps[i]:
                        ps[i].remove(x)

def isNotTaken(itera,p,fin):
    for a in range(4):
        if fin[a] and itera[a] == p[a]:
            return False
    return True



def highOccur(ps,fn):
    for p in range(4):
        rep = -1
        for i in ps[p]:
            if ps[p].count(i) >= 3:
                rep = i
        if int(rep) >=0:
            fn[p] = True
            ps[p] = [rep]

def uniqOccur(ps,fn):
    for p in range(4):
        if len(ps[p]) > 1 and len(set(ps[p])) == 1:
            fn[p] = True
            ps[p] = set(ps[p])

def inducer(ps,wr,fn):
    for p in range(4):
        if not fn[p]:
            midi = ['0','1','2','3','4','5','6','7','8','9']
            for x in wr[p]:
                midi.remove(x)
            if len(midi) == 1:
                ps[p] = midi
                fn[p] = True

main()
