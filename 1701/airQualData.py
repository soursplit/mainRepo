#
# COMP 1701 Fall 2025 Assignment 2
#
# Nelson Wing
#
'''
Airdrie
141
Ardrossan
53
Banff South of Bow River
46
Brooks Meadowplace
142
Calgary Varsity
153
Caroline
136
Cold Lake South
52
Conklin Community 
55
Cougar Point Road, Canmore
23
Drayton Valley
73
'''
def add()->None:
        locations.append(str(input("Enter location name to add: ")))
        AQI.append(int(input("Enter coresponding AQI to location: ")))
def main()->None:
    locations = ["Airdrie","Ardrossan","Banff South of Bow River","Brooks Meadowplace","Calgary Varsity","Caroline","Cold Lake South","Conklin Community","Cougar Point Road, Canmore","Drayton Valley"]
    AQI = [141,53,46,142,153,136,52,55,23,73]
    #for x in range(10):
        #locations.append(str(input("Enter location name: ")))
        #AQI.append(int(input("Enter coresponding AQI to location: ")))
    for x in range(len(locations)):
        print(locations[x],AQI[x])

main()