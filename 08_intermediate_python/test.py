import functools

customers = ["Andrew Yang", "Yang Zhi Siang"]


def validation(func):
    functools.wraps(func)

    def wrapper_validation(*args, **kwargs):
        print("Logging in ...")
        result = func(*args, **kwargs)
        if result:
            print("Logged in!")
        else:
            print("Please sign up first!")

    return wrapper_validation


@validation
def login(name):
    if name in customers:
        return True
    return False


login("Andrew Yang")
