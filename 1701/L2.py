#
# COMP 1701 Fall 2025 Lab 2
#
# Nelson Wing
# Sep 16, 2025
#
#

def main()->None:

    #2. Order of operations:
    print(2*(20/4/+1)+5)
    print(4*3/6)
    print(4/6*3)
    print(3*4/6,"\n")

    print(4//6*3)
    print(3*4//6)
    print(7%3)
    print(4+7%3-5)
    print((4+7)%3-5,"\n")

    #3. Working with Variables:
    x=2.5
    y=-1.5
    m=18
    n=4

    print(x+n*y-(x+n)*y)
    print(m//n+m%n)
    print(5*x-n//5)
    print(1-(1-(1-(1-(1-n)))),"\n")

    #4. Translating math to code
    #a+b/(c+d)
    #(x-1)*(y-4)
    #(-b+x)/(2*a)
    #x*(y**2)*z

    #5. Algorithm design
    def incanGold():
        totalGems = int(input("How many total gems were collected?\n"))
        playerGems = 0
        leftGems = 0
        
        playerGems = totalGems//2
        leftGems = totalGems%2
        print("Both players have",playerGems,"\nThe leftover pile has",leftGems,"\n")
    #incanGold()

    #6. Code tracing
    freeze = 32
    boil = 212
    freeze = 0
    boil = 100
    print(freeze)
    print(boil)

    doughnuts = 6
    friends = 3
    print("We all get", doughnuts/(friends + 1), "doughnuts.")

    doughnuts = 6
    friends = 3
    total_peeps = friends + 1
    whole_doughnuts = doughnuts // total_peeps
    leftover = doughnuts % total_peeps
    print("We all get", whole_doughnuts, "whole doughnuts!")
    print("There are", leftover, "doughnuts left over.")
    
    beta = 9
    alpha = 3 * beta
    print(alpha, ",", beta)
    alpha = alpha + 1
    print("alpha,beta")
    beta = beta + beta
    print(alpha, ",", beta)

    
main()