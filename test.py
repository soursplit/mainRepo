import math

def fareReductionFormula(dist,fare): #Cauculates what the fare is reduced to based on the total distance traveled 
    print((1/(0.4+math.e**(3-dist))))

distance = 2
tansitfare = 3.80
fareReductionFormula(distance,tansitfare)