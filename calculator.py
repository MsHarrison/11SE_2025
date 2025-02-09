# calculator program
# Year 11 SE class
# demonstrating how structure charts reflect subprograms

def addNum( number1, number2):
    result = number1 + number2
    return result

def subNum( number1, number2):
    result = number1 - number2
    return result

def multNum( number1, number2):
    result = number1 * number2
    return result

def divNum( number1, number2):
    result = number1 / number2
    return result

quit = False

while quit == False:
    getNumber1 = int(input("Enter the first number: "))
    getNumber2 = int(input("Enter the second number: "))
    operation = input("Would you like to (a)dd, (s)ubtract, (m)ultiply, (d)ivide or (q)uit? ")
    if operation.lower() == 'a':
        print(addNum(getNumber1, getNumber2))
    elif operation.lower() == 's':
        print(subNum(getNumber1, getNumber2))
    elif operation.lower() == 'm':
        print(multNum(getNumber1, getNumber2))
    elif operation.lower() == 'd':
        if getNumber2 == 0:
            print("Sorry we cannot divide by zero")
        else:
            print(divNum(getNumber1, getNumber2))
    elif operation.lower() == 'q':
        quit = True
    else:
        print("That's not a valid option!")

