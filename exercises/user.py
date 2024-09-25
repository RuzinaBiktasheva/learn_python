# Упражнение 9.3:

class User():

    def __init__(self, first_name, last_name, age, gender, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.country = country

    def describe_user(self):
        print(f"Текущий пользователь имеет следующие данные:\nИмя: {self.first_name.title()}\nФамилия: {self.last_name.title()}\nВозраст: {self.age}\nПол: {self.gender}\nСтрана проживания: {self.country}")

    def greet_user(self):
        print(f"Приветствую, {self.last_name.title()} {self.first_name.title()}!")

one_user = User('ольга', 'павлова', '30', 'женский', 'Россия')
one_user.describe_user()
one_user.greet_user()

two_user = User('max', 'jouhson', '29', 'male', 'USA')
two_user.describe_user()
two_user.greet_user()