# By default, all the functions returns none
# "*" is used to take any number of argument
# "**" is used for unpacking
def hello():
    print("Hello")


# hello()


def users_ages_in_seconds():
    users_age = int(input("Enter your age"))
    age_seconds = users_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}")


# users_ages_in_seconds()

def add(x, y):
    print(x + y)
    return x + y


# add(2, 3)
# result = add(3, 4)

sub = lambda x, y: x - y


# print(sub(21, 3))

def double(x):
    return x * 2


sequence = [2, 4, 6, 8]
# doubled = [double(x) for x in sequence]  # In function, we can use large mathematical operation
doubled = map(double, sequence)  # does the same thing as above


# print(list(doubled))
# print(tuple(doubled)) Gives empty list becauseAfter the first print(list(doubled)), the doubled iterator is
# exhausted because it has been fully consumed to create the list. When you try to print tuple(doubled) immediately
# afterward, it starts from the exhausted state, and there are no remaining elements, resulting in an empty tuple.
# use lambda and map together

def multiple(*args):
    total = 1
    for arg in args:
        total = total * arg
    print(total)


# multiple(1, 2, 3, 4, 5, 6)


def addition(*args):
    total = 0
    for arg in args:
        total += arg
    return total


# nums = {"x": 7, "y": 21}
# print(addition(**nums))

def calculator(*args, operator):
    if operator == "+":
        return addition(*args)


# print(calculator(2, 3, 5, operator="+"))  # "operator" is necessary otherwise "+" will be carried by *args

def named(**kwargs):
    print(kwargs)


# named(name="Farhan", age=22)
details = {"name": "Farhan", "ages": 22}


# named(**details)


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg} : {value}")


# print_nicely(name="Bob", age=25)
print_nicely(**details)
