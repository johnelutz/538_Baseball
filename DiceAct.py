from D6D6 import D6D6die

def ActionMap():
    ddd = 0
    ddd = D6D6die()
    if ddd == (1, 1):
        return("double")
    elif ddd == (1, 2) or (1, 3) or (1, 4):
        return("single")
    elif ddd == (1, 5):
        return("base on error")
    elif ddd == (1, 6):
        return("base on balls")
    elif ddd == (2, 2) or (2, 3) or (2, 4) or (2, 5):
        return("strike")
    elif ddd == (2, 6):
        return("foul out")
    elif ddd == (3, 3) or (3, 4) or (3, 5) or (3, 6):
        return("out at first")
    elif ddd == (4, 4) or (4, 5) or (4, 6):
        return("fly out")
    elif ddd == (5, 5):
        return("double play")
    elif ddd == (5, 6):
        return("triple")
    elif ddd == (6, 6):
        return("home run")
    

    
