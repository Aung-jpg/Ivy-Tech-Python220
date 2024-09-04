"""
Aung Aung
program that takes student scores as input and returns a grade
"""

while True:
    score = input("what is your score out of 100 ('zzz' to quit): ")
    if score.lower() == "zzz":
        break

    score = float(score)

    if score >= 90:
        print("You got an A")
    elif score >= 80 and score <= 89:
        print("You got a B")
    elif score >= 70 and score <= 79:
        print("You got a C")
    elif score >= 60 and score <= 69:
        print("You got a D")
    elif score < 60:
        print("You got an F")