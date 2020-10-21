def my_sum(*args):
    total = 0
    for item in args:
        total += item
    print(total)


my_sum(4, 5, 6)
my_sum(*[1, 2, 3], *[4, 5, 6])


def dictionary(**kwargs):
    for arg in kwargs.values():
        print(arg)


dictionary(a="hello", b="world")
