"""
The code in this module is meant to help the overall program keep track
of the state of runners on bases as the simulation runs.

It is dependent on another module, named DiceAct, within the main function
returning an action based on the simulated roll of two six-sided dice.

The below matrix is the basis of the base formations used by this function,
where (1,0,1) would indicate runners on first and third base.

a=(0,0,0)
b=(1,0,0)
c=(0,1,0)
d=(0,0,1)
e=(1,1,0)
f=(1,0,1)
g=(0,1,1)
h=(1,1,1)"""

import random
from DiceAct import ActionMap

def ActOutcomes(bases, runs, strikes, outs):
    DiceAct = ActionMap()
    if DiceAct == "double":
        strikes = 0
        if bases == 'a':
            bases = 'c'
        elif bases == 'b':
            bases = 'g'
        elif bases in ('c', 'd'):
            bases = 'c'
            runs += 1
        elif bases in ('e', 'f'):
            bases = 'g'
            runs += 1
        elif bases == 'g':
            bases = 'c'
            runs += 2
        elif bases == 'h':
            bases = 'g'
            runs += 2
    elif DiceAct in ("single", "base on error", "base on balls"):
        strikes = 0
        if bases == 'a':
            bases = 'b'
        elif bases == 'b':
            bases = 'e'
        elif bases == 'c':
            bases = 'f'
        elif bases == 'd':
            bases = 'b'
            runs += 1
        elif bases == 'e':
            bases = 'h'
        elif bases == 'f':
            bases = 'e'
            runs += 1
        elif bases == 'g':
            bases = 'f'
            runs += 1
        elif bases == 'h':
            bases = 'h'
            runs += 1
    elif DiceAct == "strike":
        strikes += 1
    elif DiceAct in ("foul out", "out at first", "fly out"):
        strikes = 0
        if bases == 'a':
            bases = 'a'
            outs += 1
        if bases == 'b':
            bases = 'c'
            outs += 1
        elif bases == 'c':
            bases = 'd'
            outs += 1
        elif bases == 'd':
            bases = 'a'
            runs += 1
            outs += 1
        elif bases == 'e':
            bases = 'g'
            outs += 1
        elif bases == 'f':
            bases = 'c'
            runs += 1
            outs += 1
        elif bases == 'g':
            bases = 'd'
            runs += 1
            outs += 1
        elif bases == 'h':
            bases = 'g'
            runs += 1
            outs += 1
    elif DiceAct == "double play":
        strikes = 0
        if bases == 'a':
            bases = 'a'
            outs += 1
        elif bases in ('b', 'c', 'd'):
            bases = 'a'
            outs += 2
        elif bases == 'e':
            bases = 'd'
            outs += 2
        elif bases in ('f', 'g'):
            bases = 'a'
            outs += 2
            runs += 1
        elif bases == 'h':
            bases = 'd'
            outs += 2
            runs +=1
    elif DiceAct == "triple play":
        strikes = 0
        if bases == 'a':
            bases = 'a'
            outs += 1
        elif bases in ('b', 'c', 'd'):
            bases = 'a'
            outs +=2
        elif bases in ('e', 'f', 'g'):
            bases = 'a'
            outs += 3
        elif bases == 'h':
            bases = 'a'
            outs += 3
            runs += 1
    elif DiceAct == "home run":
        strikes = 0
        if bases == 'a':
            bases = 'a'
            runs += 1
        elif bases in ('b', 'c', 'd'):
            bases = 'a'
            runs += 2
        elif bases in ('e', 'f', 'g'):
            bases = 'a'
            runs += 3
        elif bases == 'h':
            bases = 'a'
            runs += 4
    return(bases, runs, strikes, outs)

def main():
    (ba, ru, st, ou) = ('a', 0, 0, 0)
    o = 0
    while o < 3:
        (b, r, s, o) = ActOutcomes(ba, ru, st, ou)
        #print(b, r, s, o)
        (ba, ru, st, ou) = (b, r, s, o)

if __name__ == '__main__':
    main()
