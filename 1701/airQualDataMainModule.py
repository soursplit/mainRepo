#
# COMP 1701 Fall 2025 Assignment 2 Part 2B
#
# Nelson Wing
#

#cauculates the median
def median(data)->float:
    #copies data so it doesent modify original list and sorts the copied data
    sortedList = data.copy()
    #simple sort algorithm that compares one item in the list against all the others to sort from least to greatest
    for current in range(len(sortedList)):
        biggest = current
        for next in range (current, len(sortedList)):
            if sortedList[next] < sortedList[biggest]:
                biggest=next
        sortedList[current], sortedList[biggest] = sortedList[biggest], sortedList[current]
    #checking if the list has an even amount of items
    if len(sortedList) // 2 == 0:
        #gets the median of an even numbered list with is the item in the middle
        med = sortedList[len(sortedList) //2]
    else:
        #gets the median of an odd numbered list which is the average of the two numbers closest to the middle of the sorted list
        med = ((sortedList[len(sortedList) //2]+sortedList[(len(sortedList) //2)-1])/2)
    return med

#cauculates the mean
def mean(data)->float:
    total = 0
    for x in data:
        total += x
    return total/len(data)

#gets air quality data for the locations form the user
def add(place)->int:
    data = []
    for x in place:
        data.append(int(input(f"Enter coresponding AQI to {x}: ")))
    return data

#gets the worst quality by sorting the list and taking the first two items
def worstQual(data)->int:
    #copies data so it doesent modify original list and sorts the copied data
    sortedList = data.copy()
    #simple sort algorithm that compares one item in the list against all the others to sort from greatest to least
    for current in range(len(sortedList)):
        biggest = current
        for next in range (current, len(sortedList)):
            #In this sort algorithm, the less-than sign was switched to the greater-than sign making the list sort from biggest to lowest rather than lowest to greatest
            if sortedList[next] > sortedList[biggest]:
                biggest=next
        sortedList[current], sortedList[biggest] = sortedList[biggest], sortedList[current]
    return[sortedList[1], sortedList[0]]

#cauculates what percent of the data is at a good air quality
def above50(data)->float:
    count = 0
    for x in data:
        if x <= 50:
            count += 1
    percent = (count/len(data))*100
    return(percent)