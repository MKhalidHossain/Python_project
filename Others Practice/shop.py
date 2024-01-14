'''
This is a very simple text-based Shop Project which is implemented
by Python classes. This application will display the product list of the shop, 
the customer can add and remove the product(s) in the cart from the list, 
and confirm or cancel the purchase. The product data of the project are stored in
a text file.  

Author: Fahmida Yesmin
publisher: https://linuxhint.com

'''

#Import required modules for the shop Project
import random
from datetime import date
from colored import fg, bg, attr

'''
'shop' class is defined here to show the main menu, display product list,
and check the product exist in the file or not 
'''
class shop:
    # Declare list to store the selected product 
    cart_items = []
    # Initialize the cart amount
    cart_amount = 0
    # Initialize the customer balance
    cust_balance = 0
    # Initialize the variable that will take user's input
    answer = ''

    # Define function to display the main menu 
    def display_menu(self):
        print("\n%s%s%s" %(fg(150), '***Welcome to our Cake shop***', attr(0)))
        print("\n%s%s" %(fg(170), '1. Display Products...'))
        print("2. Select Product...")
        print("3. Exit")
        self.answer = input("\nType 1 or 2 or 3:")
    
    # Define function to read and display the product from the text file
    def display_products(self):
       
        print("\nThe list of products are given below:\n")
        with open('products.txt') as f:
            line = f.readline()
            # Print the header of the file
            print("Id\tName\t\tPrice\tMaking Date\tExpire Date")
            while line:
                # Initialize counter to set the space between the fields
                counter = 0
                # Read each line from the file
                line = f.readline()
                # Split each line based on the comma (,) and store in a list
                fieldList = list(line.split(","))
                print('\t')
                # Read each value from the list and print
                for val in fieldList:
                    if counter == 0:
                        space=''
                    else:
                        space='\t' 
                    counter = counter + 1
                    if counter == 3:
                        val = '$' + val
                    print(val, end=space)

    # Define function to check the selected product exists in the file or not
    def check_products(self, search):

        # Open the file for reading 
        with open('products.txt') as f:
            # Read each line of the file
            for line in f:
                # Split the line value based on comma(,)
                fieldList = list(line.split(","))
                for val in fieldList:
                    # Check the selected product match with the value or not
                    if search == val.strip():
                        # Add the price of the product with the cart amount if the serch value found
                        self.cart_amount = self.cart_amount + int(fieldList[2].strip())
                        return True
        # Print message if the selected product does not exist in the file
        print("The product does not exist.")
        return False

'''
'order' class is defined to add product into the cart, remove product
from the cart, and display the cart item
'''
class order(shop):

    # Define function to add product into the cart
    def add_to_cart(self, item):
        # Add product into the cart 
        self.cart_items.append(item)
        print("%s is added in the cart." %(item))

    # Define function to remove product from the cart 
    def remove_from_cart(self, obj):
        item = input("Enter the product name:")
        if item in obj.cart_items: 
            # Remove product from the cart
            obj.cart_items.remove(item)
            print("Product is removed from the cart")
            # Open the file to search the price of the product
            with open('products.txt') as f:
                for line in f:
                    fieldList = list(line.split(","))
                    for val in fieldList:
                        if item == val.strip():
                            # Remove the price of the removed product from the cart amount
                            obj.cart_amount = obj.cart_amount - int(fieldList[2].strip())  
        else:
            print("Product does not exist in the cart.")
        
    # Define function to display the cart items
    def display_cart(self, obj):
        # Check the cart amount to find out the cart is empty or not
        if obj.cart_amount > 0:
            # Display the added cart items
            print("\nYou have added the following item(s) in your cart:\n")
            for val in self.cart_items:
                print(val)
            
            # Print the total cart amount
            print("\n%s%s%d%s"  %(fg(25), 'Total amount:$', obj.cart_amount, attr(0)))

            # Display the second menu
            print("\n1. Add Product")
            print("2. Remove Product")
            print("3. Confirm Payment")
            print("4. Cancel")
            ans = input("\nType 1 or 2 or 3 or 4:")
            return ans

        else:
            # Print message if the cart is empty
            print("You cart is empty.")
            return 0

