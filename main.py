print('Hello, I am your friendly Trader Moe\'s Chatbot')

# Get user name
name = input('What is your name, user? ')

# Get user age with error handling
while True:
    try:
        age = int(input(f'Nice to meet you, {name}, how old are you? '))
        if age < 0:
            print("Age cannot be negative. Please enter a valid age.")
            continue
        break  # Exit the loop if age is valid
    except ValueError:
        print("Invalid input. Please enter a number for your age.")

# Respond based on age
if age < 18:
    print('Aren\'t you a little young to be shopping?')
elif age < 55:
    print('Thanks for the information!')
elif age < 120:
    print('Good to know! You will be enjoying our senior discounts!')
else:
    print('Wow, you are quite the relic!')

# Main loop for chatbot options
while True:
    print()
    print('How can I help you?')
    print('1. In-stock Items')
    print('2. Days store is open')
    print('3. Check Out of Stock Items')
    print('4. Exit Chatbot')

    # Get user choice with error handling
    choice = input('Enter number of choice: ')
    try:
        if choice == '1':
            print('To be implemented')
        elif choice == '2':
            print('To be implemented')
        elif choice == '3':
            print('To be implemented')
        elif choice == '4':
            print('Thanks for using the chatbot!')
            break
        else:
            raise ValueError("Invalid choice")  # Raise an error for invalid choice
    except ValueError as e:
        print(f'Error: {e}. Please enter a valid number.')