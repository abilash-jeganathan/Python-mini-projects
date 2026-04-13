def calculate_book_cost():
    try :
        # Take input from user
        num_book = int(input('Enter the number of bokks required:'))

        # Check for valid input
        if num_book <= 0 :
            print('Please enter a valid number of books(0<)')

        else:
            # Decide price per book based on quantity
            if 1 <= num_book <= 5 :
                price = 20
            elif 6 <= num_book <= 9 :
                price = 15 
            else:  # 10 or more
                price = 12

        # Calculate total cost 
        total_price = num_book * price

        # Display total price for the user
        print(f'price per book:£{price}')  
        print(f'total cost:£{total_price}') 


    # Non-integer input errors
    except ValueError :
        print('Invalid input! Please enter a whole number only')

calculate_book_cost()        
