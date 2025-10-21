#
# COMP 1701 Fall 2025 Assignment 1 part 2B
#
# Nelson Wing
#

import math

def DMStoDD(degree,min,sec)->float: #Function for converting coordinates in DMS notation to decimal degree notation
    return(degree+(min/60)+(sec/3600))

def haversineFormulae(startLat, startLong, endLat, endLong, earthRad) -> float: #Cauculates the distance between two coodinates (in DD notation) assuming the earth is a perfect sphere using the haversine formula
    deltaLat = endLat - startLat
    deltaLong = endLong - startLong
    interValueOne = (math.sin(deltaLat/2)**2) + (math.cos(startLat)) * (math.cos(endLat)) * (math.sin(deltaLong/2)**2)
    interValueTwo = 2 * math.atan2(math.sqrt(interValueOne), math.sqrt(1-interValueOne))
    dist = earthRad * interValueTwo
    return(dist/100)

def fareReductionFormula(dist,fare)->float: #Cauculates what the fare is reduced to based on the total distance traveled 
    return(fare-(1/(0.4+math.e**(3-dist))))