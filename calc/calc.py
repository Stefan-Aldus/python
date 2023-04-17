while True:
    operation = input(
        "Enter *, /, -, or + for operators, or 'exit' to exit the program: ")
    if operation.lower() == 'exit':
        print("You exited the calculator!")
        break
    usernum = input("Your first number is: ")
    usernum2 = input("Your second number is: ")
    if not usernum.isdigit() or not usernum2.isdigit():
        print("Invalid input. Please enter a valid number.")
        continue  # Skip the rest of the loop and prompt the user for input again
    usernum = float(usernum)
    usernum2 = float(usernum2)
    if operation == '*':
        result = usernum * usernum2
    elif operation == '/':
        result = usernum / usernum2
    elif operation == '-':
        result = usernum - usernum2
    elif operation == '+':
        result = usernum + usernum2
    else:
        print("Invalid operator. Please enter *, /, -, or +.")
        continue  # Skip the rest of the loop and prompt the user for input again
    print("The result of %s %s %s: %s" %
          (usernum, operation, usernum2, result))
