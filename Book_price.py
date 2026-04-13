num_books = int(input("Enter the number of books required: "))

if num_books <= 0:
    print("Please enter a valid number of books")

elif 1 <= num_books <= 5:
    price = 20

elif 6 <= num_books <= 9:
    price = 15

else:  # 10 or more
    price = 12

# Only calculate if valid
if num_books > 0:
    total_price = num_books * price
    print(f"Price per book: £{price}")
    print(f"Total cost: £{total_price}")