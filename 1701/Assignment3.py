def projectCSV(csv,listy):
    listyKeep = []
    boom = csv.copy
    for x in range(1,len(listy)):
        listyKeep.append(listy[x])
    print(listyKeep)

def columnCSV(objects):
    print("-------")
    for x in objects:
        print(x)
    print("-------")
def selectCSV(csv, column, item, objects):
    print(column)
    scan = csv.copy()
    num = objects.index(column)
    for x in scan:
        if x[num] != item and x[num] != column:
            print(f"removing {x}")
            csv.remove(x)
def printCSV(csv):
    strSize = []
    for column in csv:
        for row in column:
            if csv.index(column) == 0:
                strSize.append(len(row))
            current = column.index(row)
            if len(row) > strSize[current]:
                strSize[current] = len(row)
    print(strSize)
    print("----------------------------------------")
    for x in csv:
        if csv.index(x) == 1:
            print("----------------------------------------")
        #print(f"{x[0]:<11}{x[1]:<12}{x[2]:<6}{x[3]}")
        for column in csv:
            for row in range(len(column)):
                blah = int(strSize[row])+2
                print(f"{x[row]:<blah}", end = '')
            print()
    print("----------------------------------------")
def readCSV(csv):
    rawrrr = []
    with open(csv, mode = 'r') as file:
        for lines in file:
            lines = lines.replace("\n","")
            rawrrr.append(lines.split(','))
    return rawrrr
def main()->None:
    animalSight = []
    csvColumns = []
    while(True):
        currentCommand = str(input("Enter a command: ")).split(" ")
        if currentCommand[0] == "exit":
            break
        elif currentCommand[0] == "read":
            animalSight = readCSV(currentCommand[1])
            csvColumns = animalSight[0]
        elif currentCommand[0] == "print":
            printCSV(animalSight)
        elif currentCommand[0] == "select":
            selectCSV(animalSight, currentCommand[1], currentCommand[2], csvColumns)
        elif currentCommand[0] == "columns":
            columnCSV(csvColumns)
        elif currentCommand[0] == "project":
            projectCSV(animalSight,currentCommand)
        print(f"{len(animalSight)-1} rows")
main()