#
# COMP 1701 Fall 2025 Assignment 1
#
# Nelson Wing
#

import math

#Constants:
homageStatueLat = 51.1376194
homageStatueLong = 114.13369889
adultFare = 3.8
avgEarthRaduis = 6371

def DMStoDD(degree,min,sec): #Function for converting coordinates in DMS notation to decimal degree notation
    return(degree+(min/60)+(sec/3600))

def haversineFormulae(startLat, startLong, endLat, endLong): #Cauculates the distance between two coodinates (in DD notation) assuming the earth is a perfect sphere
    deltaLat = endLat - startLat
    deltaLong = endLong - startLong
    interValueOne = (math.sin(deltaLat/2)**2) + (math.cos(startLat)) * (math.cos(endLat)) * (math.sin(deltaLong/2)**2)
    interValueTwo = 2 * math.atan2(math.sqrt(interValueOne), math.sqrt(1-interValueOne))
    dist = avgEarthRaduis * interValueTwo
    return(dist/100)

def fareReductionFormula(dist,fare): #Cauculates what the fare is reduced to based on the total distance traveled 
    return(fare-(1/(0.4+math.e**(3-dist))))

def main()->None: #Main gets user input and calls functions
    startLatDegree = int(input("What is the lattitude's degrees? "))
    startLatMin = int(input("What is the lattitude's minutes? "))
    startLatSec =  float(input("What is the lattitude's secconds? (to three decimals) "))

    startLongDegree = int(input("What is the longitude degrees? "))
    startLongMin = int(input("What is the longitude minutes? "))
    startLongsec = float(input("What is the longitude secconds? (to three decimals) "))

    totalDist = haversineFormulae(DMStoDD(startLatDegree,startLatMin,startLatSec),DMStoDD(startLongDegree,startLongMin,startLongsec),homageStatueLat,homageStatueLong)
    fareReducted = fareReductionFormula(totalDist,adultFare)

    print(f"\nTravelling from user's starting location (at {startLatDegree}° {startLatMin}' {startLatSec}\" North, {startLongDegree}° {startLongMin}' {startLongsec}\" West) to the Homage statue on MRU campus:\nThe distance is approximately {round(totalDist,1)} km.\nTheir fare would be reduced to ${format(round(fareReducted,2),'.2f')}.")

main()