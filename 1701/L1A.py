#
# COMP 1701 Fall 2025 Lab 1A
#
# Nelson Wing
# Sep 11, 2025
#
#

def main()->None:
    first_name = input("Enter your first name: ")
    favAnimal = input("Enter your favourite animal: ")
    favYear = str(input("Enter your favourite year: "))

    print(f"Name:{first_name:>25}\n"+f"Favourite Animal:{favAnimal:>10}\n"+f"Favourite Year:{favYear:>13}")

main()

