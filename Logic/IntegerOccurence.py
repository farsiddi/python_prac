# check_array = [1, 3, 4, 6, 7, 3, 9, 11]
# number_check = int(input("Enter the number: "))
# for ()

def countX(lst, x):
    count = 0
    for ele in lst:
        if ele == x:
            count = count + 1
    return count


lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]

target = int(input("Enter the target value: "))

print('{} has occurred {} times'.format(target, countX(lst, target)))
