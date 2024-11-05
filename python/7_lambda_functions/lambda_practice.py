from functools import reduce

def filter_num(num):
    if(num % 2) != 0:
        return True
    else:
        return False
numbers = [1, 2, 3, 4, 5, 7, 10, 11, 7]
out_filter = filter(filter_num, numbers)
print("Отфильтрованный список: ", list(out_filter))


out_filter_lambda = filter(lambda x: x % 2 != 0, numbers)
print("Отфильтрованный список: ", set(out_filter_lambda))

out_map = list(map(lambda x: x * 2, numbers))
print(out_map)

out_reduce = reduce((lambda x, y: x + y), numbers)
print(out_reduce)

my_tuples = [(1, 'pear'), (2, 'apple'), (3, 'orange')]
sorted_tuples = sorted(my_tuples, key=lambda x: x[1])
print(sorted_tuples)

sorted_tuples_reverse = sorted(my_tuples, key=lambda x: x[1], reverse=True)
print(sorted_tuples_reverse)