def addition(num1, num2):
    result = num1 + num2
    print("{0}+{1}={2}".format(num1, num2, result))

def subtract(num1, num2):
    result = num1 - num2
    print("{0}-{1}={2}".format(num1, num2, result))

def multiplication(num1, num2):
    result = num1 * num2
    print("{0}*{1}={2}".format(num1, num2, result))

def division(num1, num2):
    if num2 == 0.0:
        print("Can't divide by 0")
    else:
        result = num1 / num2
        print("{0}/{1}={2}".format(num1, num2, result))

while True:
    print("What do you want to do")
    print("1: ADDITION")
    print("2: SUBTRACTION")
    print("3: MULTIPLICATION")
    print("4: DIVISION")
    print("Enter Q to exit")

    choice = input("Enter your choice: ")
    if choice == 'Q' or choice =='q':
        break

    num1 = float(input("Enter the number 1: "))
    num2 = float(input("Enter the number 2: "))

    if choice == '1':
        addition(num1, num2)
    elif choice == '2':
        subtract(num1, num2)
    elif choice == '3':
        multiplication(num1, num2)
    elif choice == '4':
        division(num1, num2)
    else:
        print("You have entered an invalid choice")
    print("\n")
