class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def adv_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@adv_decorator
def create_blog_post(user):
    print(f"The user {user.name} created new blog post")

user = User(name="Angela")
user.is_logged_in = True
create_blog_post(user)

user = User(name="John")
create_blog_post(user)