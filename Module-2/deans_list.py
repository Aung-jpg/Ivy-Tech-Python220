"""
Aung Aung
Dean's List/Honor Roll Tracker
This app will check if you made Dean's List or Honor Roll, it will constantly ask for inputs until you quit
"""
last_name = "Joe"
if last_name.upper() == "XXX":
    quit()

first_name = "Joe"
gpa = 3.3
if gpa > 3.25:
    print(f"{first_name} {last_name} made Honor Roll.")
    if gpa >= 3.5:
        print(f"{first_name} {last_name} made Dean's List.")
else:
    print("Try again next time aka git gud")