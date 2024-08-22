def calculator():
    print("Simple Calculator")
    print("Options: [1] Add [2] Subtract [3] Multiply [4] Divide [5] Exit")

    while True:
        choice = input("Choose an option: ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 != 0:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
                else:
                    print("Error! Division by zero.")
        elif choice == '5':
            print("Exiting calculator.")
            break
        else:
            print("Invalid choice, please try again.")

calculator()
