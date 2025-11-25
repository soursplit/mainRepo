ticTac = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9']]
while(True):
    for x in ticTac:
        print(x)
    xTurn = True
    while(xTurn):
        print("print where do you want to place x?")
        nextPosX = int(input()) - 1
        if nextPosX <= 3 and ticTac[0][nextPosX//3] != "X" and ticTac[0][nextPosX//3] != "O":
            ticTac[0][nextPosX] = "X"
            xTurn = False
        elif nextPosX > 3 and nextPosX <= 6 and ticTac[1][nextPosX//3] != "X" and ticTac[1][nextPosX//3] != "O":
            ticTac[1][nextPosX] = "X"
            xTurn = False
        elif nextPosX > 6 and ticTac[2][nextPosX//3] != "X" and ticTac[2][nextPosX//3] != "O":
            ticTac[3][nextPosX] = "X"
            xTurn = False
        else:
            print("that spot is already taken!\n")