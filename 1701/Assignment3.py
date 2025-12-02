#Read
#save
#select
#project
#columns
#count
#disr
#sort
#print
def sortCSV(csv,item):
    sortedListy = []
    itemToSort = csv[0].index(item)
    for column in csv:
        if csv.index(column) != 0:
            for row in range(len(column)):
                if row == itemToSort:
                    sortedListy.append(column[row])

    sortedList = sortedListy
    for current in range(len(sortedList)):
        biggest = current
        for next in range (current, len(sortedList)):
            if sortedList[next] < sortedList[biggest]:
                biggest=next
        print(sortedList[current],sortedList[biggest])
        sortedList[current], sortedList[biggest] = sortedList[biggest], sortedList[current]
        for x in range(len(csv[0])):
            print(csv[current][x],"<",csv[biggest][x])
            csv[current][x], csv[biggest][x] = csv[biggest][x], csv[current][x]
            
    print(sortedList)
    print(csv)

def distrCSV(csv, item):
    thingy = csv[0].index(item)
    track = []
    listy = []
    newList = []
    for x in range(1,len(csv)):
        listy.append(csv[x][thingy])
    for x in range(1,len(csv)):
        if csv[x][thingy] not in track:
            track.append(csv[x][thingy])
    for x in range(len(track)):
        print(f"{track[x]} {listy.count(track[x])}")
        newList.append([track[x],listy.count(track[x])])
    
def projectCSV(csv,listy):
    itemsToKeep = []
    keptItems = []
    for input in range(1,len(listy)):
        itemsToKeep.append(listy[input])
    print(itemsToKeep)
    for column in csv:
        temp = []
        for row in range(len(column)):
            print("hi")
            for remove in itemsToKeep:
                if row == csv[0].index(remove):
                    temp.append(column[row])
        keptItems.append(temp)
    for x in keptItems:
        print(x)

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
        print(f"{x[0]:<11}{x[1]:<12}{x[2]:<6}{x[3]}")
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
    print("starting...")
    while(True):
        currentCommand = str(input("Enter a command: ")).split(" ")
        if currentCommand[0] == "exit":
            print("... Exiting")
            break
        elif currentCommand[0] == "read":
            animalSight = readCSV(currentCommand[1])
            csvColumns = animalSight[0]
        elif currentCommand[0] == "print":
            printCSV(animalSight)
        elif currentCommand[0] == "select":
            selectCSV(animalSight, currentCommand[1], currentCommand[2], animalSight[0])
        elif currentCommand[0] == "columns":
            columnCSV(animalSight[0])
        elif currentCommand[0] == "project":
            projectCSV(animalSight,currentCommand)
        elif currentCommand[0] == "index":
            distrCSV(animalSight,currentCommand[1])
        elif currentCommand[0] == "sort":
            sortCSV(animalSight,currentCommand[1])
        print(f"{len(animalSight)-1} rows")
main()