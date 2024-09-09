def add(a, b):
    return a + b


def subract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    # quotient = a / b
    # remainder = a % b
    # return quotient, remainder
    return a / b


operations = {"+": add, "-": subract, "*": multiply, "/": divide}

# print(operations)
# calc = input("Enter + for addition, - for subraction, * for multiplication, / for division ")
# print(operations[calc](3,4))

result = None
should_continue = True
while should_continue:
    if result is not None:
        c = result
        d = int(input("Enter the second number: "))
        calc = input("Enter + for addition, - for subraction, * for multiplication, / for division ")

        perform = operations[calc](c, d)
        print(perform)
        result = perform
        user_input = input('Type "Y" to continue\n"N" to quit: ')
        if user_input == "Y":
            should_continue = True
        else:
            should_continue = False
    else:
        # print(operator)
        c = int(input("Enter a number: "))
        d = int(input("Enter another number: "))

        calc = input("Enter + for addition, - for subraction, * for multiplication, / for division ")
        perform = operations[calc](c, d)
        print(perform)
        print(f"{c}{" "}{calc}{" "}{d} {"="} {perform}")
        result = perform
        user_input = input('Type "Y" to continue\n"N" to quit: ')
        if user_input == "Y":
            should_continue = True
        else:
            should_continue = False
