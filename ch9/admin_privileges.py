from user import User
class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can be user']

    def show_privileges(self):
        print(self.privileges[0])
        print(self.privileges[1])
        print(self.privileges[2])
class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privilege=Privileges()

