
import functools


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("before")
        func(*args, **kwargs)
        print("after")

    return wrapper


@my_decorator
def say_something(name, something):
    print(f"{name} says {something}!")


say_something("Andrew Yang", "fuck you")


@my_decorator
def say_nothing():
    print("Say nothing")


say_nothing()



