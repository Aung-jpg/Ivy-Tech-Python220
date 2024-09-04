"""
Aung Aung
Dean's List/Honor Roll Tracker
This app will check if you made Dean's List or Honor Roll, it will constantly ask for inputs until you quit
"""

while True:
    student_last_name = input("What is your name last name ('ZZZ' to quit): ")
    if student_last_name.lower() == "zzz":
        break

    student_first_name = input("What is your name first name ('ZZZ' to quit): ")
    if student_first_name.lower() == "zzz":
        break

    while True:
        try:
            student_gpa = float(input("What is your gpa (type a float/int): "))
        except ValueError:
            print("That's not a number stupid")
            continue
        break

    if student_gpa >= 3.25:
        print(f"{student_first_name} {student_last_name} made Honor Roll")
        if student_gpa >= 3.5:
            print(f"{student_first_name} {student_last_name} made Dean's List")
    else:
        print(f"{student_first_name} {student_last_name} didn't make anything")
    