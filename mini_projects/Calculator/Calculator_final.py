def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

result = None
should_continue = True

while should_continue:
    if result is not None:
        c = result
    else:
        c = int(input("Enter a number: "))

    d = int(input("Enter another number: "))
    calc = input("Enter + for addition, - for subtraction, * for multiplication, / for division: ")

    if calc in operations:
        perform = operations[calc](c,d)
        print(f"{c} {calc} {d} = {perform}")
        result = perform
    else:
        print("Invalid operation")

    user_input = input('Type "Y" to continue or "N" to quit: ').upper()
    should_continue = user_input == "Y"
