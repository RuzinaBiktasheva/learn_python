# Упражнение 9.3:

class User():

    def __init__(self, first_name, last_name, age, gender, country, login_attempts = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.country = country
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"Текущий пользователь имеет следующие данные:\nИмя: {self.first_name.title()}\nФамилия: {self.last_name.title()}\nВозраст: {self.age}\nПол: {self.gender}\nСтрана проживания: {self.country}")

    def greet_user(self):
        print(f"Приветствую, {self.last_name.title()} {self.first_name.title()}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attepts(self):
        self.login_attempts = 0

one_user = User('ольга', 'павлова', '30', 'женский', 'Россия')
one_user.describe_user()
one_user.greet_user()

two_user = User('max', 'jouhson', '29', 'male', 'USA')
two_user.describe_user()
two_user.greet_user()

three_user = User('Сара', 'Пулман', '45', 'женский', 'Израиль')
three_user.increment_login_attempts()
three_user.increment_login_attempts()
three_user.increment_login_attempts()
print(three_user.login_attempts)
three_user.reset_login_attepts()
print(three_user.login_attempts)