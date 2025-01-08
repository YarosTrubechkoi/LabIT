class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def set_password(self, new_password):
        hash(self.password) == hash(new_password)
        print('Пароль был изменён.')

    def check_password(self, password):
        if hash(self.password)==hash(password):
            print(True)
        else:
            print(False)
    

    def get_info(self):
        print(f"{self.username}.  {self.email}.  {self.password}")


Nik = UserAccount('Nick', 'acdc@mail.ru', 'Postavte zachet')
Nik.set_password('Okey')
Np=input('Введите пароль:')
Nik.check_password(Np)