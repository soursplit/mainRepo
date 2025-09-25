def main()->None:
    numbers = input().split(" ")
    editList = numbers
    letters = list(input())
    
    for x in range(3):
        currentNum = int(numbers[x])
        for y in range(3):
            compareNum = int(numbers[y])
            if currentNum > compareNum:
                editList[x], editList[y] = editList[y], editList[x]

    for x in range(3):
        z = letters[x]
        if z == "A":
            A = x
        if z == "B":
            B = x
        if z == "C":
            C = x
    print(f"{editList[C]} {editList[B]} {editList[A]}")
main()