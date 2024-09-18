class Person:
    def __init__(self, first_name: str, last_name: str, age: int, hair_color: str, favorite_number: int) -> None:
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.age = int(age)
        self.hair_color = hair_color
        self.favorite_number = favorite_number

    def __str__(self):
        return (f"first name: {self.first_name}\nlast name: {self.last_name}\nage: {self.age}\nhair_color: {self.hair_color}\nfavorite number: {self.favorite_number}")
    
    def is_over_21(self):
        if self.age >= 21:
            print(f"{self.first_name} is 21 or over")
            return True
        print(f"{self.first_name} is not at least 21")
        return False

people = []
for i in range(3):
    f_name = input("What is your first name: ")
    l_name = input("What is your last name: ")
    age_in_years = input("What is your age: ")
    hair_color = input("What is your hair color: ")
    favorite_number = input("What is your favorite number: ")
    print()
    i = Person(f_name, l_name, age_in_years, hair_color, favorite_number)
    people.append(i)

for person in people:
    print(person)
    person.is_over_21()
    print()

