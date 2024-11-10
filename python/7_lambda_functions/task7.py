import functools

my_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
my_list2 = [("apple", 50), ("banana", 10), ("cherry", 30)]
my_list3 = [1, 2, 3, 4, 5]
my_list4 = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
my_dict = {'a': 1, 'b': 2, 'c': 3}

new_list = [x for x in my_list]
new_list2 = [x for x in range(1, 11) if x % 2 == 0]
new_list3 = list(filter(lambda x: x % 2 == 0, range(1, 11)))
my_list2.sort(key=lambda x: x[1])
mult_res = functools.reduce(lambda x, y: x * y, my_list3)
new_list4 = [i for x in my_list4 for i in x]
new_dict = {x: y for y, x in my_dict.items()}

if __name__ == '__main__':
    print(f"1. Copy of the list: {new_list}")
    print(f"2. List of only the even numbers in range(1,11): {new_list2}")
    print(f"3. List of only the even numbers in range(1,11) solved with filter() and lambda: {new_list3}")
    print(f"4. List sorted by the number using the lambda function: {my_list2}")
    print(f"5. Multiplication result of all values of the list [1, 2, 3, 4, 5]: {mult_res}")
    print(f"6. Single list of all items from [[5, 4, 7], [8, 9, 6], [7, 2, 4]]: {new_list4}")
    print(f"7. Flipped dictionary: {new_dict}")
