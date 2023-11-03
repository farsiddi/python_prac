#   Functions with output
first_name = input("Enter your first name:\n")
last_name = input("Enter your last name:\n")


def upper(f_name, l_name):
    f_name = first_name.title()
    l_name = last_name.title()
    # print(f"{f_name} {last_name}")
    return f"{f_name} {last_name}"


# upper(first_name, last_name)
print(upper(first_name, last_name))
