lst_strings = ['apple', 'banana', 'cherry', 'date', 'elderberry']
new_strings = list(filter(lambda x: len(x) > 5, lst_strings))
print(new_strings)