'''
'customer' class id defined to display the purchase information
after confirming the payment
'''
class customer(order):

    # Define constructor to initialize the customer information
    def __init__(self, name, address, phone, cash):
        name = name
        address = address
        contact_no = phone
        add_cash = cash

    # Define function to display the purchase information with customer details
    def purchase_info(self,obj):
        # Gnerate a random order number
        order_no = random.random()*100000000
        order_no = round(order_no)
        # Initilize the order date
        today = date.today()
        order_date = today.strftime("%B %d, %Y")

        # Print purchase information
        print("\nYour purchase information is given below:\n")
        print("Order No            :%s" %order_no)
        print("Order Date          :%s" %order_date)
        print("Customer's name     :%s" %name)
        print("Customer's address  :%s" %address)
        print("Customer's phone no :%s" %contact_no)

        # Print purchased product information
        print("\nPurchased product list:\n")
        for val in self.cart_items:
           print(val)
        print("\n%s%s%d%s"  %(fg(25), 'Total amount:$', obj.cart_amount, attr(0)))
        print("Thank you.")

# Declare object of the 'shop' class
objShop = shop()
# Declare the infinite loop to display the menu repeatedly 
# until the user presses '3' 
while True:
    # Display the main menu
    objShop.display_menu()
    # Set initial value for the remove_item
    remove_item = False
    
    # Display the main menu if the user presses '1'
    if objShop.answer == '1':
        objShop.display_products()
    # Display the purchase option if the user presses '2'
    elif objShop.answer == '2':
        # Declare object of the 'order' class
        objOrder = order()
        
        # Declare the infinite loop to display the second menu repeatedly 
        # until the user presses '3' or '4'
        while True:
            # Take the product name to add into the cart if the value of remove_item is False
            if remove_item == False:
                item = input("\nType the product name:")
            if item == 'none' :
                # Display the cart after adding or removing the product
                return_val = objOrder.display_cart(objShop)
                # Terminate from the loop if the cart is empty
                if return_val == 0:
                    break
                elif return_val == '1':
                    item = input("Type the product name:")
                    # Check the product exists in the products.txt file or not
                    pro_exist = objShop.check_products(item)
                    # Add the products into the cart if the product exists
                    if pro_exist == True:
                        objOrder.add_to_cart(item)
                    remove_item = False
                    
                elif return_val == '2':
                    # Remove the selected product from the cart
                    return_val = objOrder.remove_from_cart(objShop)
                    remove_item = True
                    
                elif return_val == '3':
                    # Take customer's information
                    name = input("Enter your name:")
                    address = input("Enter your address:")
                    contact_no = input("Enter your contact number:")
                    cash = int(input("Add cash: $"))
                    # Add the cash value with the customer's current balance
                    objShop.cust_balance = objShop.cust_balance + cash

                    # Check the balance of the customer is less than the cart amount ot not 
                    if objShop.cust_balance < objShop.cart_amount:
                        print("You have not enough balance.")
                    else:
                        # Create object of the 'customer' class
                        objCustomer = customer(name, address, contact_no, cash)
                        # Print the purchase information
                        objCustomer.purchase_info(objShop)
                        # Deduct the purchase amount from the customer's balance
                        objShop.cust_balance = cash - objShop.cart_amount                   
                    break
                else:
                    # Print message if the customer cancels the purchase
                    print("You have cancelled your purchase.")
                    break
            else:
                # Add the products into the cart if the product exists
                pro_exist = objShop.check_products(item)
                if pro_exist == True:
                     objOrder.add_to_cart(item)
                print("Type 'none' to stop adding product")
        # Clear the cart list after purchased or cancelled
        objShop.cart_items.clear()
        # Clear the cart amount after purchased or cancelled
        objShop.cart_amount = 0    
    # Terminate from the application if the users presses '3'
    elif objShop.answer == '3':
        print("\nTerminated from the application.")
        exit()
    
