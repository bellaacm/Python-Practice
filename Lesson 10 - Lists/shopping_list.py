# =====================================================================
# PROJECT: Shopping List & Budget Tracker
# GOAL: Practice adding items to lists and calculating data from them.
# =====================================================================

# INITIALIZE YOUR LISTS
# TODO: Create an empty list called 'shopping_cart' to hold item names.
# TODO: Create an empty list called 'price_list' to hold item prices.
shopping_cart = []
price_list = []

# MAIN
# TODO Create an infinite while loop
while True:

    # Info for user 
    # TODO Output info for user: 
    # Current cart/shopping list
    print("Current cart:", shopping_cart)
    # Current prices
    print("Current prices:", price_list)

    # TODO Output Options for user: 1. Add item to cart, 2. Remove item from cart, 3. Clear cart and restart, 4. View total and checkout
    # TODO Get user input (1-4) and save in variable
    print("1. Add item to cart, 2. Remove item from cart, 3. Clear cart and restart, 4. View total and checkout")
    option = input("Choose an option (1-4): ")

    # -----------------------------------------------------------------
    # OPTION 1: ADD ITEM 
    # -----------------------------------------------------------------
    # TODO Check if option 1 
        # TODO Ask user for the name of the item
        # TODO Add it to shopping list
        # TODO Add user for price of item
        # TODO Change price into a float
        # TODO Add price to price list

    if option == '1':
        item_name = input("Enter item name: ")
        shopping_cart.append(item_name)
        item_price = input("Enter item price: ")
        item_price = float(item_price)
        price_list.append(item_price)

    # -----------------------------------------------------------------
    # OPTION 2: REMOVE ITEM 
    # -----------------------------------------------------------------
    # TODO Else check if option 2
        # TODO Ask user for the name of the item they want to remove
        # TODO Use .index() to get the index of the item and save in variable
        # TODO Remove the item from cart
        # TODO Remove the price (using its index) from the price list

if option == '2':
    item_name = input ('Enter the name of the item you want to remove: ')
    item_index = shopping_cart.index(item_name)  
    shopping_cart.pop(item_index)
    price_list.pop(item_index) 
    
     # -----------------------------------------------------------------
    # OPTION 3: CLEAR CART (Practice clearing a list)
    # -----------------------------------------------------------------
    # TODO Else check if option 3
        # TODO: Use the .clear() method on both lists to empty them out.
        # TODO Tell them their cart is empty.

if option == '3':
    shopping_cart.clear()
    price_list.clear()
    print('Your cart is now empty.')

    # -----------------------------------------------------------------
    # OPTION 4: CHECKOUT
    # -----------------------------------------------------------------
    # TODO Else check if option 4

        
        # TODO Display the results
        # TODO Exit the loop (to exit the program)

if option == '4':
    total_cost = sum(price_list)
    print(total_cost)
    exit

else:
    print("Option is invalid")
    print("Try again")
   
# ====================================================================
# EXTENSION
# Add a budget to the list
# TODO Tell them if their cart is over budget
# TODO Recommend items to remove based on their price.

# =====================================================================
# EXPERT
# Change your program to use dictionaries so prices are connected to shopping items
# Display the cart in alphabetical order
# Add an option to display the cart in order of price.