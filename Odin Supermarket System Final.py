# -----------------SUPERMARKET MANAGEMENT SYSTEM--------------------
# Initial List of items available (temporary)
items = [
    {
        "name": "Apple",
        "quantity": 999,
        "price(Php)": 15
    },
    {
        "name": "Banana",
        "quantity": 999,
        "price(Php)": 25
    },
    {
        "name": "Orange",
        "quantity": 999,
        "price(Php)": 25
    }
]

# This portion covers the login of the user (userdictionary is the usernames and their corresponding passwords)
userdictionary = {
    "Admin": "AdminPass",
    "Cashier": "CashierPass"
}

orderlist = {}
# User Cart
cart = []

delivery_cart = []

delivery_list = []
from time import sleep
import threading



def delivery_timer(delivery_index):
    timer = 600
    while timer > 0:
        sleep(1)
        timer -= 1
        delivery_list[delivery_index]["Countdown"] = timer
    #print("\n---------------------------------")
    #print(f"Delivery {delivery_index + 1} has arrived at {delivery_list[delivery_index]['Address']}")
    #print("---------------------------------")
# LOGIN FUNCTION
def loginfunc():
    # while True:
    login = input("Enter Username: ")
    loginp = input("Enter Password: ")
    if login in userdictionary.keys():

        if loginp in userdictionary[login]:
            print("Login Successfully!")
            userstate = login
            if userstate == "Admin":
                AdminFunc()
            if userstate == "Cashier":
                CashierFunc()
        else:
            print("Invalid Password!")
            (loginfunc())
    else:
        print("Invalid Login!")
        (loginfunc())

def AdminFunc():

    while True:
        display = input('Press enter to continue.')
        print('------------------Welcome to the supermarket------------------')
        print(
            '1. View items\n2. Add items to inventory\n3. Search items\n4. Manage items \n5. View the status of the ongoing deliveries\n6. Exit')
        choice = input('Enter the number of your choice: ')

        if choice == '1':
            print('------------------View Items------------------')

            print('The number of items in the inventory are: ', len(items))
            while len(items) != 0:
                print('Here are all the items available in the supermarket.')
                for item in items:
                    for key, value in item.items():
                        print(key, ':', value)
                    print("")
                break

        elif choice == '2':
            print('------------------Add Items to Inventory------------------')
            print('To add an item fill in the form')

            item = {}
            item['name'] = input('Item name: ')
            while True:
                try:
                    item['quantity'] = int(input('Item quantity: '))
                    break
                except ValueError:
                    print('Quantity should only be in digits')
            while True:
                try:
                    item['price'] = int(input('Price (₱) : '))
                    break
                except ValueError:
                    print('Price should only be in digits')
            for i in items:
                if i['name'].lower() == item['name'].lower():
                    print('Item already exists in inventory')
                    break
            else:
                print('Item has been successfully added.')
                items.append(item)

        elif choice == '3':
            print('------------------Search items------------------')
            find_item = input('Enter the item\'s name to search in inventory: ')
            found = False
            for item in items:
                if item['name'].lower() == find_item.lower():
                    print(f"{'Name:':<10}{item['name']}")
                    print(f"{'Quantity:':<10}{item['quantity']}")
                    print(f"{'Price:':<10}₱{item['price(Php)']}")
                    found = True
                    break
            if not found:
                print('Item not found.')

        elif choice == '4':
            print('------------------Manage items------------------')
            print('1. Edit an Item\n2. Remove an Item\n3. Exit')
            choice = input('Enter the number of your choice: ')

            if choice == '1':
                print('Cart Items:')
                print('------------------------------------')
                for item in items:
                    print(f"Name: {item['name']}\nQuantity: {item['quantity']}\nPrice: ₱{item['price(Php)']}")
                print('------------------------------------')
                item_name = input('Enter the name of the item that you want to edit: ')
                for item in items:
                    if item_name.lower() == item['name'].lower():
                        print('Here are the current details of ' + item_name)
                        print(f"Name: {item['name']}\nQuantity: {item['quantity']}\nPrice: ₱{item['price(Php)']}")
                        item['name'] = input('Item name: ')
                        while True:
                            try:
                                item['quantity'] = int(input('Item quantity: '))
                                break
                            except ValueError:
                                print('Quantity should only be in digits')
                        while True:
                            try:
                                item['price(Php)'] = float(input('Price (Php): '))
                                break
                            except ValueError:
                                print('Price should only be in digits')
                        print('Item has been successfully updated.')
                        print(f"Name: {item['name']}\nQuantity: {item['quantity']}\nPrice: ₱{item['price(Php)']}")
                        break
                else:
                    print('Item not found')

            if choice == '2':
                for item in items:
                    print(f"{item['name']} - Quantity: {item['quantity']} - Price: ₱{item['price(Php)']}")
                name_to_remove = input("Enter the name of the item to remove: ")

                for item in items:
                    if item['name'].lower() == name_to_remove.lower():
                        while True:
                            try:
                                quantity_to_remove = int(input("Enter the quantity to remove: "))
                                if quantity_to_remove > item['quantity']:
                                    print("Cannot remove more than available quantity.")
                                else:
                                    item['quantity'] -= quantity_to_remove
                                    if quantity_to_remove == 1:
                                        print(f"{quantity_to_remove} {item['name']} removed successfully!")
                                    else:
                                        print(f"{quantity_to_remove} {item['name']}s removed successfully!")
                                break
                            except ValueError:
                                print("Quantity should be a number.")
                        if item['quantity'] == 0:
                            items.remove(item)
                            print(f"{item['name']} removed from inventory as there are no more quantities available.")
                        break
                else:
                    print("Item not found in the list.")

            if choice == '3':
                pass

        elif choice == '5':
            print('------------------Status of Ongoing Deliveries------------------')
            for index, delivery in enumerate(delivery_list):
                print(f"Delivery {index + 1}:")

                print(f"Address: {delivery['Address']}")

                print(f"Total: {delivery['Total']}")

                print(f"Cash Payment: {delivery['Payment']}")
                if delivery['Countdown'] != 0:
                    print(f"Time Until Delivery: {delivery['Countdown']}")
                else:
                    print("Delivery has been completed.")
                print("---------------------------------")
                print("Cart:")
                for item in delivery["Cart"]:
                  print(f"{item['name']} - Quantity: {item['quantity']} - Item Price: ₱{item['price(Php)']}")

                print("---------------------------------")
        elif choice == '6':
            print('------------------Exited------------------')
            break

        else:
            print('You entered an invalid option')
    pass

