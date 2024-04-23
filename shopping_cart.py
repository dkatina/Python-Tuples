#Create a shopping cart function that continues to prompt the user
#for an action until the users says quit.

#Functionalities:
#The user should be able to add a specific number of an item to the cart
# if the item is already in the cart, the quantity should simply increase

#The user should be able to remove items from a cart by a specific quantity.
#if there are 10 cookies in the cart the user removes 5 cookies, 5 should remain
#if the user removes an equal or greater number of an item, the entire item should be removed

#The user should be able to display their cart, showing the items and quantity.

#When the user quits, print their cart, and a farewell message


def add_to_cart(cart):
    while True:
        try:
            item = input('What item do you want to add to your cart? ').title()
            if not item.isdigit():
                quant = int(input(f'How many {item}(s) do you want to add? '))
            else:
                raise ValueError('This is not an item')
        except ValueError as ve:
            if 'an item' in str(ve):
                print('Invalid Item, please try again')
            else:
                print('Invalid quantity, please only use numbers.')
        else:
            if item in cart:
                #this item is in the cart, so I should increment the value by new quant
                cart[item] += quant
            else:
                cart[item] = quant
            show_cart(cart)
            break

def remove_from_cart(cart):

    while True:
        try:
            item = input('What item do you want to remove? ').title()
            if item in cart:
                quant = int(input(f'How many {item}(s) do you want to remove? '))
            else:
                raise ValueError('Item not in cart!')
        except ValueError as ve:
            if 'in cart' in str(ve):
                print(f'Invalid item, no {item}(s) in your cart!')
            else:
                print(f'Invalid quantity, please only use numbers')
        else:
            if cart[item] > quant:
                cart[item] -= quant
                print(f'Removed {quant} {item}(s)')
            else:
                del cart[item]
                print(f'Removed all {item}(s)')
            break
        finally:
            show_cart(cart)


def show_cart(cart):
    print('Your Cart')
    print('~~~~~~~~~~~~~~')
    for item, quant in cart.items():
        print(f'{item}: {quant}')









def shopper():
    #dict to store item (key) and quantity (value)
    cart = {}

    while True:

        action = input('''
    Would you like to:
    ~~~~~~~~~~~~~~~~~~
    1.) add
    2.) remove
    3.) quit 
    >''').lower()
        if action == 'quit' or action == '3':
            show_cart(cart)
            print('Have A Nice Day!')
            break
        elif action == 'add' or action == '1':
            add_to_cart(cart)
        elif action == 'remove' or action == '2':
            remove_from_cart(cart)
        else:
            print('Invalid Response, try again please')



shopper()






