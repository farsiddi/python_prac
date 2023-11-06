#  object = Class() => Name of class Pascal Case
# Attribute is a variable associated with an object
#   Constructor - __init__
class User:
    def __init__(self, user_id, user_name):  # Self is the object that is initialized
        print("A user is created")  # Every a new user is created this statement will be called
        self.id = user_id
        self.username = user_name
        self.locat = "Bangalore"  # Giving default values
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1


user_1 = User(2, "Faran")
user_2 = User(3, "Rohan")

# user_1.id = "0001"
print(user_1.locat)
print(user_2.locat)
user_2.locat = "Pune" # We can change the default value further in the code
print(user_2.locat)

user_1.follow(user_2)
print(user_1.following)

def my_func():
    pass


# print(user_1.id)
