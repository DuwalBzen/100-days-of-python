
class User:

    def __init__(self, user_id, username):
        # initialise
        print("new user being created...")
        self.id = user_id
        self.username = username
        # Default value
        self.followers = 0
        self.following = 0

    """
    Self -> Is a way for us to refer to a object
          that gonna be created from the class 
          inside the class blueprint
    follow(self) When this method is called,
    it knows the object that called it
    """

    def follow(self, user):
        user.followers += 1
        self.following += 1





adom = User(0, "Adom")
user_2 = User(1, "Selena")


print(adom.username)
adom.follow(user_2)
print(adom.following)

print(user_2.username)
print(user_2.followers)

