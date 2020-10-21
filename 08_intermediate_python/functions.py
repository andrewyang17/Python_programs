def say_hello(name):
    print(f"Hello {name}")


def be_awesome(name):
    print(f"Yo {name}, together we are the awesomest!")


# first class function, can be accessed in list and dictionary
function_in_list = [say_hello, be_awesome]
function_in_list[0]("Andrew")
function_in_list[1]("Yang")

function_in_dictionary = {1: say_hello, 2: be_awesome}
function_in_dictionary[1]("Andrew")
function_in_dictionary[2]("Yang")


# function takes function as argument
def greet_yang(greeter_func):
    return greeter_func("Yang")


greet_yang(say_hello)
greet_yang(be_awesome)


# function has child, inner function
# returning function from function
def parent(num):
    def first_child():
        print("Hi I am first child")

    def second_child():
        print("Hi I am second child")

    if num == 1:
        return first_child
    else:
        return second_child


test = parent(2)
test()
