class UserAlreadyExistError(Exception):
    def __init__(self, nameUser, email):
        self.nameUser = nameUser
        self.email = email

    def __str__(self):
        return f'Ja existe um usuario usando estas credenciais:\n{self.nameUser}  -  {self.email}'
