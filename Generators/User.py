from Generators import UserGenerator
from GeneralUser import HasteUser
from os.path import join as path_join


class User:
    def __init__(self):
        self.name = None
        self.username = None
        self.email = None
        self.password = None

    def generate_user(self, email_generator):
        self.name = UserGenerator.generate_name()
        self.username = UserGenerator.generate_username()
        self.password = UserGenerator.generate_password()
        self.email = email_generator.generate_email()

        return HasteUser(self.name, self.email, self.username, self.password)

    def create_user_file(self, path, file_name):
        with open(file_name, 'w') as user_file:
            user_file.write("Name : " + str(self.name) + '\n')
            user_file.write("Username : " + str(self.username) + '\n')
            user_file.write("Password : " + str(self.password) + '\n')
            user_file.write("Email : " + str(self.email) + '\n')
