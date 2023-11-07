# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
my_tuple = (1, 2, 3, "faran", 87.3)
for i in my_tuple:
    print(i)
    print(type(i))

# Converting a tuple into a list
my_list = list(my_tuple)
for i in my_list:
    print(i)