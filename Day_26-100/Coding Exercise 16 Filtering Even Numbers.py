list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers_to_int = [int(i) for i in list_of_strings]
even_numbers = [i for i in numbers_to_int if i % 2 == 0]
print(even_numbers)