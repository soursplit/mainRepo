#
# COMP 1701 Fall 2025 Assignment 1 part 2A
#
# Nelson Wing
#

#Imports functions from module file
from transitFareModule import DMStoDD, haversineFormulae, fareReductionFormula

#Constants:
#Homage statue coordinates in DMS notation
homageStatueLat = 51.1376194
homageStatueLong = 114.13369889

#The adult fare taken from the Calgary transit website
adultFare = 3.8

#The earth radius taken from wikipedia
avgEarthRaduis = 6371.0087714


def main()->None: #Main gets user input and calls functions
    #Asks the user for their starting latitude coordinates in DMS notation
    startLatDegree = int(input("What is the lattitude's degrees? "))
    startLatMin = int(input("What is the lattitude's minutes? "))
    startLatSec =  float(input("What is the lattitude's secconds? (to three decimals) "))
   
    #Asks the user for their starting longitude coordinates in DMS notation
    startLongDegree = int(input("What is the longitude degrees? "))
    startLongMin = int(input("What is the longitude minutes? "))
    startLongsec = float(input("What is the longitude secconds? (to three decimals) "))

    #Calls functions to convert the given DMS notation to DD notation and to get the total distance travelled between the starting coordinates and the coordinates of the homage statue
    totalDist = haversineFormulae(DMStoDD(startLatDegree,startLatMin,startLatSec),DMStoDD(startLongDegree,startLongMin,startLongsec),homageStatueLat,homageStatueLong,avgEarthRaduis)
    
    #Calls the fareReductionFormula to cauculate the users total fare using the total distance and the current Calgary fare cost
    fareReducted = fareReductionFormula(totalDist,adultFare)
    
    #Prints out the users results in the format that was used in the assignment example
    print(f"\nTravelling from user's starting location (at {startLatDegree}° {startLatMin}' {startLatSec}\" North, {startLongDegree}° {startLongMin}' {startLongsec}\" West) to the Homage statue on MRU campus:\nThe distance is approximately {round(totalDist,1)} km.\nTheir fare would be reduced to ${format(round(fareReducted,2),'.2f')}.")

main()