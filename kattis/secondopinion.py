number = int(input())

secconds = (number % 3600) % 60
minutes = (number % 3600) // 60
hours = number // 3600

print(hours,":", minutes, ":", secconds)