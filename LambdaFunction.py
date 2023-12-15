# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Syntax : lambda arguments : expression

# Using inside the function it will helps
# def myfunc(n):
#   return lambda a : a * n

x = lambda a, b: a * b
print(x(5, 6))