def CashierFunc():
    while True:
        display = input('Press enter to continue.')
        print('------------------Welcome to the supermarket------------------')
        print('1. View items\n2. Purchase items\n3. Manage Cart \n4. Search items \n5. Delivery Menu \n6. Exit')
        choice = input('Enter the number of your choice : ')

        if choice == '1':
            print('------------------View Items------------------')

            print('The number of items in the inventory are : ', len(items))
            while len(items) != 0:
                print('Here are all the items available in the supermarket.')
                for item in items:
                    for key, value in item.items():
                        print(key, ':', value)
                    print("")
                break

        elif choice == '2':
            print('------------------Purchase items------------------')
            for item in items:
                print(f"{item['name']}: ₱{item['price(Php)']}, {item['quantity']} in stock")
            print('--------------------------------------------------')
            purchase_item = input('which item do you want to purchase? Enter name: ')
            for item in items:
                if purchase_item.lower() == item['name'].lower():
                    if item['quantity'] != 0:
                        cart_item_amount = int(input("How many of the items do you want? "))
                        cart_item = item.copy()  # create a copy of the item dictionary
                        cart_item['quantity'] = cart_item_amount
                        cart.append(cart_item)  # append the copy to the cart list
                        item['quantity'] -= cart_item_amount
                        print('------------------Current Cart------------------')
                        for cart_item in cart:
                            print(f"{cart_item['name']}: {cart_item['quantity']}")
                        print('--------------------------------------------------')
                        print('------------------Current Inventory------------------')
                        for inventory_item in items:
                            print(f"{inventory_item['name']}: {inventory_item['quantity']} in stock")
                        print('--------------------------------------------------')
                    else:
                        print("Item out of stock!")

        elif choice == '3':
            print('------------------Current items in Cart------------------')
            for i, item in enumerate(cart):
                print(f"{i + 1}. {item['name']} - Quantity: {item['quantity']} - Price: ₱{item['price(Php)']}")
            print('----------------------------------------------------------')

            print('1. Edit/Remove an Item\n2. Checkout \n3. Exit')
            choice = input('Enter the number of your choice: ')

            if choice == '1':
                print('------------------Manage Cart------------------')
                print('Current Items in Cart: ')
                for item in cart:
                    print(f"{item['name']}: {item['quantity']}")
                print('--------------------------------------------------')
                name_to_remove = input("Enter the name of the item to remove: ")

                for item in cart:
                    if item['name'].lower() == name_to_remove.lower():
                        while True:
                            try:
                                quantity_to_remove = int(input(f"How many {name_to_remove} do you want to remove? "))
                                if quantity_to_remove <= 0:
                                    print("Please enter a positive quantity.")
                                elif quantity_to_remove > item['quantity']:
                                    print("You cannot remove more than the quantity in the cart.")
                                else:
                                    break
                            except ValueError:
                                print("Please enter a valid quantity.")

                        item['quantity'] -= quantity_to_remove

                        if item['quantity'] == 0:
                            cart.remove(item)

                        print(f"{quantity_to_remove} {name_to_remove}(s) removed successfully!")
                        break
                else:
                    print("Item not found in the cart.")

            if choice == '2':
                final = 0
                for item in cart:
                    quantity = item['quantity']
                    price = item['price(Php)']

                    # calculate the total
                    total = quantity * price

                    final += total
                print("The total price is:",final,"Php")

            if choice == '3':
                pass

        elif choice == '4':
            print('------------------Search items------------------')
            find_item = input('Enter the item\'s name to search in inventory: ')
            found = False
            for item in items:
                if item['name'].lower() == find_item.lower():
                    print('The item named ' + find_item + ' is displayed below with its details')
                    if item['name'].lower() == find_item.lower():
                        print(f"{'Name:':<10}{item['name']}")
                        print(f"{'Quantity:':<10}{item['quantity']}")
                        print(f"{'Price:':<10}₱{item['price(Php)']}")
                    found = True
                    break
                if not found:
                    print('item not found.')

        elif choice == "5":
            print('-----------------Delivery Menu------------------')
            print("1. Appoint a delivery order for a customer")

            print("2. Check Delivery Status")

            print("3. Return to Menu")

            delivery_option = input("Enter the number of your choice: ")

            if delivery_option == "1":

                print("--------Appointing delivery order----------")


                print('Please double check your order')

                for i, item in enumerate(cart):
                    print(f"{i + 1}. {item['name']} - Quantity: {item['quantity']} - Price: ₱{item['price(Php)']}")

                    final = 0

                for item in cart:
                    quantity = item['quantity']
                    price = item['price(Php)']

                        # calculate the total
                    total = quantity * price

                    final += total

                print("The total price is:",final,"Php")


                print('-------------------------------------------')
                print('Proceed to Delivery? -y/n-')
                delivery_choice = input('Enter your choice : ')
                # get order details
                if delivery_choice == 'y':
                    print('-------------------------------------------')
                    Address = input("Enter your delivery address: ")

                    Payment = int(input("How much will you be paying: "))
                    print('-------------------------------------------')
                    if Payment >= final:

                        delivery_cart = cart.copy()

                        order = {"Address": Address, "Payment": Payment, "Total": final, "Cart": delivery_cart}

                        # add order to delivery list

                        delivery_list.append(order)

                        # start delivery timer in background thread

                        delivery_thread = threading.Thread(target=delivery_timer, args=(len(delivery_list) - 1,))

                        delivery_thread.start()

                        print("---------------------------------")

                        print("Delivery details saved successfully.\n")

                        print("---------------------------------")

                        print(f"Address: {Address}")
                        print(f"Total: {final}")
                        print("---------------------------------")
                        print("Cart:")
                        for item in cart:
                            print(f"{item['name']} - Quantity: {item['quantity']} - Price: ₱{item['price(Php)']}")
                        print("---------------------------------")
                        print()

                        cart.clear()

                    else:
                        print("Insufficient Payment.\nReturning to Menu.")



                elif delivery_choice == 'n':
                    print('Returning to menu.\n')
                else:
                    print('Invalid choice')


            elif delivery_option == "2":

                print("---------Delivery Status---------")

                for index, delivery in enumerate(delivery_list):

                    print(f"Delivery {index + 1}:")

                    print(f"Address: {delivery['Address']}")

                    print(f"Total: {delivery['Total']}")

                    print(f"Cash Payment: {delivery['Payment']}")
                    if delivery['Countdown'] != 0:
                        print(f"Time (Seconds) Until Delivery: {delivery['Countdown']}")
                    else:
                        print("Delivery has been completed.")

                    print("---------------------------------")

                    print("Cart:")
                    for item in delivery["Cart"]:
                        print(f"{item['name']} - Quantity: {item['quantity']} - Item Price: ₱{item['price(Php)']}")

                    print("---------------------------------")

            elif delivery_option == "3":

                print("Returning to Menu")

            else:
                print('You entered an invalid option')

        elif choice == '6':
            print('------------------Exited------------------')
            break

        else:
            print('You entered an invalid option')
    pass##TAPOS NA TO

def OrderFunc():
    total_order_price = 0
    print('------------------Order------------------')
    print("To order, please fill out the form below: ")

    item_order = input("Please enter the name of the item to order: ")
    item_order_quantity = int(input("Please enter the desired quantity of the item you want to order: "))

    for item in items:
        if item['name'].lower() == order_item.lower():
            if item['quantity'] >= order_quantity:
                price_order = item['price(Php)'] * item_order_quantity
                total_order_price += price_order
                orderlist[item_order] = item_order_quantity
                print("Order Successful!")
                print(f"Order Details: {item_order_quantity} {item_order}     for {price_order} Php")
        else:
            print("Not enough stock for this item. Order failed!")
        break
    else:
        print("Invalid item. Not found in the inventory!")

    return total_order_price

loginfunc()