import math

def DMStoDD(degree,min,sec):
    return(degree+(min/60)+(sec/3600))

def haversineFormulae(startLat, startLong, endLat, endLong):
    deltaLat = endLat - startLat
    deltaLong = endLong - startLong
    a = (math.sin(deltaLat/2)**2) + (math.cos(startLat)) * (math.cos(endLat)) * (math.sin(deltaLong/2)**2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = 6378 * c
    return(d/100)

def fareReductionFormula(dist,fare):
    return(1/(0.4+fare**(3-dist)))

def main()->None:
    print("hehehehe")
    latDegree = 51 #int(input("What is the lattitude's degrees? "))
    latMin = 2 #int(input("What is the lattitude's minutes? "))
    latSec =  40.445 #float(input("What is the lattitude's secconds? (to three decimals)"))

    longDegree = 114 #int(input("What is the longitude degrees? "))
    longMin = 2 #int(input("What is the longitude minutes? "))
    longsec =  39.106 #float(input("What is the longitude secconds? (to three decimals)"))

    destLat = 51.1376194
    destLong = 114.13369889

    fare = 3.8

    totalDist = haversineFormulae(DMStoDD(latDegree,latMin,latSec),DMStoDD(longDegree,longMin,longsec),destLat,destLong)
    fareReducted = fareReductionFormula(totalDist,fare)

    print(f"Travelling from user's starting location (at {latDegree}° {latMin}' {latSec}\" North, {longDegree}° {longMin}' {longsec}\" West) to the Homage statue on MRU campus,\nThe distance is approximately {round(totalDist,1)} km.\nTheir fare would be reduced to ${round(fareReducted,2)}.")

main()