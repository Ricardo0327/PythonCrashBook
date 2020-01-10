class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can be user']

    def show_privileges(self):
        print(self.privileges[0])
        print(self.privileges[1])
        print(self.privileges[2])
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("The user name is "+self.last_name+" "+self.first_name)

    def greet_user(self):
        print("Hello,"+self.last_name+" "+self.first_name)

class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privilege=Privileges()

admin=Admin('ming','lu')
admin.privilege.show_privileges()