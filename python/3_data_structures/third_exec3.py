# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become
# positives.
#
# [1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
# [1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
# [] --> []
# You can assume that all values are integers. Do not mutate the input array.

myList =[1, 2, 3, 4, 5]

negativeList = [- element * 2 for element in myList]
print(negativeList)

new_list = [i for i in range(1, 11) if i % 2 == 0]
print(new_list)