from sys import stdin

for line in stdin:
    try:
        data = line.split()
        a = int(data[0])
        b = int(data[1])
        if a > b:
            print(a-b)
        else:
            print(b-a)
    except:
        break