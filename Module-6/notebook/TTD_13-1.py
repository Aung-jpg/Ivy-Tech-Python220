from datetime import datetime
today = datetime.today()
with open("today.txt", "w") as file:
    file.write(today.strftime("%m/%d/%Y %H:%M:%S"))
