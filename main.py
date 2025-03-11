# Sample item inventory with six-digit IDs
items = {
    100001: {"name": "Soft & Juicy Dried Mango", "price": 10.99, "stock": 5},
    100002: {"name": "Mandarin Orange Chicken", "price": 12.99, "stock": 0},
    100003: {"name": "Sparkling Strawberry Juice", "price": 8.99, "stock": 10},
}

# Admin credentials
admin_username = "admin"
admin_password = "$3CR3T_P455W0RD"

def display_items():
    print("\nAvailable Items:")
    for item_id, item in items.items():
        status = "In Stock" if item["stock"] > 0 else "Out of Stock"
        print(f"ID: {item_id:06d}, Name: {item['name']}, Price: ${item['price']:.2f}, Status: {status}")

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
    print('6. Common Q/A')
    print('7. Exit Chatbot')
    
    # Get user choice with error handling
    choice = input('Enter number of choice: ')
    try:
        if choice == '1':
            display_items()
        elif choice == '2':
            print('The store is open from Monday to Saturday, 9 AM to 9 PM.')
        elif choice == '3':
            print("\nOut of Stock Items:")
            out_of_stock_items = [item for item in items.values() if item["stock"] == 0]
            if out_of_stock_items:
                for item in out_of_stock_items:
                    print(f"Name: {item['name']}, Price: ${item['price']:.2f}")
            else:
                print("All items are in stock.")
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
                        item_id = int(input("Enter new item ID (6 digits): "))
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
            print("Q: What is Trader Moe’s?")
            print("A: Trader Moe’s is a specialty grocery store offering high-quality, unique, and affordable food products.\n")
            print("Q: Do you carry vegan or gluten-free options?")
            print("A: Absolutely! We offer a variety of plant-based, dairy-free, gluten-free, and allergen-friendly products.\n")
            print("Q: Does Trader Moe’s offer online shopping or delivery?")
            print("A: Currently, we are an in-store shopping experience, but select locations offer delivery through third-party services.\n")
            print("Q: What is Trader Moe’s return policy?")
            print("A: We have a no-questions-asked return policy! If you’re unsatisfied with a product, bring it back for a full refund or exchange.\n")
        elif choice == '7':
            print('Thanks for using the chatbot!')
            break
        else:
            raise ValueError("Invalid choice")  # Raise an error for invalid choice
    except ValueError as e:
        print(f'Error: {e}. Please enter a valid number.')