from os.path import devnull

mylist = [9,8,7,6,5,4,3,2,1,0]
new_list = [x for x in mylist]
new_list2 = [x for x in range(1,11) if x % 2 == 0]
new_list3 = lambda x:

print(f"1. Copy of the list: {new_list}")
print(f"2. List of only the even numbers in range(1,11): {new_list2}")