dimensions = []
while True:
    maxWidth = int(input())
    if maxWidth == 0:
        break
    boxWidth = 0
    boxWidthHighest = 0
    boxHeight = 0
    boxHeightTOT = 0
    while True:
        widthHeight = input().split()
        if widthHeight[0] == "-1" and widthHeight[1] == "-1":
            if boxWidthHighest < boxWidth:
                boxWidthHighest = boxWidth
            boxHeightTOT += boxHeight
            break
        if boxWidth + int(widthHeight[0]) <= maxWidth:
            boxWidth += int(widthHeight[0])
        else:
            if boxWidthHighest < boxWidth:
                boxWidthHighest = boxWidth
            boxWidth = 0
            boxHeightTOT += boxHeight
            boxHeight = 0
            if boxWidth + int(widthHeight[0]) <= maxWidth:
                boxWidth += int(widthHeight[0])
        if boxHeight < int(widthHeight[1]):
            boxHeight = int(widthHeight[1])
    dimensions.append("%s x %s" % (boxWidthHighest, boxHeightTOT))
for x in dimensions:
    print(x)
