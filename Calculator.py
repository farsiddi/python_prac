def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("Enter the first number: "))
    for symbol in operation:
        print(symbol)
    next_calc = True

    while next_calc:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("Enter the next number: "))
        calculation_function = operation[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(
                f"Type 'yes' to continue calculating with {answer}, or type 'no' to start a new calculation: ") == "yes":
            num1 = answer
        else:
            next_calc = False
            calculator()


calculator()
