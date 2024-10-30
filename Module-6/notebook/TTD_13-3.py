from datetime import datetime
with open("today.txt", "r") as file:
    today_string = file.readline()

today_string = datetime.strptime(today_string, "%m/%d/%Y %H:%M:%S")
today_string.strftime("%m/%d/%Y")
print(today_string)

