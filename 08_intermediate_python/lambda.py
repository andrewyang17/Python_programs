names = ["Andrew Yang", "Yang Zhi Siang", "Ah Yang", "Ah Siang"]
names.sort(key=lambda x: x.split()[-1].lower())
print(names)


# fliter allows quick creation of iterables of items in another iterable passes a test
nums = list(range(1, 21))
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)


# map return an iterator that applies function to every item of iterable, yield the results
nums = list(range(1, 11))
sq_nums = list(map(lambda x: x**2, nums))
even = list(map(lambda x: x % 2 == 0, nums))
print(sq_nums)
print(even)


# reduce allows cumulative application of a function to every element of an iterable
from functools import reduce
nums = list(range(1, 11))
total = reduce(lambda x, y: x + y, nums)
print(total)
