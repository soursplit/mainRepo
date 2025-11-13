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
    print(sort([5,62,3,78,2,3,4,666,41,1,2,3,4]))
main()