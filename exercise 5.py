# Dictionary containing number of months as keys and number of days as values
days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

try:
    # Get the number of the month from the user.
    month = int(input('Enter the number of the month (1-12): '))

    if 1 <= month <= 12:
        # Checking with the user if it is February and asking about leap year 
        if month == 2:
            leap = input('Are you checking for leap year (Yes or No): ').lower()

            if leap == 'yes':
                print('The month has 29 days.')
            else:
                print('The month has 28 days.')
        else:
            # Prints the days for months excluding February
            print(f'The month has {days[month]} days.')
    else:
        print('Please enter a valid number between 1 and 12.')
        
except ValueError:
    print('Please enter a valid number.')

print("**THANK YOU**")
