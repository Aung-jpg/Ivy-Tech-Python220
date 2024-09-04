"""
Aung Aung
program that checks if a year is a leap year
"""

while True:
    year = input("What year is it ('zzz' to quit): ")
    if year.lower() == "zzz":
        break

    year = float(year)

    no = "Not a leap year"
    yes = "Leap year"

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(yes)
            else:
                print(no)
        else:
            print(yes)
    else:
        print(no)
    