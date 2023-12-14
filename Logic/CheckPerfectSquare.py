def isPerfectSquare(num):
    sqrt_num = int(num ** 0.5)

    return sqrt_num ** 2 == num


number = 32
result = isPerfectSquare(number)
print(f"{number} is a perfect square: {result}")
