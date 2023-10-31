# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used
# to store collections of data, the other 3 are Tuple, Set, and Dictionary
# Lists are created using square brackets
# List items are ordered, changeable, and allow duplicate values.
# A list can contain different data types:

fruits = ["apple", "banana", "cherry"]
print(fruits[1])

fruits[1] = "grapes"
print(fruits)

fruits.append("orange")
print(fruits)

# fruits.append("Mango" , "Pineapple" , "Watermelon")   cannot enter more than one
# fruits.append(["Mango" , "Pineapple" , "Watermelon"]) will create a sub list inside the list fruits
fruits.extend(["Mango", "Pineapple", "Watermelon"])
print(fruits)

