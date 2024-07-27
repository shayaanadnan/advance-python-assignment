from functools import reduce

numbers = [2, 4, 6, 8, 10]
doubled_numbers = list(map(lambda x: x * 2, numbers))
product = reduce(lambda x, y: x * y, doubled_numbers)
print("Doubled numbers:", doubled_numbers)
print("Product of doubled numbers:", product)
