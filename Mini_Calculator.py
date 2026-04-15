def calculator():
    history = []   # history of your calculation
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
            
            # save your calculation 
            calculation = f"{num_1} {operator} {num_2} = {result}"
            history.append(calculation)
            
        except ValueError:
            print("Invalid input! Please enter numbers only.")

        # ask user to show history
        history_choice = input("Do you want to see your calculation history? (y/n)").lower()
        if history_choice == "y" :
            print(history)
            
        # Exit option
        choice = input("Do you want to continue? (y/n): ").lower()
        if choice != "y":
            print("Calculator stopped.")
            break


calculator()


