input1 = input()
num = input1.split(';')
final = 0
for x in num:
    try:
        sp = x.split('-')
        for y in range(int(sp[0]),int(sp[1])+1):
            final +=1
    except:
        final +=1
print(final)