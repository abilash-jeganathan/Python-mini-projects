def calculator():
    while True:
        try:
            num_1 = float(input("Enter the first number: "))
            num_2 = float(input("Enter the second number: "))
            operator = input("Enter the operator (+, -, *, /): ")

            if operator == "+":
                result = num_1 + num_2

            elif operator == "-":
                result = num_1 - num_2

            elif operator == "*":
                result = num_1 * num_2

            elif operator == "/":
                if num_2 == 0:
                    print("Error: Division by zero is not allowed!")
                    continue
                result = num_1 / num_2

            else:
                print("Invalid operator!")
                continue

            print(f"Result: {result}")

        except ValueError:
            print("Invalid input! Please enter numbers only.")

        # Exit option
        choice = input("Do you want to continue? (y/n): ").lower()
        if choice != "y":
            print("Calculator stopped.")
            break


calculator()


