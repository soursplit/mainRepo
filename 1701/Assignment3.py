import csv
def main()->None:
    rawrrr = []
    with open('sightings.csv', mode = 'r') as file:
        for lines in file:
            lines = lines.replace("\n","")
            rawrrr.append(lines.split(','))
    print(rawrrr)
    print("----------------------------------------")
    for x in rawrrr:
        if rawrrr.index(x) == 1:
            print("----------------------------------------")
        print(f"{x[0]:<11}{x[1]:<12}{x[2]:<6}{x[3]}")
    print("----------------------------------------")
main()