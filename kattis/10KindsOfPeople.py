def main()->None:
    print("hehehehe")
    mapPlot = input().split(" ")
    theMap = [0]*int(mapPlot[0])
    for x in range(int(mapPlot[0])):
        theMap[x] = list(input())
    amtOfcoords = int(input())
    coordanates = [0] * amtOfcoords
    for x in range(amtOfcoords):
        coordanates[x] = input().split(" ")
    #for x in range(int(mapPlot[0])):
    for y in range(amtOfcoords):
        oneX = int(coordanates[y][0])-1
        oneY = int(coordanates[y][1])-1
        twoX = int(coordanates[y][2])-1
        twoY = int(coordanates[y][3])-1

        oneXY = theMap[oneX][oneY]
        twoXY = theMap[twoX][twoY]

        for x in range(int(mapPlot[0])):
            for y in theMap[x]:
                break


        #if oneXY == '0' and twoXY == '0':
            #print("binary")
        #elif oneXY == '1' and twoXY == '1':
            #print("decimal")
        #else:
            #print("neither")

        

main()