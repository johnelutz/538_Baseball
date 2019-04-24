import random

def D6D6die():
    roll = (random.randint(1,6), random.randint(1,6))
    return sorted(roll)
