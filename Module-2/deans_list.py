"""
Aung Aung
Dean's List/Honor Roll Tracker
This app will check if you made Dean's List or Honor Roll, it will constantly ask for inputs until you quit
"""

while True:
    student_last_name = input("What is your name last name ('ZZZ' to quit): ")
    if student_last_name.lower() == "zzz":
        break
    student_first_name = input("What is your name first name: ")
    while True:
        try:
            student_gpa = float(input("What is your gpa (type a float/int): "))
        except ValueError:
            print("That's not a number stupid")
            continue
        break
    if student_gpa >= 3.5:
        print("Congrats you made Dean's List")
    # I don't know if you can make both Dean's list and Honor Roll
    elif student_gpa >= 3.25:
        print("Congrats you made Honor Roll")
    else:
        print("you didn't make anything")
    