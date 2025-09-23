#
# COMP 1701 Fall 2025 Lab 2A
#
# Nelson Wing
# Sep 16, 2025
#
#

import math

#1. Compund Intrest
def Invest():
    initValue = float(input("What is the initial value of your investment? \n"))
    modValue = initValue
    intRate = float(input("What is the intrest rate?\n"))
    years = int(input("How many years would you like to invest?\n"))
        
    print("An investment of",str(initValue),"at",str(intRate*100),"%","will be worth", str(round(initValue+(initValue*intRate*years),2)),"after",str(years),"years without compunding intrest.\n")
        
    for x in range(years):
        modValue = modValue+(modValue*intRate)
    print("An investment of",str(initValue),"at",str(intRate*100),"%","will be worth", str(round(modValue,2)),"after",str(years),"years with compunding intrest.\n")

#2. Doubling
def Fold():
    thickness = 0.05
    modThickness = thickness
    folds = int(input("How many folds?\n"))
    
    for x in range(folds):
        modThickness = modThickness*2
    print("A paper that is",str(thickness)+"mm","thick, if folded",folds,"times, it would be",str(round(modThickness,2))+"mm","thick or",str(round((modThickness/1000),2))+"M","thick")

#3.Doubling Times
def doublingTime():
    growthRate = int(input("Enter the growth rate in percent:\n"))
    exact = round((math.log(2))/(math.log(1+(growthRate/100))), 2)
    approx = round((math.log(2))/(math.log(1+(growthRate/100))), 0)
    diff = (math.log(2))/(math.log(1+(growthRate/100))) - approx

    print(f"At a growth rate of {growthRate} doubling is approximately {approx} and exactly {exact}\nThe difference is {diff}")

def main()->None:    
    print("hehehehaw")
    
    Invest()
    
    Fold()
    
    doublingTime()

main()