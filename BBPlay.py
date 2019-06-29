"""This module runs the simulation of the baseball game,
and returns the number of runs in a single game."""

from ActOutcomes import ActOutcomes

def HalfInning():
    (ba, ru, st, ou) = ('a', 0, 0, 0)
    o = 0
    while o < 3:
        (b, r, s, o) = ActOutcomes(ba, ru, st, ou)
        #print(b, r, s, o)
        (ba, ru, st, ou) = (b, r, s, o)
    return (ba, ru, st, ou)

def RunGame():
    runs = 0
    for i in range(18):
        (bas, run, str, out) = HalfInning()
        runs += run
    return runs


def main():
    print(RunGame())

if __name__ == '__main__':
    main()
