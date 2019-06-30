"""This module will run the BBPlay module n times and return
the average number of runs scored in 9 innings."""

from BBPlay import RunGame

def FindAvg(n):
    AvgRun = 0
    for i in range(n):
        AvgRun = AvgRun + (RunGame())
    return AvgRun/n

def main():
    print(FindAvg(10000))

if __name__ == '__main__':
    main()
