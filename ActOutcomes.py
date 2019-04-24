"""
The code in this module is meant to help the overall program keep track
of the state of runners on bases as the simulation runs.

It is dependent on another module, named DiceAct, within the main function
returning an action based on the simulated roll of two six-sided dice.
"""
import random

a=(0,0,0)
b=(1,0,0)
c=(0,1,0)
d=(0,0,1)
e=(1,1,0)
f=(1,0,1)
g=(0,1,1)
h=(1,1,1)

bases = a
runs = 0
strikes = 0
outs = 0

def ActOutcomes(DiceAct):
    if DiceAct == "double":
        if bases == a:
            bases = c
        elif bases == b:
            bases = g
        elif bases == c or d:
            bases = c
            runs += 1
        elif bases == e or f:
            bases = g
            runs += 1
        elif bases == g:
            bases = c
            runs += 2
        elif bases == h:
            bases = g
            bases += 2
    elif DiceAct == "single" or "base on error" or "base on balls":
        if bases == a:
            bases = b
        elif bases == b:
            bases = e
        elif bases == c:
            bases = f
        elif bases == d:
            bases = b
            runs += 1
        elif bases == e:
            bases = h
        elif bases == f
            bases = e
            runs += 1
        elif bases == g:
            bases = f
            runs += 1
        elif bases == h:
            bases = h
            bases += 1
    elif DiceAct == "strike":
        strikes += 1
    elif DiceAct == "foul out" or "out at first" or "fly out":
        outs += 1
        if bases == b:
            bases = c
        elif bases == c:
            bases = d
        elif bases == d:
            bases = a
            runs += 1
        elif bases == e:
            bases = g
        elif bases == f:
            bases = c
            runs += 1
        elif bases == g:
            bases = d
            runs += 1
        elif bases == h:
            bases = g
            runs += 1
    elif DiceAct == "double play":
        if bases == a:
            bases = a
            outs += 1
        elif bases == b or c or d:
            bases = a
            outs += 2
        elif bases == e:
            bases = d
            outs += 2
        elif bases == f or g:
            bases = a
            outs += 2
            runs += 1
        elif bases == h:
            bases = d
            outs += 2
            runs +=1
    elif DiceAct == "triple":
        if bases == a:
            bases = a
            outs += 1
        elif bases == b or c or d:
            bases = a
            outs +=2
        elif bases == e or f or g:
            bases = a
            outs += 3
        elif bases == h:
            bases = a
            outs += 3
            runs += 1
    elif DiceAct = "homerun":
        if bases == a:
            bases = a
            runs += 1
        elif bases == b or c or d:
            bases = a
            runs += 2
        elif bases == e or f or g:
            bases = a
            runs += 3
        elif bases == h:
            bases = a
            runs += 4
        
    return(bases, runs, strikes, outs)


    
    
        

        
