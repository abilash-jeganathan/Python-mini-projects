import random

print(f'{"Number Guessing Game":*^100}')
print('Welcome to the Number Guessing Game!')
print('1.Start Game')
print('2.Score')
print('3.Exit')
score = 0
while True:
    choice = input('Enter your choice (1-3): ')
    if choice == '1':
        number_to_guess = random.randint(1, 100)
        attempts = 0
        while True:
            try:
                guess = int(input('Guess a number between 1 and 100: '))
                attempts += 1
                if guess < number_to_guess:
                    print('Too low! Try again.')
                elif guess > number_to_guess:
                    print('Too high! Try again.')
                else:
                    print(f'Congratulations! You guessed the number in {attempts} attempts.')
                    score += 10 - attempts  # Score based on attempts
                    break
            except Exception as e:
                print(e)
    elif choice == '2':
        print(f'Your current score is: {score}')
    elif choice == '3':
        print('Thank you for playing! Goodbye!')
        break
    else:
        print('Invalid choice. Please enter a number between 1 and 3.')
