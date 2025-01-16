print('Hello, I am your friendly Trader Moe\'s Chatbot')
name = input('What is your name user? ')
age = int(input(f'Nice to meet you, {name}, how old are you?'))
if(age < 18):
    print('Aren\'t you a little young to be shopping?')
elif(age < 55):
    print('Thanks for the information!')
elif(age < 120):
    print('Good to know! You will be enjoying our senior discounts!')
else:
    print('Wow, you are quiet the relic!')

while(True):
    print()
    print('How can I help you?')
    print('1. In-stock Items')
    print('2. Days store is open')
    print('3. Check Out of Stock Items')
    print('4. Exit Chatbot')
    choice = input('Enter number of choice: ')
    if(choice == '1'):
        print('To be implemented')
    elif(choice == '2'):
        print('To be implemented')
    elif(choice == '3'):
        print('To be implemented')
    elif(choice == '4'):
        print('Thanks for using chatbot!')
        break
    else:
        print('Error: Please enter a valid number')