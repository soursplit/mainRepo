import random

def sort(listy):
    sortedList = listy
    for current in range(len(sortedList)):
        biggest = current
        for next in range (current, len(sortedList)):
            if sortedList[next] < sortedList[biggest]:
                biggest=next
        sortedList[current], sortedList[biggest] = sortedList[biggest], sortedList[current]
    return sortedList


def main():
    listy=[]
    for x in range(1000):
        listy.append(random.randint(1,1000))
    print(str(listy)+"\n")
    print(sort(listy))
main()