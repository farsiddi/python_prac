watch = 20


def watch_count():
    watch = 12
    print(watch)


watch_count()
print(watch)


# Local Scope
def smartphone():
    count = 2
    print(count)


smartphone()
# print(count) Gives error => unresolved error => only available inside the function

#   Global Scope => Available within the function and outside also

#   There is nothing like block scope

cities_visited = 3
if cities_visited < 5:
    cities_visited = 99

print(cities_visited)

#   Modifying global variable
shoes = 4


def shoe_count():
    global shoes
    shoes += 1
    print(shoes)


shoe_count()
print(shoes)

#   Global Constants
PI = 3.141