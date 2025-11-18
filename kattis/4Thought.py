eq = ["4 * 4", "4 + 4", "4 - 4", "4 / 4"]
sumz = [16,8,0,1]
def findingEq(currentNum,listy):
    solution = "none"
    for current in range(len(sumz)):
        this = listy[current]
        for next in range(len(sumz)):
            that = listy[next]
            if this*that == currentNum:
                print(eq[current],"*",eq[next], "=", currentNum)
                solution = "*"
                break
            elif this+that == currentNum:
                print(eq[current],"+",eq[next], "=", currentNum)
                solution = "+"
                break
            elif this-that == currentNum:
                print(eq[current],"-",eq[next], "=", currentNum)
                solution = "-"
                break
            elif that != 0 and this//that == currentNum:
                print(eq[current],"/",eq[next], "=", currentNum)
                solution = "/"
                break
        if solution != "none":
            break
    #if solution == "none":
        #print("no solution")
    

def userIn():
    amtOfCases = int(input())
    cases = []
    for x in range(amtOfCases):
        cases.append(int(input()))
    return cases


def main()->None:
    #haha = userIn()
    for x in range(-500,500):
        findingEq(x,sumz)
main()