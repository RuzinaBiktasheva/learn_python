from privileges import Privileges

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

class Admin(User):

    def __init__(self, first_name, last_name, age, gender, country, login_attempts = 0):
        super().__init__(first_name, last_name, age, gender, country, login_attempts = 0)
        self.admin_privileges = Privileges()


my_admin = Admin('Андрей', 'Калинин', 34, 'мужской', 'Россия')
my_admin.admin_privileges.show_privileges()