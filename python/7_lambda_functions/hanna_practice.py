# List comprehensions

list_hanna = ['Alex', 'Hanna', 'Ksu', 'Olha', 'Inna', 'Helen']

list_new = []
for i in list_hanna:
    if 'a' not in i and 'A' not in i:
        list_new.append(i)
print(list_new)

list_new1 = [i for i in list_hanna if 'a' not in i and 'A' not in i]
print(list_new1)

list_hannochka = [7, 3, 15, 4, 27, 6, 8, 9]
list_2 = []
for i in list_hannochka:
    if i % 3 == 0:
        list_2.append(i)
print(list_2)

list_comp = [i for i in list_hannochka if i % 3 == 0]
print(list_comp)

new_string = 'I love Hanna and Inna'
print(len([i for i in new_string if 'a' == i]))

# 10-50
print([i * 3 for i in range(10, 51) if i % 2 != 0])

# Dict comprehensions

d = {'anna': 45, 'masha': 44, 'alina': 33, 'vasja': 11}

print({key.capitalize(): value - 9 for key, value in d.items()})

d_2 = {'anna': 45, 'masha': 44, 'ksu': 33, 'vasja': 11, 'murlo': 66}

print({key.capitalize(): value - 9 for key, value in d_2.items() if 'a' not in key})

# Set comprehensions

list_numbers = [2, 7, 4, 2, 9, 2, 4, 16]
print({i for i in list_numbers if i %2 == 0})

worlds = ['alisa', 'anna', 'ksunja', 'anna', 'denis', 'voitek']
print({i.capitalize() for i in worlds if 'a' in i })

