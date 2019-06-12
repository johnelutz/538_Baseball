from D6D6 import D6D6die

def ActionMap():
    ddd = D6D6die()
    if ddd == [1, 1]:
        return("double")
    elif ddd in ([1, 2], [1, 3], [1, 4]):
        return("single")
    elif ddd == [1, 5]:
        return("base on error")
    elif ddd == [1, 6]:
        return("base on balls")
    elif ddd in ([2, 2], [2, 3], [2, 4], [2, 5]):
        return("strike")
    elif ddd == [2, 6]:
        return("foul out")
    elif ddd in ([3, 3], [3, 4], [3, 5], [3, 6]):
        return("out at first")
    elif ddd in ([4, 4], [4, 5], [4, 6]):
        return("fly out")
    elif ddd == [5, 5]:
        return("double play")
    elif ddd == [5, 6]:
        return("triple play")
    elif ddd == [6, 6]:
        return("home run")

def main():
    print(ActionMap())

if __name__ == '__main__':
    main()
