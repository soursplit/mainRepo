def main()->None:
    amountOfChar = int(input())
    word = list(input())
    lPresent = False
    vPresent = False
    zero = False
    one = False
    two = False
    for x in word:
        if x == "l" or x == "L":
            lPresent = True
        if x == "v" or x == "V":
            vPresent = True
    if lPresent == False and vPresent == False:
        two = True
    else:
        for x in range(amountOfChar):
            y = word[x]
            if x != amountOfChar-1 and y == "l" or y == "L":
                if word[x+1] == "v" or word[x+1] == "V":
                    zero = True
                else:
                    one = True
                    
    if zero:
        print(0)
    elif one:
        print(1)
    elif two:
        print(2)
main()