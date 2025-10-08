def movingLeft(rowList):
    for x in range(len(rowList)):
            mod = 0
            while(True):
                #print(x,x+mod)
                #print(f"before change: {rowList}\n")
                if rowList[x+mod] == "0":
                    #print("non num\n")
                    break
                elif x == 0+mod or x+mod == 0:
                    #print("EOF\n")
                    break
                elif rowList[x+mod] == '1024' and rowList[(x+mod)-1] == '1024':
                    rowList[(x+mod)-1], rowList[x+mod] = "2048", "0"
                    mod -= 1
                elif rowList[x+mod] != '2048' and rowList[(x+mod)-1] == rowList[x+mod]:
                    rowList[(x+mod)-1], rowList[x+mod] = str(int(rowList[x+mod])**2), "0"
                    mod -= 1
                elif rowList[(x+mod)-1] == '0':
                    rowList[(x+mod)-1], rowList[x+mod] = rowList[x+mod], rowList[(x+mod)-1]
                    mod -= 1
                elif rowList[(x+mod)-1] != rowList[x+mod]:
                    #print("nonmatching")
                    break
                #print(f"after change: {rowList}\n")
    return rowList

def movingUp(ArowList,BrowList,CrowList,DrowList):
    mainList=[ArowList,BrowList,CrowList,DrowList]
    for column in range(4):
        print(f"{mainList[0][0]} {mainList[0][1]} {mainList[0][2]} {mainList[0][3]}\n{mainList[1][0]} {mainList[1][1]} {mainList[1][2]} {mainList[1][3]}\n{mainList[2][0]} {mainList[2][1]} {mainList[2][2]} {mainList[2][3]}\n{mainList[3][0]} {mainList[3][1]} {mainList[3][2]} {mainList[3][3]}\n\n")
        for row in range(4):
            mod = 0
            while(True):
                current = mainList[row+mod][column]
                print(row,mod,row+mod-1)
                next = mainList[row+mod-1][column]
                
                if current == "0":
                    print('nonnumber')
                    break
                elif row == 0 + mod:
                    print('EOF')
                    break
                elif next == '0':
                    mainList[row+mod-1][column], mainList[row+mod][column] = mainList[row+mod][column], mainList[row+mod-1][column]
                    mod -= 1
                    print("0move")
                elif next == current:
                    mainList[row+mod-1][column], mainList[row+mod][column] = str(int(mainList[row+mod][column])**2), "0"
                    mod -= 1
                    print('combine')
                elif next != current:
                    print('nonmatching')
                    break


def main():
    rowOne = input().split(" ")
    rowTwo = input().split(" ")
    rowThree = input().split(" ")
    rowFour = input().split(" ")
    direction = input()

    if direction == '0': #left
        rowOne = movingLeft(rowOne)
        rowTwo = movingLeft(rowTwo)
        rowThree = movingLeft(rowThree)
        rowFour = movingLeft(rowFour)
        print(f"{rowOne}\n{rowTwo}\n{rowThree}\n{rowFour}")



    elif direction == '1': #up
        rowOne = movingUp(rowOne,rowTwo,rowThree,rowFour)
    elif direction == 2: #Right
        print("haha")
    elif direction == 3: #down
        print("haha")


main()