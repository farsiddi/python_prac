list1 = ["Hello", "Farhan", "Siddiqui"]
tuple1 = ("Hello", "Adams", "Black")
set1 = {"Hello", "Bag"}  # No order
# print(set1)
# print(set1[1])   Not subscript allowed

# set1[1] = "call" No assignment supported
# print(set1)
list1.append("Smith")
# print(list1)
# print(tuple1.index("Adams"))
set1.add("Phone")
set1.add("Charger")
set1.add("Watch")
# print(set1)

set2 = {"Plant", "Watch", "Animal"}
set3 = set1.difference(set2)
# print(set3)  # Omitted the elements of set1 if they are present in set2
# empty set - set()
set4 = set1.union(set2)  # All of them combine
# print(set4)
set5 = set1.intersection(set2)
# print(set5)
# second_list = [12]
# print(second_list)
# tuple2 = (21,)
# print(type(tuple2))


#  Boolean
# print("Alex" == "Farhan")
# print("Farhan" == "Farhan")
# print(12 == 12)

things = ["Carom", "IDCard"]
elements = ["Carom", "IDCard"]
print(things == elements)
print(
    things is elements)  # False because list which itself when created they are created in two different places in the memory

watch = ["Patek", "Rado"]
edt = watch
print(watch is edt)  # true because both lists are created in the same memory spaces
print("------------------")
print("Rado" in watch)
name = "Farhan Siddiqui"
print('F' in name)
