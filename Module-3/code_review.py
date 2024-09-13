class User:
    def __init__(self, first_name: str, last_name: str, gender: str, favorite_color: str):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.gender = gender
        self.favorite_color = favorite_color

    def describe_user(self):
        return f"{self.first_name} {self.last_name} is {self.gender} and likes the color {self.favorite_color}"

    def greet_user(self):
        return f"Hi {self.first_name}!"

people = []
aung = User("aung", "aung", "male", "red")
people.append(aung)
jackson = User("jackson", "ball", "male", "yellow")
people.append(jackson)
luis = User("luis", "v-r", "male", "baby blue")
people.append(luis)
obeth = User("obeth", "cruze", "male", "green")
people.append(obeth)
logan = User("logan", "ghast", "male", "purple")
people.append(logan)

for i in people:
    print(i.describe_user())
    print(i.greet_user())

