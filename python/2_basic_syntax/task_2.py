# 1) Define two variables, "length" and "width," and give them the values representing the rectangle's length and width.
# 2) Compute the area of the rectangle by multiplying the values stored in the "length" and "width" variables.
# 3) Print the calculated area.

length = 12.5
width = 14.3

print(f" Area of rectangle: {length * width}")

# write a function that will count how many pieces of each vegetable are in the bag
# input: ['potato', 'carrot', 'potato', 'tomato', 'paprika', 'paprika', 'potato', 'carrot']
# exptected output:
# potato: 3
# carrot: 2
# tomato: 1
# paprika: 2

def veg_count(bag):
    for x in set(bag):
        print(f"{x} in present in the {bag.count[x]}")

bag = ['potato', 'carrot', 'potato', 'tomato', 'paprika', 'paprika', 'potato', 'carrot']

veg_count(bag)

