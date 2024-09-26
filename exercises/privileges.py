# Упражнение 9.8

class Privileges():

    def __init__(self):
        self.privileges = ['разрешено добавлять сообщения', 'разрешено добавлять пользователя', 'разрешено блокировать действия пользователя']

    def show_privileges(self):
        print(f"Пользователь имеет следующие полномочия: \n* {self.privileges[0]}\n* {self.privileges[1]}\n* {self.privileges[2]}")