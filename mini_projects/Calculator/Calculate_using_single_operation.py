# This code initiates the operation you want to perform at first and continue untill the user quita

def add (a,b):
    return  a + b
def subract (a,b):
    return  a - b
def multiply (a,b):
    return  a * b
def divide (a,b):
    quotient = a / b
    remainder = a % b
    return quotient,remainder

operations = {"+": add, "-" : subract,"*" : multiply, "/" : divide}
# print(operations)

calc = input("Enter + for addition, - for subraction, * for multiplication, / for division ")
# print(operations[calc](3,4))

should_continue = True
while should_continue == True:

    #print(operator)
    c, d = int(input("Enter the first number: ")), int(input("Enter the second number: "))
    perform = operations[calc](c,d)
    print(perform)

    user_input = input('Type "Y" to continue\n"N" to quit: ')

    if user_input == "Y":
        should_continue = True
    else:
        should_continue = False