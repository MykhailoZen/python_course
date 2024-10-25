fruits = ['apple', 'banana', 'cherry', 'potato']
colors = ('white', 'black', 'gray')
numbers = set(range(1, 4))
mydict = {
    "Vasyl": 43,
    "Iryna": 18,
    "Mariia": 26,
    "Petro": 19
}

print(f"Initial 'fruits' list: {fruits}")
fruits.append('grape')
print(f"'fruits' list after adding grape to the end of it: {fruits} ")
fruits.remove('potato')
print(f"'fruits' list after removing potato from it: {fruits}")
if 'apple' in fruits:
    print("'apple' is in 'fruits' list")
print(f"The length of colors tuple is: {len(colors)}, the colors in tuple are: {colors}")
print(f"Initial 'numbers' set is: {numbers}")
numbers.add(4)
print(f"'numbers' set after adding 4 : {numbers}")
print(f"The initial dictionary is: {mydict}")
mydict.update({"Yuliia": 23})
print(f"Dictionary after adding new person {mydict}")
