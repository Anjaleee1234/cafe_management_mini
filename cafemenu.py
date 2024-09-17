menu = {
    'Pizza': 100,
    'Pasta': 70,
    'Burger': 50,
    'Coffee': 30,
    'French fries': 60,
}

print("Welcome to our Restaurant")
print("Pizza: Rs100\nPasta: Rs70\nBurger: Rs50\nCoffee: Rs30\nFrench fries: Rs60")

order_total = 0

# First item input
item_1 = input("Enter the name of the item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1}' has been added to your order.")
else:
    print(f"Ordered item '{item_1}' is not available yet!")

# Ask if the user wants another item
another_order = input("Do you want to add another item? (Yes/No): ").lower()

if another_order == "yes":
    item_2 = input("Enter the name of the second item: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item '{item_2}' has been added to your order.")
    else:
        print(f"Ordered item '{item_2}' is not available!")

# Print the total order amount
print(f"The total amount of your order is Rs{order_total}")
