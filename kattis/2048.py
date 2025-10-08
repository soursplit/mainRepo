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



    elif direction == 1: #up
        print("haha")
    elif direction == 2: #Right
        print("haha")
    elif direction == 3: #down
        print("haha")


main()