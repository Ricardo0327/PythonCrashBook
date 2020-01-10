class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("The user name is "+self.last_name+" "+self.first_name)

    def greet_user(self):
        print("Hello,"+self.last_name+" "+self.first_name)

user1=User('hong','li')
user2=User('hua','li')
user3=User('ye','wu')
user1.describe_user()
user2.describe_user()
user3.describe_user()
user1.greet_user()
user2.greet_user()
user3.greet_user()

