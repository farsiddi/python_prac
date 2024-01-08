list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = int(input("Enter the nth index")) - 1
list1.sort()
print(list1[n])

#   numbers.sort(reverse=True)

# Sorting an array

l1 = [76, 23, 45, 12, 54, 9]
print("Original List:", l1)

for i in range(0, len(l1)):
    for j in range(i + 1, len(l1)):
        if l1[i] >= l1[j]:
            l1[i], l1[j] = l1[j], l1[i]

# sorted list
print("Sorted List", l1)