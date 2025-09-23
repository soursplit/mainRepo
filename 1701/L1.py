#
# COMP 1701 Fall 2025 Lab 1
#
# Nelson Wing
# Sep 11, 2025
#
#

print("""Nelson Wing
Cat
2004""")

print("Nelson Wing","Cat","2004\n")

print("'Comp 1701 is \"Fun!\"'")

print( "Hello, \n\"World\". \n\tT\'s a great day to learn about the\t\t\\.")
print()

name = "Nelson Wing"
favAnimal = "Cat"
favYear = "2004"
hehe = (name,favAnimal,favYear)
for x in hehe:
    print(x)
    print(type(x))

print("Name:", name)
print("Variable name has type:", type(name))