# Sample item inventory
items = {
    1: {"name": "Widget A", "price": 10.99, "stock": 5},
    2: {"name": "Widget B", "price": 12.99, "stock": 0},
    3: {"name": "Widget C", "price": 8.99, "stock": 10},
}
# Admin credentials
admin_username = "admin"
admin_password = "password"
def display_items():
    print("\nAvailable Items:")
    for item_id, item in items.items():
        status = "In Stock" if item["stock"] > 0 else "Out of Stock"
        print(f"ID: {item_id}, Name: {item['name']}, Price: ${item['price']}, Status: {status}")
def return_item():
    item_id = int(input("Enter the ID of the item you want to return: "))
    if item_id in items:
        items[item_id]["stock"] += 1  # Increase stock for returned item
        print(f"You have successfully returned {items[item_id]['name']}.")
    else:
        print("Invalid item ID. Please try again.")
def admin_login():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    return username == admin_username and password == admin_password
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
    print('4. Return an Item')
    print('5. Admin Login')
    print('6. Exit Chatbot')
    # Get user choice with error handling
    choice = input('Enter number of choice: ')
    try:
        if choice == '1':
            display_items()
        elif choice == '2':
            print('To be implemented')
        elif choice == '3':
            print('To be implemented')
        elif choice == '4':
            return_item()
        elif choice == '5':
            if admin_login():
                print("Admin logged in successfully.")
                while True:
                    print("\nAdmin Menu:")
                    print("1. Add Item")
                    print("2. Remove Item")
                    print("3. Logout")
                    admin_choice = input("Enter number of choice: ")
                    if admin_choice == '1':
                        item_id = int(input("Enter new item ID: "))
                        item_name = input("Enter new item name: ")
                        item_price = float(input("Enter new item price: "))
                        item_stock = int(input("Enter initial stock: "))
                        items[item_id] = {"name": item_name, "price": item_price, "stock": item_stock}
                        print(f"Item {item_name} added successfully.")
                    elif admin_choice == '2':
                        item_id = int(input("Enter item ID to remove: "))
                        if item_id in items:
                            del items[item_id]
                            print("Item removed successfully.")
                        else:
                            print("Invalid item ID.")
                    elif admin_choice == '3':
                        print("Admin logged out.")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Invalid admin credentials.")
        elif choice == '6':
            print('Thanks for using the chatbot!')
            break
        else:
            raise ValueError("Invalid choice")  # Raise an error for invalid choice
    except ValueError as e:
        print(f'Error: {e}. Please enter a valid number.')