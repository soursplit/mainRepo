#
# COMP 1701 Fall 2025 Assignment 2 Part 2A
#
# Nelson Wing
#

#Importing functions from the module
from airQualDataMainModule import mean, median, worstQual,above50,add

#Defining location constants
locations = ["Airdrie","Ardrossan","Banff South of Bow River","Brooks Meadowplace","Calgary Varsity","Caroline","Cold Lake South","Conklin Community","Cougar Point Road, Canmore","Drayton Valley"]

def main()->None:
    AQI = add(locations)
    #Original air quality data in order corresponding with location data for easy testing
    #AQI = [141,53,46,142,153,136,52,55,23,73]
    print(f"The mean of the air quality of the locations is {round(mean(AQI),1)}.")
    print(f"The median of the air quality of the locations is {round(median(AQI),1)}.")
    print(f"The locations with the worst air quality data is {locations[AQI.index(worstQual(AQI)[0])]} with an air quality of {worstQual(AQI)[0]} and {locations[AQI.index(worstQual(AQI)[1])]} with an air quality of {worstQual(AQI)[1]}.")
    print(f"Among all the locations %{int(round(above50(AQI)))} of them have a good air quality.")
main()