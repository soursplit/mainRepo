num = input()
line = input()
data = line.split()
out = 0
for x in range(len(data)):
    data[x] = int(data[x])
for y in data:
    if y < 0:
        out += 1
print(out)